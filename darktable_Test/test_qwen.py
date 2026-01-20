import os
import re
from pathlib import Path

from src_gmic.ai_engine import AIEngine


def _load_secrets(path: Path) -> dict:
    data = {}
    if not path.exists():
        return data
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        match = re.match(r"([A-Z0-9_]+)\s*=\s*\"(.*)\"\s*$", line)
        if match:
            data[match.group(1)] = match.group(2)
    return data


def main() -> int:
    base_dir = Path(__file__).parent
    secrets = _load_secrets(base_dir / ".streamlit" / "secrets.toml")

    qwen_model = os.environ.get("QWEN_MODEL_NAME") or secrets.get("QWEN_MODEL_NAME", "")
    qwen_lora = os.environ.get("QWEN_LORA_PATH") or secrets.get("QWEN_LORA_PATH", "")
    if not qwen_model:
        print("[ERR] QWEN_MODEL_NAME is not set in env or .streamlit/secrets.toml")
        return 2

    engine = AIEngine(qwen_model, qwen_lora)
    system_prompt = "You are a short, direct assistant."
    user_prompt = "Say hello in 3 words."
    output = engine.generate(user_prompt, system_prompt, max_new_tokens=16, min_new_tokens=1)
    print("[OK] Output:", output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
