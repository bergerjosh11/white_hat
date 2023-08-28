#!/usr/bin/env python
# main.py
from AI_model import AIModel
import requests
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <url>")
        sys.exit(1)

    target_url = sys.argv[1]

    model_path = "path/to/your/trained_model.h5"  # Path to your trained AI model
    ai_model = AIModel(model_path)

    try:
        response = requests.get(target_url)
        if response.status_code == 200:
            content = response.content
            detected_vulnerabilities = ai_model.detect_vulnerabilities(content)

            if detected_vulnerabilities:
                print("Detected vulnerabilities:")
                for vulnerability in detected_vulnerabilities:
                    print(vulnerability)
            else:
                print("No vulnerabilities detected.")
        else:
            print("Failed to fetch URL:", response.status_code)

    except requests.exceptions.RequestException as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
