import requests
import os

url = os.getenv('ENDPOINT_URL','https://tu-openai-api-management.azure-api.net/nail-projects/openai/deployments/gpt-4o-nail/chat/completions')
querystring = {"api-version": os.getenv('CHAT_GPT_API_VERSION','2024-08-01-preview')}

def get_chatgpt_response(user_message, conversation_type):
    try:
        # Detect if the user mentions finishing a phase
        if any(keyword in user_message.lower() for keyword in ["finished", "completed", "done"]):
            if conversation_type == "planning":
                return (
                    "Great job on completing your planning phase! Now, let's move on to the monitoring phase. "
                    "Good luck, and keep up the great work!"
                )
            elif conversation_type == "monitoring":
                return (
                    "Well done on completing your monitoring phase! Let's move on to the reflecting phase. "
                    "\nThe reflecting phase helps you analyze your actions and outcomes, ensuring continuous improvement. Keep it up!"
                )
            elif conversation_type == "reflection":
                return (
                    "Fantastic! You've completed the reflecting phase and learned from your experiences. "
                    "Now, it's time to apply these insights to your next plan. Start the planning phase again, "
                    "and let the AI tutor guide you in setting even better goals and strategies for success!"
                )

        # Dynamically adjust the system content based on the conversation type
        if conversation_type == "planning":
            system_content = (
                "You are an AI tutor designed to help students create and manage their study plans based on Self-Regulated Learning (SRL). "
                "Encourage students to create their own plans by setting goals, deadlines, and priorities. "
                "Use strategic planning techniques to ask questions like: "
                "'What is your task?', 'How complicated do you think it will be?', or 'What resources do you need?'. "
                "Avoid giving solutions or creating the plan for them. Instead, provide tips or reflective prompts to guide them. "
                "Ensure that students stay in control of their planning process. "
                "Once a plan is created, direct them to the monitoring phase."
            )
        elif conversation_type == "reflection":
            system_content = (
                "You are an AI tutor guiding students through self-reflection to improve their performance. "
                "Ask questions that analyze the connection between actions (causes) and outcomes (effects), such as: "
                "'Why do you think this approach worked?' or 'What could you have done differently?'. "
                "Help students identify potential pitfalls and generate strategies to avoid them in the future. "
                "Facilitate the creation of a cause-effect pattern, enabling students to learn from their experiences and improve."
            )
        elif conversation_type == "monitoring":
            system_content = (
                "You are an AI tutor helping students monitor their progress and stay motivated. "
                "Ask questions like: 'On which task are you currently working?' or 'How is your progress compared to your plan?'. "
                "Encourage students to assess if they are staying on track with their goals and timelines. "
                "Avoid discussing the specific content of tasks; focus on general progress and scheduling. "
                "If students are falling behind, suggest tips such as minimizing distractions or rescheduling. "
                "Once tasks are complete, direct students to the reflection phase."
            )
        else:
            # Default message in case of an unrecognized conversation type
            system_content = (
                "You are an AI tutor designed to help students with Self-Regulated Learning (SRL). "
                "Assist them with planning, execution, monitoring, and reflecting on their study activities."
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
            "api-key": os.getenv('CHAT_GPT_API_KEY', '8c5567ebd69347cc8092ea4c55efeec9'),
        }

        # Make the POST request
        response = requests.post(url, json=payload, headers=headers, params=querystring)
        response.raise_for_status()

        # Extract the assistant's reply
        assistant_reply = response.json().get("choices", [{}])[0].get("message", {}).get("content", "")
        return assistant_reply
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error with OpenAI API: {str(e)}")
