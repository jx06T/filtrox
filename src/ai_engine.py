import google.generativeai as genai

class AIEngine:
    def __init__(self, api_key: str, reference_content: str):
        genai.configure(api_key=api_key)
        # 可根據需求更換模型版本
        self.model = genai.GenerativeModel('gemini-2.5-flash') 

        self.reference_content = reference_content

    def _build_system_prompt(self):
        return f"""
You are a G'MIC command conversion expert.
Based on the reference documentation and user request, generate ONLY the G'MIC parameters.

--- Reference Documentation ---
{self.reference_content}
--- End ---

Rules:
1. Output ONLY the parameter portion (no 'gmic' prefix, no input/output filenames).
2. Use fully specified parameters even for default values.
3. If multiple effects are needed, separate with spaces (e.g., -blur 2 -sharpen 50).
4. No Markdown formatting or code blocks.
5. Minimize use of 'clut'; prefer basic adjustment commands first.
"""

    def get_gmic_command(self, user_prompt: str) -> str:
        try:
            chat = self.model.start_chat(history=[])
            system_msg = self._build_system_prompt()
            full_prompt = f"{system_msg}\n\nUser Request: {user_prompt}"
            
            response = chat.send_message(full_prompt)
            command = response.text.strip()
            
            # 清理常見的 AI 錯誤輸出
            command = command.replace("`", "").replace("bash", "").strip()
            if command.lower().startswith("gmic "):
                command = command[5:]
            
            return command
        except Exception as e:
            return f"Error: {str(e)}"