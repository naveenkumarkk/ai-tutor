from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy
db = SQLAlchemy()

# User model to store user information
class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name=db.Column(db.String(240),nullable=False)
    last_name=db.Column(db.String(240),nullable=False)
    dob=db.Column(db.Date,nullable=False)
    sex = db.Column(db.Enum('male', 'female', 'not-preferred', name='sex'), default='not-preferred')
    nationality=db.Column(db.String(120),nullable=False)
    occupation=db.Column(db.String(120),nullable=True)
    organisation=db.Column(db.String(120),nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    google_token = db.Column(db.Text, nullable=True)  # Google OAuth token
    microsoft_token = db.Column(db.Text, nullable=True)  # Microsoft OAuth token
    last_login=db.Column(db.DateTime,nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationship: One user can have many conversations
    conversations = db.relationship('Conversation', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'


# Conversation model to track conversation sessions
class Conversation(db.Model):
    __tablename__ = 'conversations'
    conversation_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    started_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.Enum('ongoing', 'completed', 'paused', name='conversation_status'), default='ongoing')

    # Relationship: One conversation can have many messages
    messages = db.relationship('Message', backref='conversation', lazy=True)

    def __repr__(self):
        return f'<Conversation {self.conversation_id} for user {self.user_id}>'


# Message model to store each interaction in the conversation
class Message(db.Model):
    __tablename__ = 'messages'
    message_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    conversation_id = db.Column(db.Integer, db.ForeignKey('conversations.conversation_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    role = db.Column(db.Enum('user', 'assistant', name='message_role'), nullable=False) 
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Message {self.message_id} in conversation {self.conversation_id}>'

class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    subject = db.Column(db.String(120), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.Enum('completed', 'pending', name='status_enum'), default='pending')
    tasks = db.relationship('Task', backref='schedule', lazy=True)

# Task
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    schedule_id = db.Column(db.Integer, db.ForeignKey('schedule.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    due_date = db.Column(db.DateTime, nullable=False)
    completed = db.Column(db.Boolean, default=False)

class Grade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    subject = db.Column(db.String(120), nullable=False)
    score = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
class Feedback(db.Model):
    __tablename__ = 'feedback'
    feedback_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    message_id = db.Column(db.Integer, db.ForeignKey('messages.message_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    rating = db.Column(db.Integer, nullable=True) 
    comments = db.Column(db.Text, nullable=True) 
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Feedback {self.feedback_id} for message {self.message_id}>'
