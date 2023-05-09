import numpy as np
import scipy.io.wavfile as wav

def encode():
    # Load audio file
    rate, audio_data = wav.read('trial.wav')
    print("Hello")
    # Define message to hide
    message = 'This is a hidden message.'

    # Define echo parameters
    delay = 2000  # delay in samples
    amplitude = 0.1  # amplitude of echo

    # Encode message in echo
    echo = np.zeros_like(audio_data)
    for i, sample in enumerate(audio_data):
        if i < delay:
            echo[i] = sample
        else:
            echo[i] = sample + amplitude * audio_data[i - delay]
            if i == delay + len(message) * 8:
                break  # End of message

    # Save audio file with hidden message
    wav.write('audio_with_hidden_message.wav', rate, audio_data + echo)

def decode():
    # Load audio file with hidden message
    rate, audio_data = wav.read('audio_with_hidden_message.wav')

    # Define echo parameters
    delay = 2000  # delay in samples
    amplitude = 0.1  # amplitude of echo

    # Decode message from echo
    echo = audio_data - np.roll(audio_data, delay) * amplitude
    binary_message = []
    for i, sample in enumerate(echo):
        if i >= delay and i < delay + len('This is a hidden message.') * 8:
            bit = int(round(sample / amplitude))
            binary_message.append(bit)
    message = ''.join(chr(int(''.join(map(str, binary_message[i:i+8])), 2)) for i in range(0, len(binary_message), 8))

    print(message)

encode()
decode()
