#!/usr/bin/env python
# main.py
from AI_model import AIModel
import requests
import sys
import os

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <url>")
        sys.exit(1)

    target_url = sys.argv[1]

    # Get the path of the directory where main.py is located
    script_directory = os.path.dirname(os.path.realpath(__file__))

    # Construct the path to the trained model file in the same directory
    model_path = os.path.join(script_directory, "trained_model.h5")

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
