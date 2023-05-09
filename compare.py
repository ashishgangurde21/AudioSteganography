import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

# import tkinter as tk
# import tkinter.filedialog as fd
# import matplotlib.pyplot as plt
# import numpy as np
# import librosa

# # Function to load audio file and calculate its spectrogram
# def load_audio(file_path):
#     data, rate = librosa.load(file_path)
#     spec, _, _, _ = plt.specgram(data, Fs=rate, NFFT=1024, noverlap=900)
#     return spec

# # Function to compare two spectrograms and highlight differences
# def compare_spectrograms(spec1, spec2):
#     # Calculate difference between spectrograms
#     diff_spec = np.abs(spec1) - np.abs(spec2)
#     # Set threshold for highlighting differences
#     threshold = np.max(diff_spec) * 0.1
#     # Create colormap for highlighting differences
#     cmap = plt.get_cmap('cool')
#     # Plot spectrograms with differences highlighted
#     plt.subplot(2,1,1)
#     plt.imshow(spec1, cmap='hot', aspect='auto')
#     plt.title('Spectrogram 1')
#     plt.subplot(2,1,2)
#     plt.imshow(spec2, cmap='hot', aspect='auto')
#     plt.title('Spectrogram 2')
#     for i in range(diff_spec.shape[1]):
#         for j in range(diff_spec.shape[0]):
#             if diff_spec[j,i] > threshold:
#                 plt.subplot(2,1,1)
#                 plt.plot(i, j, 's', markersize=5, color=cmap(diff_spec[j,i]))
#                 plt.subplot(2,1,2)
#                 plt.plot(i, j, 's', markersize=5, color=cmap(diff_spec[j,i]))
#     plt.show()

# # Function to handle button click event
# def browse_files():
#     # Open file dialog to select first audio file
#     file1_path = fd.askopenfilename(title="Select first audio file", filetypes=[("Audio Files", ".wav")])
#     # Check if file was selected
#     if file1_path:
#         # Load spectrogram for first audio file
#         spec1 = load_audio(file1_path)
#         # Open file dialog to select second audio file
#         file2_path = fd.askopenfilename(title="Select second audio file", filetypes=[("Audio Files", ".wav")])
#         # Check if file was selected
#         if file2_path:
#             # Load spectrogram for second audio file
#             spec2 = load_audio(file2_path)
#             # Compare spectrograms and highlight differences
#             compare_spectrograms(spec1, spec2)

# # Create main window
# root = tk.Tk()
# root.title("Audio Difference Viewer")

# # Create button to browse for audio files
# browse_button = tk.Button(root, text="Browse", command=browse_files)
# browse_button.pack()

# # Start GUI
# root.mainloop()


# Load the original and modified audio signals
original_audio, sr = librosa.load('trial.wav', sr=None)
modified_audio, sr = librosa.load('encoded.wav', sr=None)

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


