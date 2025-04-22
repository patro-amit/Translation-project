# models.py
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class TranslationLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    input_type = db.Column(db.String(20), nullable=False) # 'text', 'ocr', 'audio'
    source_language = db.Column(db.String(10), nullable=False) # e.g., 'en', 'hi'
    target_language = db.Column(db.String(10), nullable=False) # e.g., 'mr', 'ta', 'bn'
    original_text = db.Column(db.Text, nullable=True)
    translated_text = db.Column(db.Text, nullable=True)
    error_message = db.Column(db.Text, nullable=True) # Store errors if any

    def __repr__(self):
        return f'<TranslationLog {self.id}: {self.source_language} -> {self.target_language}>'