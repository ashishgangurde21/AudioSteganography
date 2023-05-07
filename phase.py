import numpy as np
import scipy.io.wavfile as wavfile
import librosa

def encode_phase(audio_file, message):
    # Load the audio file
    rate, data = wavfile.read(audio_file)

    # Convert the message to binary
    binary_message = ''.join(format(ord(c), '08b') for c in message)

    # Ensure that the message is no longer than the audio signal
    if len(binary_message) > data.shape[0]:
        raise ValueError('Message is too long for audio file')

    # Convert the audio signal to the frequency domain
    data_freq = np.fft.fft(data)

    # Encode the message into the phase information of the audio signal
    for i in range(len(binary_message)):
        bit = int(binary_message[i])
        if bit == 0:
            data_freq[i] = abs(data_freq[i])
        else:
            data_freq[i] = -1 * abs(data_freq[i])

    # Convert the modified signal back to the time domain
    data_mod = np.fft.ifft(data_freq)

    # Save the modified audio signal to a new file
    output_file = 'Phase_encoded.wav'
    wavfile.write(output_file, rate, np.real(data_mod).astype(np.int16))

    print('Message encoded successfully to', output_file)

encode_phase("trial.wav","Hello this is ashish and This is a trial")

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
