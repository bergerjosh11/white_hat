from AI_model import AIModel
import requests

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <url>")
        sys.exit(1)

    target_url = sys.argv[1]

    model_path = "path/to/your/model"  # Path to your AI model
    ai_model = AIModel(model_path)

    response = requests.get(target_url)
    content = response.content

    detected_vulnerabilities = ai_model.detect_vulnerabilities(content)

    print("Detected vulnerabilities:")
    for vulnerability in detected_vulnerabilities:
        print(vulnerability)

if __name__ == "__main__":
    main()
