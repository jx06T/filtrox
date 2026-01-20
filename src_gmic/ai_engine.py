import google.generativeai as genai

class AIEngine:
    def __init__(self, api_key: str, reference_content: str):
        genai.configure(api_key=api_key)
        # 保持使用您指定的 gemini-2.5-flash
        # self.model = genai.GenerativeModel('gemini-2.5-flash') 
        self.model = genai.GenerativeModel('gemini-2.5-flash-lite') 
        self.reference_content = reference_content

    def _build_system_prompt(self, base_command: str = None):
        # 判斷是否為「修改模式」
        context_instruction = ""
        if base_command:
            context_instruction = f"The user is CURRENTLY using these commands: `{base_command}`. " \
                                  f"Based on the new request, you should MODIFY or ADD to these parameters " \
                                  f"to produce a single combined G'MIC command string."
        else:
            context_instruction = "The user is starting a new image modification."

        return f"""
You are a G'MIC command conversion expert.
{context_instruction}
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
6. Command Prefixes (+ vs -): 
   - Use '-' prefix (e.g., -blur 5) to modify the current image in-place. 
   - Use '+' prefix (e.g., +blur 5) to create a NEW image/layer based on the current one, keeping the original intact in the stack.
7. Layer/Stack Concept: 
   - G'MIC manages images in a 'stack' (list of layers). 
   - You can refer to images by index: [0] is the first image, [-1] is the last/current image.
   - For complex effects, you can duplicate layers, process them separately, and then use blending commands like '-blend' or '-overlay' to merge them.
   - Always ensure the final desired result is at the end of the stack or clearly selected.
"""

    def get_gmic_command(self, user_prompt: str, base_command: str = None) -> str:
        try:
            chat = self.model.start_chat(history=[])
            system_msg = self._build_system_prompt(base_command)
            
            # 將指令背景與使用者新需求結合
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