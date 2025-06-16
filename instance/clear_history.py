# filepath: /Users/shyampatro/Translation project/clear_history.py
from app import app
from models import db, TranslationLog

with app.app_context():
    TranslationLog.query.delete()
    db.session.commit()
    print("All translation history deleted.")