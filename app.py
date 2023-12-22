from flask import Flask, render_template, request, jsonify

import os
import openai
from openai import OpenAI

app = Flask(__name__)

# Replace 'YOUR_OPENAI_API_KEY' with your OpenAI API key
#openai.api_key = 'YOUR_OPENAI_API_KEY'

client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY'],  # this is also the default, it can be omitted
)

@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/ask', methods=['POST'])
def ask_get():
    question = request.form.get('question')
    #question = "What is the capital of France?"
    # token_limit_str = request.args.get('token_limit', '50')
    # token_limit = int(token_limit_str)
    #token_limit = 50
    # Generate a response from the chatbot
    messages = [{"role": "user", "content": question}]
    response = openai.chat.completions.create(
        model= "gpt-3.5-turbo",
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
        max_tokens= 1024, # the maximum number of tokens to generate
    )
    #print(response)
    # Extract the chatbot's reply from the response
    chatbot_reply = response.choices[0].message.content

    return chatbot_reply

if __name__ == '__main__':
    app.run(debug=True)

