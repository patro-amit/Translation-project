
from flask import Flask, render_template
import os
from indic_translation.api import register_indic_translate_api

app = Flask(__name__)

# Set up environment variables
app.config['MODELS_DIR'] = os.environ.get('MODELS_DIR', './models')

# Register the translation API blueprint
register_indic_translate_api(app)

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# Add a dedicated translation page
@app.route('/translate')
def translate_page():
    return render_template('translate.html')

if __name__ == '__main__':
    # Create models directory if it doesn't exist
    os.makedirs(app.config['MODELS_DIR'], exist_ok=True)
    app.run(debug=True)
