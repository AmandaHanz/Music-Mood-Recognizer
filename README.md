Sure! Here’s the markdown version of your project description without the example code:

# Music Mood Recognizer 🎶💡

This project predicts the mood of a song based on its audio features, such as danceability, energy, valence, tempo, speechiness, and acousticness. It uses machine learning to classify the mood into predefined categories and provides mood-based music recommendations by playing YouTube playlists.

## Key Features ✨

- **Mood Prediction**: Input song features (e.g., danceability, energy) and predict the mood of the song.
- **Music Recommendations**: Based on the predicted mood, get a mood-specific playlist that is automatically played via YouTube.
- **Real-Time Playlists**: Integrates with `pywhatkit` to play mood-based music playlists on YouTube.
- **User-Friendly Interface**: Simple, interactive tool to input song features and get recommendations.

## Tech Stack 🛠️

- **Machine Learning**: 
  - Classification algorithms (Random Forest)
  - Trained using the [Spotify Tracks Dataset](https://www.kaggle.com/datasets)
- **Python**:
  - Data preprocessing with Pandas & NumPy
  - Model training using Scikit-Learn
- **YouTube Integration**: 
  - Play music via YouTube using `pywhatkit`
- **Deployment**: End-to-end solution for mood prediction and song recommendations ; used Flask.

## Setup Instructions 🚀

1. Clone this repository:
   ```bash
   git clone https://github.com/AmandaHanz/music-mood-recognizer.git
   ```
2. Install the necessary Python libraries
   

3. Download the model and dataset:
   - Download the Spotify Tracks Dataset from [Kaggle](https://www.kaggle.com/datasets) and place it in the project folder.
   - Train the model or use a pre-trained model provided in the repository.

5. Input song features when prompted and get mood-based music recommendations!

## Mood-Based Playlist Recommendations 🎧

- Happy songs playlist
- Sad songs playlist
- Energetic workout music
- Calm relaxing tunes
- Romantic love songs
- Upbeat dance hits
- Mysterious suspenseful tracks
- Intense cinematic soundtracks
- Peaceful nature sounds
- Darkwave synth music

## Model Development 💻

- **Data Collection & Preprocessing**: Utilized the Spotify Tracks Dataset from Kaggle to extract key audio features and preprocess the data for model training.
- **Model Development**: Applied classification algorithms (such as Random Forest) to predict mood labels based on the extracted features. Trained the model using a labeled dataset with various mood categories.
- **Mood Prediction**: Developed an interactive tool where users can input song features (such as danceability, energy, etc.) and receive a mood prediction for the song.
- **Music Recommendation**: Integrated the system with YouTube to play mood-based song playlists using `pywhatkit` library, enabling users to listen to recommended songs in real time.
- **Deployment**: Built an end-to-end solution that allows users to input song features, predicts the mood, and provides a direct music link based on the prediction.
