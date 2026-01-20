import os
from typing import Optional

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM


class AIEngine:
    def __init__(
        self,
        qwen_model_name: str,
        qwen_lora_path: str = "",
        device: Optional[str] = None,
    ):
        if not qwen_model_name or qwen_model_name == "path-or-hf-id":
            raise ValueError("Missing QWEN_MODEL_NAME")
        self.qwen_model_name = qwen_model_name
        self.qwen_lora_path = qwen_lora_path or ""
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self._load_models()

    def _load_models(self) -> None:
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

    def generate(
        self,
        user_prompt: str,
        system_prompt: str,
        max_new_tokens: int = 256,
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


def load_engine_from_env(env: Optional[dict] = None) -> AIEngine:
    env = env or os.environ
    qwen_model_name = env.get("QWEN_MODEL_NAME", "")
    qwen_lora_path = env.get("QWEN_LORA_PATH", "")
    return AIEngine(qwen_model_name, qwen_lora_path)
