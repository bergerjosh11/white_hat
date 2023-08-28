import subprocess
from AI_model import AIModel
import requests

def run_security_test(url, ai_model):
    response = requests.get(url)
    content = response.content

    # Use the AI model to detect vulnerabilities
    detected_vulnerabilities = ai_model.detect_vulnerabilities(content)

    return detected_vulnerabilities

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python security_test.py <url>")
        sys.exit(1)

    target_url = sys.argv[1]

    # Initialize the AI model
    ai_model = AIModel()

    # Run security test using subprocess
    run_security_test(target_url, ai_model)
