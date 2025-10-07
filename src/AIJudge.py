import json
from config import GEMINI_API_KEY
import google.generativeai as genai

class AIJudge:
    def __init__(self, api_key=GEMINI_API_KEY, model_name="gemini-1.5-pro-latest"):
        genai.configure(api_key=api_key)
        self.model_name = model_name
        self.model = genai.GenerativeModel(self.model_name)

    def validate_payload(self, payload_to_validate_str: str, json_schema: dict):
        judge_prompt = f"""
        You are an AI Test Automation expert. Your task is to validate a JSON payload against a given JSON schema.

        Respond ONLY with a JSON object containing two keys: "conforms" (boolean) and "reasoning" (string).

        **JSON Schema:**
        ```json
        {json.dumps(json_schema, indent=2)}
        ```

        **Payload to Validate:**
        ```json
        {payload_to_validate_str}
        ```
        """
        verdict_str = self.model.generate_content(judge_prompt).text

        try:
            verdict = json.loads(verdict_str)
            conforms = verdict.get("conforms", False)
            reasoning = verdict.get("reasoning", "The judge returned an invalid or incomplete response.")
            return conforms, reasoning
        except json.JSONDecodeError:
            return False, f"The AI Judge returned a non-JSON response: {verdict_str}"
