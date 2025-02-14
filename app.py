from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model
model = joblib.load("mood_classifier.pkl")

# Homepage route to render the form
@app.route('/')
def index():
    return '''
    <html>
        <head>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f0f4f8;
                    margin: 0;
                    padding: 0;
                }
                h1 {
                    text-align: center;
                    color: #333;
                }
                .container {
                    width: 50%;
                    margin: 0 auto;
                    background-color: #fff;
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                }
                form {
                    display: flex;
                    flex-direction: column;
                    gap: 15px;
                }
                label {
                    font-size: 16px;
                    font-weight: bold;
                }
                input[type="number"] {
                    padding: 8px;
                    font-size: 14px;
                    border: 1px solid #ccc;
                    border-radius: 4px;
                }
                button {
                    padding: 10px;
                    background-color: #4CAF50;
                    color: white;
                    border: none;
                    border-radius: 4px;
                    cursor: pointer;
                    font-size: 16px;
                }
                button:hover {
                    background-color: #45a049;
                }
                a {
                    display: block;
                    text-align: center;
                    margin-top: 20px;
                    color: #007BFF;
                    text-decoration: none;
                }
                a:hover {
                    text-decoration: underline;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Predict Song Mood</h1>
                <form action="/predict" method="POST">
                    <label for="danceability">Danceability (0-1):</label>
                    <input type="number" name="danceability" step="0.01" min="0" max="1" required>

                    <label for="energy">Energy (0-1):</label>
                    <input type="number" name="energy" step="0.01" min="0" max="1" required>

                    <label for="valence">Valence (0-1):</label>
                    <input type="number" name="valence" step="0.01" min="0" max="1" required>

                    <label for="tempo">Tempo (BPM):</label>
                    <input type="number" name="tempo" required>

                    <label for="speechiness">Speechiness (0-1):</label>
                    <input type="number" name="speechiness" step="0.01" min="0" max="1" required>

                    <label for="acousticness">Acousticness (0-1):</label>
                    <input type="number" name="acousticness" step="0.01" min="0" max="1" required>

                    <button type="submit">Predict Mood</button>
                </form>
            </div>
        </body>
    </html>
    '''

# Define 114 mood labels (Replace these with actual mood names)
mood_map = {
    0: "Happy", 1: "Sad", 2: "Energetic", 3: "Relaxing", 4: "Romantic", 5: "Calm",
    6: "Exciting", 7: "Chill", 8: "Melancholy", 9: "Upbeat", 10: "Groovy", 11: "Dark",
    12: "Dreamy", 13: "Hopeful", 14: "Funky", 15: "Intense", 16: "Lively", 17: "Euphoric",
    18: "Mystical", 19: "Pensive", 20: "Warm", 21: "Whimsical", 22: "Peaceful",
    23: "Tense", 24: "Motivational", 25: "Mysterious", 26: "Nostalgic", 27: "Serene",
    28: "Sentimental", 29: "Powerful", 30: "Cinematic", 31: "Dramatic", 32: "Aggressive",
    33: "Ethereal", 34: "Soft", 35: "Playful", 36: "Quirky", 37: "Angry", 38: "Emotional",
    39: "Cheerful", 40: "Romantic Chill", 41: "Passionate", 42: "Classical Elegance",
    43: "Jazz Lounge", 44: "Trippy", 45: "Sultry", 46: "Blissful", 47: "Wistful",
    48: "Exotic", 49: "Hyped", 50: "Glitchy", 51: "Sci-Fi", 52: "Futuristic",
    53: "Vintage", 54: "Raw", 55: "Soulful", 56: "Lo-Fi", 57: "Majestic", 58: "Rebellious",
    59: "Cyberpunk", 60: "Steampunk", 61: "Melodic", 62: "Grunge", 63: "Grotesque",
    64: "Haunting", 65: "Anthemic", 66: "Lush", 67: "Darkwave", 68: "New Wave",
    69: "Gothic", 70: "Industrial", 71: "Psychedelic", 72: "Epic", 73: "Enigmatic",
    74: "Harmonic", 75: "Smooth", 76: "Creepy", 77: "Foreboding", 78: "Minimalist",
    79: "Abstract", 80: "Crisp", 81: "Dizzying", 82: "Majestic Jazz", 83: "Brooding",
    84: "Glorious", 85: "Heavy", 86: "Deep", 87: "Urban", 88: "Spiritual",
    89: "Tranquil", 90: "Minimal", 91: "Punchy", 92: "Explosive", 93: "Otherworldly",
    94: "Glistening", 95: "Bouncy", 96: "Eccentric", 97: "Choral", 98: "Apocalyptic",
    99: "Cheesy", 100: "Old School", 101: "Boom Bap", 102: "R&B Groove", 103: "Electronic Bliss",
    104: "Celtic", 105: "Folk Vibes", 106: "Country Swing", 107: "Bluegrass",
    108: "Tropical", 109: "Salsa Heat", 110: "Reggae Roots", 111: "Afrobeat Groove",
    112: "Flamenco Passion", 113: "Bollywood Beats"
}

@app.route('/predict', methods=['POST'])
def predict():
    # Get input features from the form
    try:
        danceability = float(request.form['danceability'])
        energy = float(request.form['energy'])
        valence = float(request.form['valence'])
        tempo = float(request.form['tempo'])
        speechiness = float(request.form['speechiness'])
        acousticness = float(request.form['acousticness'])

        # Prepare features for prediction
        song_features = np.array([[danceability, energy, valence, tempo, speechiness, acousticness]])

        # Predict the mood/genre
        mood = model.predict(song_features)[0]  # Get predicted class index
        predicted_mood = mood_map.get(mood, f"Unknown Mood ({mood})")  # Handle unknown moods

        print(f"Predicted Mood: {predicted_mood}")  # Debugging

        # Return the prediction result with styling
        return f'''
        <html>
            <head>
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        background-color: #f0f4f8;
                        margin:0;
                        padding: 0;
                    }}
                    
                    .container {{
                
                        margin: 50px auto; /* Add margin-top here to create space from the top */
                        background-color: #fff;
                        padding: 20px;
                        border-radius: 8px;
                        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }}
    
                    h1 {{
                        text-align: center;
                        color: #333;
                    }}
                    .result-container {{
                        width: 50%;
                        margin: 50px auto;
                        background-color: #fff;
                        padding: 20px;
                        border-radius: 8px;
                        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                        text-align: center;
                    }}
                    a {{
                        display: block;
                        text-align: center;
                        margin-top: 20px;
                        color: #007BFF;
                        text-decoration: none;
                    }}
                    a:hover {{
                        text-decoration: underline;
                    }}
                </style>
            </head>
            <body>
                <div class="result-container">
                    <h1>Your Song Mood: {predicted_mood}</h1>
                    <a href="/">Try again</a>
                </div>
            </body>
        </html>
        '''
    except Exception as e:
        return f'<h1>Error: {str(e)}</h1> <a href="/">Try again</a>'


if __name__ == '__main__':
    app.run(debug=True)
