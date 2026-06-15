import pickle
import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

SEQUENCE_LENGTH = 50
BATCH_SIZE = 64
EPOCHS = 30
HIDDEN_SIZE = 256

# Load notes
with open("data/notes.pkl", "rb") as f:
    notes = pickle.load(f)

pitchnames = sorted(set(notes))

note_to_int = {
    note: number
    for number, note in enumerate(pitchnames)
}

network_input = []
network_output = []

for i in range(len(notes) - SEQUENCE_LENGTH):

    seq_in = notes[i:i + SEQUENCE_LENGTH]
    seq_out = notes[i + SEQUENCE_LENGTH]

    network_input.append(
        [note_to_int[n] for n in seq_in]
    )

    network_output.append(
        note_to_int[seq_out]
    )

X = np.array(network_input)
y = np.array(network_output)

VOCAB_SIZE = len(pitchnames)

class MusicDataset(Dataset):
    def __init__(self, X, y):
        self.X = torch.tensor(X, dtype=torch.long)
        self.y = torch.tensor(y, dtype=torch.long)

    def __len__(self):
        return len(self.X)

    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]

dataset = MusicDataset(X, y)
loader = DataLoader(dataset,
                    batch_size=BATCH_SIZE,
                    shuffle=True)

class MusicLSTM(nn.Module):

    def __init__(self, vocab_size):

        super().__init__()

        self.embedding = nn.Embedding(
            vocab_size,
            128
        )

        self.lstm = nn.LSTM(
            128,
            HIDDEN_SIZE,
            num_layers=2,
            batch_first=True
        )

        self.fc = nn.Linear(
            HIDDEN_SIZE,
            vocab_size
        )

    def forward(self, x):

        x = self.embedding(x)

        out, _ = self.lstm(x)

        out = self.fc(out[:, -1, :])

        return out

model = MusicLSTM(VOCAB_SIZE)

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.001
)

print("Training Started...")

for epoch in range(EPOCHS):

    total_loss = 0

    for X_batch, y_batch in loader:

        optimizer.zero_grad()

        output = model(X_batch)

        loss = criterion(output, y_batch)

        loss.backward()

        optimizer.step()

        total_loss += loss.item()

    print(
        f"Epoch {epoch+1}/{EPOCHS} "
        f"Loss: {total_loss:.4f}"
    )

torch.save(
    {
        "model_state_dict":
        model.state_dict(),

        "note_to_int":
        note_to_int,

        "pitchnames":
        pitchnames
    },

    "models/music_model.pth"
)

print("Model Saved!")