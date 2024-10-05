import torch
import torchaudio
device = ('cuda' if torch.cuda.is_available() else 'cpu')
print(device)
print(torchaudio.__version__)
