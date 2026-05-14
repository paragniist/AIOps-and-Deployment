import vertexai
from vertexai.preview.generative_models import GenerativeModel
from flask import Flask, request

vertexai.init(project="training-projects-43-430", location="us-central1")

parameters = {
    "temperature": 0.6,
    "max_output_tokens": 256,
    "top_k": 3,
    "top_p": 0.5
}

model = GenerativeModel("gemini-1.5-pro-002")

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
        model_response = model.generate_content(
        contents=request.get_json()['prompt'])
        return model_response.candidates[0].content.parts[0].text


if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0', debug=True)