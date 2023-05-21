import numpy as np
import scipy.fftpack as fft
import scipy.io.wavfile as wav


def read_audio_file(file_path):
    # Read the audio file and return the sample rate and audio data as a numpy array
    sample_rate, audio_data = wav.read(file_path)
    if audio_data.dtype == np.int16:
        audio_data = audio_data.astype(np.float32) / np.iinfo(np.int16).max
    return sample_rate, audio_data


def write_audio_file(file_path, sample_rate, audio_data):
    # Convert the audio data to int16 format and write it to the output file
    audio_data = np.int16(audio_data * np.iinfo(np.int16).max)
    wav.write(file_path, sample_rate, audio_data)


def encode_message(audio_data, message, alpha=0.1):
    # Perform Fourier transform on audio data
    freq_data = fft.fft(audio_data)

    # Convert message to binary
    binary_message = ''.join(format(ord(c), '08b') for c in message)

    # Repeat binary message as many times as needed to accommodate all the frequency coefficients
    repeated_binary_message = np.tile(np.array(list(binary_message), dtype=int), int(len(freq_data) / len(binary_message)) + 1)

    # Generate phase shifts based on binary array
    phase_shift = alpha * np.pi * repeated_binary_message

    # Apply phase shifts to frequency coefficients
    modified_freq_data = freq_data * np.exp(1j * phase_shift[:len(freq_data)].reshape(-1, 1))


    # Perform inverse Fourier transform to get modified audio data
    modified_audio_data = np.real(fft.ifft(modified_freq_data))

    return modified_audio_data


def decode_message(audio_data, alpha):
    freq_data = np.fft.fft(audio_data)
    phase_shift = np.angle(freq_data)
    binary_message = ''
    for p in phase_shift:
        binary_message += str(int(np.round((p / (alpha * np.pi) + 1) / 2).tolist()))
    message = ''.join(chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message), 8))
    return message.rstrip('\0')



if __name__ == '__main__':
    # Define the input and output file paths
    input_file_path = 'trial.wav'
    output_file_path = 'output.wav'

    # Define the message to encode
    message = 'Hello, world!'

    # Define the alpha parameter for phase modulation
    alpha = 0.1

    # Read the input audio file
    sample_rate, audio_data = read_audio_file(input_file_path)

    # Encode the message in the audio data
    modified_audio_data = encode_message(audio_data, message, alpha)

    # Write the modified audio data to the output file
    write_audio_file(output_file_path, sample_rate, modified_audio_data)

    # Read the modified audio data from the output file
    _, modified_audio_data = read_audio_file(output_file_path)

    # Decode the message from the modified audio data
    decoded_message = decode_message(modified_audio_data, alpha)

    # Print the original message and the decoded message
    print('Original message:', message)
    print('Decoded message:', decoded_message)
