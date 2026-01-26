import os
from typing import Optional

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
try:
    import google.generativeai as genai
except Exception:
    genai = None


class AIEngine:
    def __init__(
        self,
        qwen_model_name: str,
        qwen_lora_path: str = "",
        gemini_api_key: str = "",
        llm_provider: str = "qwen",
        device: Optional[str] = None,
    ):
        self.qwen_model_name = qwen_model_name
        self.qwen_lora_path = qwen_lora_path or ""
        self.gemini_api_key = gemini_api_key or ""
        self.llm_provider = (llm_provider or "qwen").lower()
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        if self.llm_provider != "gemini":
            if not qwen_model_name or qwen_model_name == "path-or-hf-id":
                raise ValueError("Missing QWEN_MODEL_NAME")
        self._load_models()

    def _load_models(self) -> None:
        if self.llm_provider == "gemini":
            if self.gemini_api_key and genai:
                genai.configure(api_key=self.gemini_api_key)
                self.gemini_model = genai.GenerativeModel("gemini-2.5-flash-lite")
            else:
                self.gemini_model = None
            self.qwen_tokenizer = None
            self.qwen_model = None
            return

        qwen_kwargs = {
            "low_cpu_mem_usage": True,
            "device_map": "auto",
            "trust_remote_code": True,
        }
        if torch.cuda.is_available():
            qwen_kwargs["torch_dtype"] = torch.float16
        try:
            import bitsandbytes  # noqa: F401

            qwen_kwargs["load_in_4bit"] = True
        except Exception:
            pass

        self.qwen_tokenizer = AutoTokenizer.from_pretrained(
            self.qwen_model_name, use_fast=True, trust_remote_code=True
        )
        self.qwen_model = AutoModelForCausalLM.from_pretrained(
            self.qwen_model_name, **qwen_kwargs
        )
        if self.qwen_lora_path:
            try:
                from peft import PeftModel

                self.qwen_model = PeftModel.from_pretrained(
                    self.qwen_model, self.qwen_lora_path
                )
            except Exception as exc:
                raise RuntimeError(f"Failed to load Qwen LoRA: {exc}") from exc
        self.qwen_model.eval()

        if self.gemini_api_key and genai:
            genai.configure(api_key=self.gemini_api_key)
            self.gemini_model = genai.GenerativeModel("gemini-2.5-flash-lite")
        else:
            self.gemini_model = None

    def generate(
        self,
        user_prompt: str,
        system_prompt: str,
        max_new_tokens: int = 32768,
        min_new_tokens: int = 1,
    ) -> str:
        if self.llm_provider == "gemini":
            return self._generate_gemini(user_prompt, system_prompt)
        return self._generate_qwen(
            user_prompt,
            system_prompt,
            max_new_tokens=max_new_tokens,
            min_new_tokens=min_new_tokens,
        )

    def _generate_qwen(
        self,
        user_prompt: str,
        system_prompt: str,
        max_new_tokens: int = 32768,
        min_new_tokens: int = 1,
    ) -> str:
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]
        input_ids = self.qwen_tokenizer.apply_chat_template(
            messages, return_tensors="pt", add_generation_prompt=True
        )
        input_ids = input_ids.to(self.qwen_model.device)
        with torch.no_grad():
            output_ids = self.qwen_model.generate(
                input_ids,
                max_new_tokens=max_new_tokens,
                min_new_tokens=min_new_tokens,
                eos_token_id=self.qwen_tokenizer.eos_token_id,
                do_sample=False,
            )
        output_text = self.qwen_tokenizer.decode(
            output_ids[0][input_ids.shape[-1] :], skip_special_tokens=True
        )
        return output_text.strip()

    def _generate_gemini(self, user_prompt: str, system_prompt: str) -> str:
        if not self.gemini_model:
            raise RuntimeError("Gemini model is not configured.")
        chat = self.gemini_model.start_chat(history=[])
        full_prompt = f"{system_prompt}\n\nUser Request: {user_prompt}"
        response = chat.send_message(full_prompt)
        return response.text.strip()


def load_engine_from_env(env: Optional[dict] = None) -> AIEngine:
    env = env or os.environ
    qwen_model_name = env.get("QWEN_MODEL_NAME", "C:/models/qwen2.5-coder-7b-instruct")
    qwen_lora_path = env.get("QWEN_LORA_PATH", "")
    gemini_api_key = env.get("GEMINI_API_KEY", "AIzaSyCeNdxGuPuZwjQ6D-tSin7jTsGaob8ZEbU")
    llm_provider = env.get("LLM_PROVIDER", "gemini")
    return AIEngine(qwen_model_name, qwen_lora_path, gemini_api_key, llm_provider)
