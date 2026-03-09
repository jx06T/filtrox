import google.generativeai as genai
from abc import ABC, abstractmethod

# =================================================================
# Layer 1: 模型基礎設施層 (Infrastructure Layer)
# 職責：API 認證、模型配置、錯誤重試、原始文本生成
# =================================================================

class BaseLLM(ABC):
    """抽象基類：定義所有 LLM 都必須具備的接口"""
    @abstractmethod
    def generate_text(self, prompt: str) -> str:
        pass

class Gemini(BaseLLM):
    """Google Gemini 的具體實作"""
    def __init__(self, api_key: str, model_name: str = 'gemini-2.5-flash'):
        self.api_key = api_key
        self.model_name = model_name
        self._configure()
    
    def _configure(self):
        genai.configure(api_key=self.api_key)
        # 這裡可以設定 generation_config (temperature 等)
        self.model = genai.GenerativeModel(self.model_name)

    def generate_text(self, prompt: str) -> str:
        try:
            chat = self.model.start_chat(history=[])
            response = chat.send_message(prompt)
            return response.text
        except Exception as e:
            # 這裡只處理連線層級的錯誤
            raise ConnectionError(f"LLM Provider Error: {str(e)}")
