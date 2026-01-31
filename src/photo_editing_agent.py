import json
import re
from typing import List, Dict, Any, Optional

from .llm_backend import BaseLLM , Gemini
from dotenv import load_dotenv

# 假設這是從您的 Snippet 3 引入的
# from ai_engine_module import AIEngine 


class PhotoEditingAgent:
    """
    專門用於控制 Darktable 'colorbalancergb' 模組的 AI 代理
    """
    def __init__(self, llm_provider: BaseLLM):
        self.llm = llm_provider
        
        # === 關鍵：這裡的 Schema 必須嚴格對應 Darktable C Struct 的變數名 ===
        # 參考前面的 binary layout 代碼：FIELD_ORDER_32F
        self.param_schema = {
            # --- 4-Way Controls (Shadows, Midtones, Highlights, Global) ---
            # C = Chroma (Saturation), Y = Luminance (Brightness), H = Hue
            "global_C": "float (-0.5 to 0.5) - Global Saturation adjustment",
            "global_Y": "float (-0.5 to 0.5) - Global Brightness",
            "global_H": "float (-180 to 180) - Global Hue Tint",
            
            "shadows_C": "float (-0.5 to 0.5) - Shadows Saturation",
            "shadows_Y": "float (-0.3 to 0.3) - Shadows Brightness",
            "shadows_H": "float (0 to 360) - Shadows Hue Tint",
            
            "midtones_C": "float (-0.5 to 0.5) - Midtones Saturation",
            "midtones_Y": "float (-0.3 to 0.3) - Midtones Brightness",
            "midtones_H": "float (0 to 360) - Midtones Hue Tint",
            
            "highlights_C": "float (-0.5 to 0.5) - Highlights Saturation",
            "highlights_Y": "float (-0.3 to 0.3) - Highlights Brightness",
            "highlights_H": "float (0 to 360) - Highlights Hue Tint",
            
            # --- Master Controls ---
            "contrast": "float (-0.5 to 0.5) - Global Contrast center",
            "vibrance": "float (-0.5 to 0.5) - Smart saturation (Vibrance)",
            "saturation_global": "float (0.0 to 2.0) - Linear Saturation Multiplier (Default 1.0)",
            
            # --- Optional (Fulcrums) ---
            # "white_fulcrum": "float - Defines what is considered white (Default 0.0)"
        }

    def _get_system_instruction(self) -> str:
        # load from system_prompt.md
        system_prompt = ""
        with open("system_prompt.md", "r", encoding="utf-8") as f:
            system_prompt = f.read()
        return system_prompt

    def _clean_json_output(self, raw_text: str) -> str:
        """清理 LLM 的輸出"""
        text = raw_text.strip()
        pattern = r"```(?:json)?\s*(.*?)\s*```"
        match = re.search(pattern, text, re.DOTALL)
        if match:
            text = match.group(1)
        return text

    def _execute_prompt(self, task_prompt: str) -> List[Dict[str, Any]]:
        """執行 Prompt 並解析結果"""
        full_prompt = f"{self._get_system_instruction()}\n\n---\n\n{task_prompt}"

        raw_response = self.llm.generate_text(full_prompt)
        raw_response = raw_response.replace('```json', '')  # 有時候會多個 json 標籤，先替換掉
        raw_response = raw_response.replace('```', '')
        print(raw_response)

        raw_json = json.loads(self._clean_json_output(raw_response))

        return raw_json['configs']

    def _format_disliked_factors(self, disliked_factors: Optional[Dict[str, List[float]]]) -> str:
        if not disliked_factors:
            return ""
        compact = {k: v for k, v in disliked_factors.items() if isinstance(v, list) and v}
        if not compact:
            return ""
        return f"\nDisliked factor values (avoid these numbers or close neighbors): {json.dumps(compact)}"

    def _format_preferred_factors(self, preferred_factors: Optional[Dict[str, float]]) -> str:
        if not preferred_factors:
            return ""
        return f"\nPreferred factor center (stay close to these values): {json.dumps(preferred_factors)}"

    def _format_variation_scale(self, variation_scale: Optional[float]) -> str:
        if variation_scale is None:
            return ""
        return f"\nVariation scale: {variation_scale} (lower means smaller changes around preferred factors)."

    # ================= 業務場景方法 =================

    def cold_start(self, user_request: str) -> List[Dict]:
        """場景 1: 冷啟動 (Cold Start)"""
        prompt = f"""
        **Task: Cold Start Generation**
        User Request: "{user_request}"
        
        Goal: Generate 3 DISTINCT visual styles using strictly Color Balance RGB parameters.
        Example: 
        - If request is "Warm Cinematic", focus on 'midtones_H' (orange) and 'shadows_H' (teal).
        - If request is "High Contrast B&W", set 'saturation_global' to 0 and boost 'contrast'.
        """
        return self._execute_prompt(prompt)

    def auto_iterate(
        self,
        current_params: Dict,
        disliked_factors: Optional[Dict[str, List[float]]] = None,
        preferred_factors: Optional[Dict[str, float]] = None,
        variation_scale: Optional[float] = None,
    ) -> List[Dict]:
        """場景 2: 自動迭代 (Auto Iteration) - 不需提示詞"""
        prompt = f"""
        **Task: Refinement (Auto-Iteration)**
        The user selected this specific style:
        {json.dumps(current_params)}
        {self._format_disliked_factors(disliked_factors)}
        {self._format_preferred_factors(preferred_factors)}
        {self._format_variation_scale(variation_scale)}
        
        Goal: Generate 3 variations based on this baseline:
        1. "Polished": Keep the vibe but fix potential issues (e.g. check if skin tones/midtones look natural).
        2. "Intensified": Push the color grading stronger (increase Chroma/Contrast values).
        3. "Softened": Reduce the effect intensity (bring values closer to 0).
        Keep variations closer to preferred factors as iterations increase.
        Always include the required "factors" object for each config.
        """
        return self._execute_prompt(prompt)

    def text_refine(
        self,
        current_params: Dict,
        user_feedback: str,
        disliked_factors: Optional[Dict[str, List[float]]] = None,
        preferred_factors: Optional[Dict[str, float]] = None,
        variation_scale: Optional[float] = None,
    ) -> List[Dict]:
        """場景 3: 指定修飾 (Text Refinement)"""
        prompt = f"""
        **Task: Specific Adjustment**
        Base Parameters: {json.dumps(current_params)}
        User Feedback: "{user_feedback}"
        {self._format_disliked_factors(disliked_factors)}
        {self._format_preferred_factors(preferred_factors)}
        {self._format_variation_scale(variation_scale)}
        
        Goal: Apply the feedback to the Base Parameters.
        Generate 3 versions: Subtle change, Moderate change, Strong change.
        Keep variations closer to preferred factors as iterations increase.
        Always include the required "factors" object for each config.
        """
        return self._execute_prompt(prompt)
    


if __name__ == "__main__":
    import os
    
    # 1. 設置 API Key
    load_dotenv()  
    api_key = os.getenv("GEMINI_API_KEY")
    
    # 2. 初始化 Infrastructure
    llm_service = Gemini(api_key=api_key)
    
    # 3. 初始化 Agent (注入 GeminiService)
    agent = PhotoEditingAgent(llm_provider=llm_service)
    
    # 4. 測試 Cold Start
    print("🤖 正在生成 '賽博龐克' 風格...")
    variations = agent.cold_start("Cyberpunk style, neon lights")
    
    if variations:
        selected = variations[0]
        print(f"\n✅ 選擇方案: {selected['name']}")
        print(f"📝 理由: {selected['reasoning']}")
        print(f"🔧 參數: {json.dumps(selected['parameters'], indent=2)}")
        
        # 5. 測試 Auto Iterate (假設使用者點了這張圖)
        print("\n🤖 正在基於選擇進行自動迭代...")
        refined_vars = agent.auto_iterate(selected['parameters'])
        
        for idx, var in enumerate(refined_vars):
            print(f"  > 變體 {idx+1}: {var['name']} - {var['reasoning']}")
