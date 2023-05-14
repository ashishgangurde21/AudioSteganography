import numpy as np
import wave
import struct


def read_wavefile(file_path):
    with wave.open(file_path, 'rb') as f:
        params = f.getparams()
        nframes = params[3]
        audio_data = np.zeros(nframes)
        for i in range(nframes):
            frame = f.readframes(1)
            audio_data[i] = struct.unpack("<h", frame)[0]
        framerate = f.getframerate()
    return audio_data, framerate



def write_wavefile(output_file, framerate, audio_data):
    with wave.open(output_file, 'wb') as f:
        f.setparams((1, 2, framerate, len(audio_data), 'NONE', 'not compressed'))
        for sample in audio_data:
            f.writeframes(struct.pack('<h', int(sample)))

def encode(audio_file, message):
    # Load the audio file
    with wave.open(audio_file, "rb") as wav:
        n_channels, sample_width, framerate, n_frames, _, _ = wav.getparams()
        audio_data = np.zeros(n_frames, dtype=np.float32)
        for i in range(n_frames):
            frame = wav.readframes(1)
            audio_data[i] = struct.unpack("<h", frame)[0] / (2 ** 15)  # Normalize to [-1, 1]

    # Convert the message to a binary array
    message = message.encode("utf-8")
    binary_array = np.unpackbits(np.frombuffer(message, dtype=np.uint8))

    # Embed the binary data in the audio using LSB steganography
    step_size = 2 ** (sample_width - 1) - 1
    for i in range(len(binary_array)):
        start = int(i * (n_frames / len(binary_array)))
        end = int((i + 1) * (n_frames / len(binary_array)))
        if binary_array[i] == 1:
            audio_data[start:end] += step_size / 2
        else:
            audio_data[start:end] -= step_size / 2

    # Write the modified audio data to a new file
    with wave.open("output.wav", "wb") as wav:
        wav.setparams((n_channels, sample_width, framerate, n_frames, "NONE", "Uncompressed"))
        for i in range(n_frames):
            frame = struct.pack("<h", int(audio_data[i] * (2 ** 15)))
            wav.writeframes(frame)

def decode(audio_file):
    # Load the audio file
    with wave.open(audio_file, "rb") as wav:
        n_channels, sample_width, framerate, n_frames, _, _ = wav.getparams()
        audio_data = np.zeros(n_frames, dtype=np.float32)
        for i in range(n_frames):
            frame = wav.readframes(1)
            audio_data[i] = struct.unpack("<h", frame)[0] / (2 ** 15)  # Normalize to [-1, 1]

    # Extract the LSBs of each frame to recover the binary data
    step_size = 2 ** (sample_width - 1) - 1
    binary_array = np.zeros(n_frames, dtype=np.uint8)
    for i in range(n_frames):
        if audio_data[i] >= 0:
            binary_array[i] = 1
        else:
            binary_array[i] = 0
        audio_data[i] = abs(audio_data[i]) % (step_size / 2)

    # Convert the binary data to a string
    message = np.packbits(binary_array).tobytes().decode("utf-8")

    return message



if __name__ == '__main__':
    audio_file = 'trial.wav'
    message_to_hide = "This is a secret message to hide in audio."
    output_file = 'audio2.wav'
    delay = 50
    gain = 0.1

    # Read the audio file
    audio_data, framerate = read_wavefile(audio_file)

    # Encode the message in audio
    encoded_audio_data = encode(audio_data, message_to_hide, delay, gain)

    # Write the encoded audio to file
    write_wavefile(output_file, framerate, encoded_audio_data)

    # Read the encoded audio file
    encoded_audio_data, framerate = read_wavefile(output_file)

    # Decode the message from audio
    # decoded_message = decode_message(encoded_audio_data, delay)

    # # Print the decoded message
    # print(decoded_message)
