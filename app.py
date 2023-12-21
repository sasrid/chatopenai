from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Replace 'YOUR_OPENAI_API_KEY' with your OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['GET'])
def ask():
    question = request.args.get('question')
    token_limit = int(request.args.get('token_limit'))

    # Define the OpenAI prompt
    prompt = f"User: {question}\nChatbot:"

    # Generate a response from the chatbot
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=token_limit
    )

    # Extract the chatbot's reply from the response
    chatbot_reply = response.choices[0].text.strip()

    return chatbot_reply

if __name__ == '__main__':
    app.run(debug=True)
