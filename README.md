# MyOwnChatGPT!

## Simple application to demonstrate the use of OpenAI APIs with GPT3.5 Turbo model - for a particular use case

###  Use case: Answer user provided question with the help of OpenAI's Completion API

#### Software stack used

- HTML
- Javascript
- Python with OpenAI and Flask
- Azure Webapp to deploy Python app or this app can be run locally


##### How it works

app.py listens on port 5000 and it has decorators for / and /ask routes. 
app.py serves HTML/JS at / path.   
app.py addresses POST call at /ask path.


