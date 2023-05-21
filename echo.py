import numpy as np
import wave

def encode_echo(message, audio_file, output_file, delay=0.1, gain=0.5):
    # Load audio file
    with wave.open(audio_file, 'rb') as f:
        params = f.getparams()
        audio_data = np.frombuffer(f.readframes(params[3]), dtype=np.int16)

    # Generate binary representation of message
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    binary_array = np.array(list(map(int, binary_message)))

    # Add echo to audio data
    framerate = params[2]
    delay_samples = int(delay * framerate)
    delayed_audio_data = np.concatenate((np.zeros(delay_samples), audio_data))
    modified_audio_data = audio_data + gain * delayed_audio_data[:len(audio_data)] * binary_array[:, np.newaxis]

    # Save modified audio file
    with wave.open(output_file, 'wb') as f:
        f.setparams(params)
        f.writeframes(modified_audio_data.astype(np.int16).tobytes())

def decode(audio_file, delay=0.1, threshold=0.1):
    # Load audio file
    with wave.open(audio_file, 'rb') as f:
        params = f.getparams()
        audio_data = np.frombuffer(f.readframes(params[3]), dtype=np.int16)

    # Remove echo from audio data
    framerate = params[2]
    delay_samples = int(delay * framerate)
    undelayed_audio_data = audio_data[delay_samples:]
    corr = np.correlate(undelayed_audio_data, audio_data[:len(undelayed_audio_data)], mode='same')
    binary_array = (corr > threshold).astype(int)

    # Convert binary array to string message
    binary_message = ''.join(map(str, binary_array))
    message = ''
    for i in range(0, len(binary_message), 8):
        message += chr(int(binary_message[i:i+8], 2))

    return message

# # Decode message from output audio file
# decoded_message = decode(output_file, len(message) * 8)
# print(decoded_message)  # Output: 'Hello, world!'
