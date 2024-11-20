# chatgpt_service.py

import openai

# Set up OpenAI API key (you could also move this to a config file or environment variable)
openai.api_key = 'TODO'

def get_chatgpt_response(prompt):
    response = openai.Completion.create(
        model="gpt-4o-nail",
        messages=[{"role": "system", "content": "You are a study assistant."}, {"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']
