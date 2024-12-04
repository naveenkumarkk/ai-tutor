from models import db, User, Conversation, Message
from datetime import datetime

def get_or_create_conversation(user_id,conversation_type):
    """Retrieve an ongoing conversation or create a new one."""
    conversation = Conversation.query.filter_by(user_id=user_id, status='ongoing',conversation_type = conversation_type).first()
    if not conversation:
        conversation = Conversation(user_id=user_id,conversation_type = conversation_type)
        db.session.add(conversation)
        db.session.commit()
    return conversation

def retrieve_user_ongoing_history_and_pair(user_id, conversation_id):
    return (
        Message.query.filter_by(user_id=user_id, conversation_id=conversation_id)
        .order_by(Message.created_at)
        .all()
    )

def save_user_message(conversation_id, user_id, user_message):
    """Save a user's message in the database."""
    user_msg = Message(
        conversation_id=conversation_id,
        user_id=user_id,
        role='user',
        content=user_message,
        created_at=datetime.utcnow()
    )
    db.session.add(user_msg)
    db.session.commit()

def save_assistant_message(conversation_id, user_id, assistant_reply):
    """Save the assistant's reply in the database."""
    assistant_msg = Message(
        conversation_id=conversation_id,
        user_id=user_id,
        role='assistant',
        content=assistant_reply,
        created_at=datetime.utcnow()
    )
    db.session.add(assistant_msg)
    db.session.commit()
