# chatgpt_controller.py

from flask import jsonify, request
from models import User
from services.conversation_service import get_or_create_conversation, save_user_message, save_assistant_message
from services.chatgpt_service import get_chatgpt_response
from services.zapier_service import send_to_zapier  # Import Zapier service
from services.google_calendar_service import create_google_calendar_event  # Import Google Calendar service

def chat_with_gpt():
    """Process the chat with ChatGPT."""
    data = request.json
    user_id = data.get('user_id')
    user_message = data.get('message')

    # Check if user exists
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    # Retrieve or create a new conversation
    conversation = get_or_create_conversation(user_id)

    # Save user's message in the database
    save_user_message(conversation.conversation_id, user_id, user_message)

    # Get response from ChatGPT
    try:
        assistant_reply = get_chatgpt_response(user_message)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    # Save the assistant's response in the database
    save_assistant_message(conversation.conversation_id, user_id, assistant_reply)

    # Example: Send data to Zapier if the assistant suggests a task
    if "task" in assistant_reply.lower():
        send_to_zapier({'user_id': user_id, 'message': user_message, 'reply': assistant_reply})

    # Example: Create a Google Calendar event (assuming user has a Google token)
    if user.google_token and "schedule" in assistant_reply.lower():
        event_data = {
            'summary': 'New Task from AI Assistant',
            'description': assistant_reply,
            'start': {'dateTime': '2024-11-01T09:00:00-07:00', 'timeZone': 'America/Los_Angeles'},
            'end': {'dateTime': '2024-11-01T10:00:00-07:00', 'timeZone': 'America/Los_Angeles'},
        }
        create_google_calendar_event(user.google_token, event_data)

    # Return the assistant's reply to the user
    return jsonify({'reply': assistant_reply})
