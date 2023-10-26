from payload_validator_interface import PayloadValidatorInterface
from abc import abstractmethod

#The detector does not perform any sanitization
class AbstractXssDetector(PayloadValidatorInterface):
    def sanitize_payload(self, payload: str) -> str:
        return str
    
    @abstractmethod
    def detect_valid_payload(self, payload: str) -> bool:
        return super().detect_valid_payload(payload)