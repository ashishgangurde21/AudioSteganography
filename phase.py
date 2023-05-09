import numpy as np
import scipy.io.wavfile as wavfile
import librosa

import numpy as np

def encode_phase(audio_file, message):
    data, rate = librosa.load(audio_file, sr=None, mono=True)
    
    # Convert message to bytes and then to numpy array of floats
    encoded_message = message.encode('utf-8')
    encoded_message = np.frombuffer(encoded_message, dtype=np.uint8)
    encoded_message = np.unpackbits(encoded_message)
    encoded_message = np.where(encoded_message == 0, -1, encoded_message)
    
    # Calculate spectrogram of audio signal
    _, _, spec = plt.specgram(data, Fs=rate, NFFT=1024, noverlap=900)
    phase_data = np.angle(spec)
    
    # Embed message into phase of spectrogram
    alpha = 1000
    phase_data += alpha * encoded_message[:, np.newaxis]
    
    # Synthesize audio signal from modified spectrogram
    modified_spec = np.abs(spec) * np.exp(1j * phase_data)
    modified_data = librosa.istft(modified_spec, win_length=1024, hop_length=900)
    
    return modified_data, rate

import numpy as np

def decode_phase(audio_file):
    # Load audio file
    data, rate = librosa.load(audio_file, sr=None, mono=True)

    # Compute spectrogram
    spec = np.abs(librosa.stft(data))

    # Compute phase
    phase = np.angle(librosa.stft(data))

    # Find the maximum and minimum phase values
    max_phase = np.max(phase)
    min_phase = np.min(phase)

    # Quantize the phase values to 8 bits
    qphase = np.round(((phase - min_phase) / (max_phase - min_phase)) * 255)

    # Convert the phase values to integers
    iphase = qphase.astype(int)

    # Convert the integers to binary strings
    bphase = np.array([np.binary_repr(i, width=8) for i in iphase.flatten()])

    # Convert the binary strings to a single binary string
    binstr = "".join(bphase)

    # Convert the binary string to a byte string
    bytestr = int(binstr, 2).to_bytes(len(binstr) // 8, byteorder='big')

    # Convert the byte string to the original message
    message = bytestr.decode('utf-8')

    return message
