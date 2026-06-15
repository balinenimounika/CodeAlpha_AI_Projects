# 🎵 AI Music Generation using PyTorch

## 📌 Project Overview

This project is an AI-powered Music Generation System that learns musical patterns from MIDI files and generates new melodies using a Deep Learning LSTM (Long Short-Term Memory) network built with PyTorch.

The model is trained on a collection of classical piano MIDI files and predicts the next note in a sequence, enabling the creation of entirely new musical compositions.

## 🚀 Features

* MIDI file preprocessing using Music21
* Deep Learning-based Music Generation
* LSTM Neural Network implemented with PyTorch
* Automatic note sequence extraction
* Generates new MIDI music files
* Supports multiple classical piano MIDI datasets
* Beginner-friendly and easy to extend

## 🛠️ Technologies Used

* Python
* PyTorch
* Music21
* NumPy
* Pretty MIDI
* Matplotlib

## 📂 Project Structure

Task3_MusicGeneration/

├── data/

│ ├── midi_files/

│ └── notes.pkl

├── generated_music/

│ └── output.mid

├── models/

│ └── music_model.pth

├── src/

│ ├── preprocess.py

│ ├── train.py

│ └── generate.py

├── main.py

├── requirements.txt

└── README.md

## 📊 Workflow

### 1. Data Collection

Collect MIDI files containing piano or classical music compositions.

### 2. Data Preprocessing

Extract notes and chords from MIDI files and convert them into sequences suitable for training.

### 3. Model Training

Train an LSTM neural network to learn musical patterns and note relationships.

### 4. Music Generation

Generate new note sequences using the trained model and convert them into a MIDI file.

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/Task3_MusicGeneration.git
cd Task3_MusicGeneration
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Usage

### Preprocess MIDI Files

```bash
python src/preprocess.py
```

### Train Model

```bash
python src/train.py
```

### Generate Music

```bash
python src/generate.py
```

Generated music will be saved inside:

```text
generated_music/
```

## 📈 Results

* Successfully extracted musical notes from MIDI datasets.
* Trained an LSTM-based music generation model.
* Generated new AI-composed MIDI melodies.
* Demonstrated sequence prediction using Deep Learning.

## 🎯 Future Enhancements

* Transformer-based Music Generation
* Genre-specific music generation
* Web interface using Streamlit
* MIDI-to-WAV conversion
* Real-time music playback
* Attention-based architectures


## 🏆 Internship Project

This project was developed as part of the **Code Alpha AI Internship Program**, demonstrating the application of Deep Learning and Artificial Intelligence in creative music generation.
