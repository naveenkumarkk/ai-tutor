# chatgpt_controller.py
from flask import Blueprint,jsonify, request,render_template,session
from models import User
from services.conversation_service import get_or_create_conversation, save_user_message, save_assistant_message
from services.chatgpt_service import get_chatgpt_response
from utils import login_required 

chatgpt_bp = Blueprint('chatgpt_bp', __name__)

@chatgpt_bp.route('/chat', methods=['POST'])
@login_required
def chat_with_gpt():
    """Process the chat with ChatGPT."""
    data = request.json
    user_id = session.get('user_id')
    conversation_type = data.get('conversation_type')
    user_message = data.get('message')

    # Check if user exists
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    # Retrieve or create a new conversation
    conversation = get_or_create_conversation(user_id,conversation_type)

    # Save user's message in the database
    save_user_message(conversation.conversation_id, user_id, user_message)

    # Get response from ChatGPT
    try:
        assistant_reply = get_chatgpt_response(user_message)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    # Save the assistant's response in the database
    save_assistant_message(conversation.conversation_id, user_id, assistant_reply)

    # Return the assistant's reply to the user
    return jsonify({'reply': assistant_reply})

@chatgpt_bp.route("/chatscreen")
@login_required
def chatscreen():
    return render_template("main.html")

@chatgpt_bp.route("/tips")
@login_required
def tipsscreen():
    return render_template("tips.html")

@chatgpt_bp.route("/help")
@login_required
def helpscreen():
    return render_template("help.html")