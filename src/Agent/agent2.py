import json
import re
from pathlib import Path

from Agent.agent import APITestPlanAgent

PRE_PAYLOAD_SEPARATOR = f"\n\n---\n**Generated Payload:**\n"
POST_PAYLOAD_SEPARATOR = f"--- End of Generated Payload ---\n"
PROMPT_FILE = PROMPT_FILE_PATH = Path(__file__).parent / "prompt.txt"


class APITestPlanWithExamples(APITestPlanAgent):
    def get_test_plan(self, endpoint_info, generation_config=None):
        raw_plan = super().generate_plan_for_endpoint(endpoint_info, generation_config)

        if raw_plan.startswith("Error:"):
            return raw_plan

        payload = self._extract_json_payload(raw_plan)

        is_valid, validation_error = self.validate_json(payload)

        if is_valid:
            final_plan = raw_plan + PRE_PAYLOAD_SEPARATOR + f"```json\n{json.dumps(payload, indent=2)}\n```" + POST_PAYLOAD_SEPARATOR
        else:
            final_plan = raw_plan + PRE_PAYLOAD_SEPARATOR + f" No valid payload was returned. Reason: {validation_error}" + POST_PAYLOAD_SEPARATOR

        return final_plan

    def _extract_json_payload(self, markdown_text):
        # Regex to find a JSON code block
        match = re.search(r"```json\s*([\s\S]*?)\s*```", markdown_text)
        if not match:
            return None

        try:
            return json.loads(match.group(1))
        except json.JSONDecodeError:
            return None

    def validate_json(self, payload, required_keys = None):
        if not payload or not isinstance(payload, dict):
            return False, "Payload is not a valid JSON object."

        missing_keys = [key for key in required_keys if key not in payload]

        if missing_keys:
            return False, f"Missing required keys: {', '.join(missing_keys)}"

        return True, None
