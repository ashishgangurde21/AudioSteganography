import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

# Load the original and modified audio signals
original_audio, sr = librosa.load('trial.wav', sr=None)
modified_audio, sr = librosa.load('Phase_encoded.wav', sr=None)

# Compute the spectrograms of both signals
spec_orig = librosa.stft(original_audio)
spec_mod = librosa.stft(modified_audio)

# Convert the spectrograms to decibels (dB)
spec_orig_db = librosa.amplitude_to_db(abs(spec_orig))
spec_mod_db = librosa.amplitude_to_db(abs(spec_mod))

# Compute the difference spectrogram
spec_diff_db = spec_mod_db - spec_orig_db

# Define the color map for the spectrograms
cmap = plt.get_cmap('coolwarm')

# Plot the original and modified spectrograms
plt.figure(figsize=(12, 8))
plt.subplot(3, 1, 1)
librosa.display.specshow(spec_orig_db, sr=sr, x_axis='time', y_axis='log', cmap=cmap)
plt.title('Original Audio Spectrogram')
plt.colorbar(format='%+2.0f dB')

plt.subplot(3, 1, 2)
librosa.display.specshow(spec_mod_db, sr=sr, x_axis='time', y_axis='log', cmap=cmap)
plt.title('Modified Audio Spectrogram')
plt.colorbar(format='%+2.0f dB')

# Plot the difference spectrogram
plt.subplot(3, 1, 3)
librosa.display.specshow(spec_diff_db, sr=sr, x_axis='time', y_axis='log', cmap=cmap)
plt.title('Difference Spectrogram')
plt.colorbar(format='%+2.0f dB')

# Show the plots
plt.tight_layout()
plt.show()
