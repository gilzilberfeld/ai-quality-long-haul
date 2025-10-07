from Agent.agent2 import APITestPlanWithExamples
from C02_Unit_Tests.common import VALID_FAKE_KEY
from config import GEMINI_API_KEY


class TestJsonValidation:
    def setup_method(self):
        self.agent = APITestPlanWithExamples(api_key=VALID_FAKE_KEY, model_name=GEMINI_API_KEY)

    def test_validate_json_with_valid_payload(self):
        valid_payload = {
            "title": "Create new support ticket for user.",
            "priority": "High"
        }
        required_keys = ["title", "priority"]
        is_valid, error_message = self.agent.validate_json(valid_payload, required_keys)
        assert is_valid is True
        assert error_message is None

    def test_validate_json_with_missing_key(self):
        invalid_payload = {
            "title": "This payload is missing the priority."
        }
        required_keys = ["title", "priority"]
        is_valid, error_message = self.agent.validate_json(invalid_payload, required_keys)
        assert is_valid is False
        assert error_message == "Missing required keys: priority"

    def test_validate_json_with_invalid_type(self):
        invalid_payload = "just a string"
        is_valid, error_message = self.agent.validate_json(invalid_payload)
        assert is_valid is False
        assert error_message == "Payload is not a valid JSON object."
