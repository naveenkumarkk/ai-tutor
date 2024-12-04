import requests

url = "https://tu-openai-api-management.azure-api.net/nail-projects/openai/deployments/gpt-4o-nail/chat/completions"
querystring = {"api-version": "2024-08-01-preview"}

def get_chatgpt_response(user_message, conversation_type):
    try:
        # Dynamically adjust the system content based on the conversation type
        if conversation_type == "planning":
            system_content = (
                "You are an AI tutor helping students create detailed study plans. Your primary focus is on setting goals, "
                "prioritizing tasks, and distributing study sessions effectively across available time."
            )
        elif conversation_type == "reflection":
            system_content = (
                "You are an AI tutor guiding students through self-reflection. Help them analyze their performance, identify "
                "areas of improvement, and provide constructive feedback for better outcomes in future tasks."
            )
        elif conversation_type == "monitoring":
            system_content = (
                "You are an AI tutor helping students monitor their progress. Provide updates on their tasks, highlight missed deadlines, "
                "and suggest modifications to stay on track with their study goals."
            )
        else:
            # Default message in case of an unrecognized conversation type
            system_content = (
                "You are an AI tutor designed to help students with Self-Regulated Learning (SRL). Assist them with planning, "
                "execution, monitoring, and reflecting on their study activities."
            )

        payload = {
            "messages": [
                {"role": "system", "content": system_content},
                {"role": "user", "content": user_message},
            ],
            "max_tokens": 200,
            "temperature": 0.3,
        }

        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Insomnia/2023.5.6",
            "api-key": "8c5567ebd69347cc8092ea4c55efeec9",
        }

        # Make the POST request
        response = requests.post(url, json=payload, headers=headers, params=querystring)
        response.raise_for_status()

        # Extract the assistant's reply
        assistant_reply = response.json().get("choices", [{}])[0].get("message", {}).get("content", "")
        return assistant_reply
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error with OpenAI API: {str(e)}")

# Example usage
if __name__ == "__main__":
    user_message = "Can you help me create a study plan for my exams?"
    conversation_type = "planning"  # Choose from "planning", "reflection", "monitoring"
    reply = get_chatgpt_response(user_message, conversation_type)
    print("ChatGPT Reply:", reply)
