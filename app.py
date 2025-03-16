import os
from dotenv import load_dotenv
from api import create_app

load_dotenv()

# Create the Flask application
app = create_app()

if __name__ == "__main__":
    debug_mode = os.getenv('FLASK_DEBUG', 'True') == 'True'
    app.run(debug=debug_mode, port=9890)

