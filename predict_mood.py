# import pywhatkit as kit
# import joblib
# import numpy as np
# import pandas as pd
# from train_model import model  # Import the trained model
#
# # Define feature names (same as used in training)
# feature_names = ['danceability', 'energy', 'valence', 'tempo', 'speechiness', 'acousticness']
#
# # Define a sample song's features (you can modify these values to test with other songs)
# song_features = np.array([[0.7, 0.8, 0.6, 120, 0.02, 0.3]])
#
# # Convert to DataFrame to match the format the model was trained on
# song_features_df = pd.DataFrame(song_features, columns=feature_names)
#
# # Predict genre/mood
# mood = model.predict(song_features_df)[0]
# print(f"Predicted Mood: {mood}")
#
# # Mood-based song recommendations
# mood_songs = {
#     0: "Happy songs playlist",
#     1: "Sad songs playlist",
#     2: "Energetic workout music",
#     3: "Calm relaxing tunes"
# }
#
# def play_song(mood):
#     query = mood_songs.get(mood, "Top trending songs")
#     kit.playonyt(query)  # Plays YouTube song
#
# # Play song based on mood
# play_song(mood)

import pywhatkit as kit
import joblib
import numpy as np
import pandas as pd
from train_model import model  # Import the trained model

# Define feature names (same as used in training)
feature_names = ['danceability', 'energy', 'valence', 'tempo', 'speechiness', 'acousticness']

def get_user_input():
    # Prompt the user for input values for each feature
    print("Please enter the following features for the song:")

    danceability = float(input("Danceability (0-1): "))
    energy = float(input("Energy (0-1): "))
    valence = float(input("Valence (0-1): "))
    tempo = float(input("Tempo (BPM): "))
    speechiness = float(input("Speechiness (0-1): "))
    acousticness = float(input("Acousticness (0-1): "))

    # Return the input values as a numpy array
    return np.array([[danceability, energy, valence, tempo, speechiness, acousticness]])

# Get the song features from the user
song_features = get_user_input()

# Convert to DataFrame to match the format the model was trained on
song_features_df = pd.DataFrame(song_features, columns=feature_names)

# Predict genre/mood
mood_number = model.predict(song_features_df)[0]
print(f"Predicted Mood Number: {mood_number}")

# Mood-based song recommendations (mood names mapped to mood numbers)
mood_songs = {
    0: "Happy songs playlist",
    1: "Sad songs playlist",
    2: "Energetic workout music",
    3: "Calm relaxing tunes",
    4: "Romantic love songs",
    5: "Calm instrumental vibes",
    6: "Exciting party tracks",
    7: "Chill background music",
    8: "Melancholy ballads",
    9: "Upbeat dance hits",
    10: "Groovy funk jams",
    11: "Dark atmospheric tunes",
    12: "Dreamy ambient tracks",
    13: "Hopeful inspirational music",
    14: "Funky beats",
    15: "Intense cinematic soundtracks",
    16: "Lively energetic beats",
    17: "Euphoric anthems",
    18: "Mystical soundscapes",
    19: "Pensive introspective music",
    20: "Warm acoustic melodies",
    21: "Whimsical quirky tunes",
    22: "Peaceful nature sounds",
    23: "Tense thriller soundtracks",
    24: "Motivational workout music",
    25: "Mysterious suspenseful tracks",
    26: "Nostalgic retro vibes",
    27: "Serene calm soundtracks",
    28: "Sentimental love songs",
    29: "Powerful epic music",
    30: "Cinematic movie scores",
    31: "Dramatic orchestral pieces",
    32: "Aggressive rock anthems",
    33: "Ethereal ambient sounds",
    34: "Soft lullabies",
    35: "Playful kids music",
    36: "Quirky indie tracks",
    37: "Angry heavy metal",
    38: "Emotional ballads",
    39: "Cheerful pop hits",
    40: "Romantic chill beats",
    41: "Passionate love songs",
    42: "Classical elegance",
    43: "Jazz lounge vibes",
    44: "Trippy psychedelic music",
    45: "Sultry smooth jazz",
    46: "Blissful meditation music",
    47: "Wistful acoustic tunes",
    48: "Exotic world music",
    49: "Hyped party anthems",
    50: "Glitchy electronic beats",
    51: "Sci-Fi futuristic sounds",
    52: "Futuristic chill music",
    53: "Vintage rock classics",
    54: "Raw underground sounds",
    55: "Soulful R&B tracks",
    56: "Lo-Fi chill beats",
    57: "Majestic orchestral music",
    58: "Rebellious punk rock",
    59: "Cyberpunk techno beats",
    60: "Steampunk industrial music",
    61: "Melodic classical pieces",
    62: "Grunge rock hits",
    63: "Grotesque darkwave",
    64: "Haunting eerie tracks",
    65: "Anthemic stadium rock",
    66: "Lush orchestral arrangements",
    67: "Darkwave synth music",
    68: "New Wave pop hits",
    69: "Gothic dark ambient",
    70: "Industrial techno beats",
    71: "Psychedelic rock vibes",
    72: "Epic soundtracks",
    73: "Enigmatic mysterious music",
    74: "Harmonic melodic tracks",
    75: "Smooth jazz vibes",
    76: "Creepy horror soundtracks",
    77: "Foreboding ominous music",
    78: "Minimalist electronic",
    79: "Abstract experimental sounds",
    80: "Crisp acoustic guitar",
    81: "Dizzying electronic music",
    82: "Majestic jazz ballads",
    83: "Brooding atmospheric music",
    84: "Glorious orchestral anthems",
    85: "Heavy metal riffs",
    86: "Deep bass music",
    87: "Urban hip hop tracks",
    88: "Spiritual meditative music",
    89: "Tranquil ambient sounds",
    90: "Minimal electronic music",
    91: "Punchy techno beats",
    92: "Explosive rock solos",
    93: "Otherworldly ambient music",
    94: "Glistening pop hits",
    95: "Bouncy dance music",
    96: "Eccentric indie music",
    97: "Choral classical pieces",
    98: "Apocalyptic movie scores",
    99: "Cheesy 80s hits",
    100: "Old School hip hop",
    101: "Boom Bap rap",
    102: "R&B Groove hits",
    103: "Electronic Bliss",
    104: "Celtic folk tunes",
    105: "Folk Vibes acoustic",
    106: "Country Swing",
    107: "Bluegrass",
    108: "Tropical summer vibes",
    109: "Salsa Heat",
    110: "Reggae Roots",
    111: "Afrobeat Groove",
    112: "Flamenco Passion",
    113: "Bollywood Beats"
}

# Get the mood name using the predicted mood number
mood_name = mood_songs.get(mood_number, "Top trending songs")
print(f"Predicted Mood: {mood_name}")

# Play song based on mood name
kit.playonyt(mood_name)
