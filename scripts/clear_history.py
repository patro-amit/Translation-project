# filepath: /Users/shyampatro/Translation project/clear_history.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app
from models import db, TranslationLog

with app.app_context():
    TranslationLog.query.delete()
    db.session.commit()
    print("All translation history deleted.")