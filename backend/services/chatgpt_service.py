# chatgpt_service.py

import openai

# Set up OpenAI API key (you could also move this to a config file or environment variable)
openai.api_key = 'your_openai_api_key'

def get_chatgpt_response(prompt):
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a study assistant."}, {"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']
