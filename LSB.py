import wave

def encode_audio(audio_file, message):
    # Open wave audio file
    audio = wave.open(audio_file, mode='rb')
    
    # Read audio data
    frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))

    # Append null bytes to fill last frame
    message += '0' * (len(frame_bytes) - (len(message) * 8))

    # Convert message to binary
    message_bytes = ''.join([format(ord(i), "08b") for i in message])

    # Hide message in LSB of audio data
    j = 0
    for i in range(0, len(frame_bytes), 2):
        if j < len(message_bytes):
            frame_bytes[i] = int(str(frame_bytes[i])[:-1] + message_bytes[j], 2)
            frame_bytes[i+1] = int(str(frame_bytes[i+1])[:-1] + message_bytes[j+1], 2)
            j += 2

    # Write the new audio data
    output_audio = wave.open('encoded_audio.wav', 'wb')
    output_audio.setparams(audio.getparams())
    output_audio.writeframes(frame_bytes)
    
    # Close the files
    audio.close()
    output_audio.close()

    #Printing the Completion of the Function
    print("The process has been completed")

def decode_audio(audio_file):
    # Open wave audio file
    audio = wave.open(audio_file, mode='rb')
    
    # Read audio data
    frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))

    # Extract LSB of audio data to get message
    message_bits = ''
    for i in range(0, len(frame_bytes), 2):
        byte = frame_bytes[i]
        message_bits += bin(byte)[-1]
        byte = frame_bytes[i+1]
        message_bits += bin(byte)[-1]

    # Convert message from binary to string
    message = ''
    for i in range(0, len(message_bits), 8):
        byte = message_bits[i:i+8]
        message += chr(int(byte, 2))
        if message[-1] == '\0':
            break
    
    # Close the file
    audio.close()

    # Return the decoded message
    return message
