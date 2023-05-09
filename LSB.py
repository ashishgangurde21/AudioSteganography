import wave

def encode_LSB(audio_file, message):
    # Read the audio file as binary data
    with wave.open(audio_file, 'rb') as audio:
        # Get the number of audio frames and channels
        num_frames = audio.getnframes()
        num_channels = audio.getnchannels()
        
        # Convert the message to binary
        binary_message = ''.join(format(ord(c), '08b') for c in message)
        
        # Check that the message will fit in the audio file
        max_bytes = (num_frames * num_channels) // 8
        if len(binary_message) > max_bytes:
            raise ValueError('Message is too large to encode in audio file')
        
        # Read the audio frames and embed the message in the LSB of each sample
        frames = audio.readframes(num_frames)
        new_frames = bytearray(frames)
        message_index = 0
        for i in range(len(new_frames)):
            if message_index < len(binary_message):
                # Convert the audio sample to binary and clear the LSB
                sample = int.from_bytes(bytes([new_frames[i]]), byteorder='little')
                sample &= ~1
                
                # Embed the next bit of the message in the LSB
                bit = int(binary_message[message_index])
                sample |= bit
                
                # Convert the sample back to bytes and update the audio frame
                new_frames[i] = sample.to_bytes(1, byteorder='little')[0]
                
                # Move to the next bit of the message
                message_index += 1
        
        # Write the new audio frames to a new file
        with wave.open('encoded.wav', 'wb') as output:
            output.setparams(audio.getparams())
            output.writeframes(new_frames)

        #Printing the Completion of the Function
        print("The process has been completed")

def decode_LSB(audio_file):
    # Read the audio file as binary data
    with wave.open(audio_file, 'rb') as audio:
        # Get the number of audio frames and channels
        num_frames = audio.getnframes()
        num_channels = audio.getnchannels()
        
        # Read the audio frames and extract the message from the LSB of each sample
        frames = audio.readframes(num_frames)
        binary_message = ''
        for i in range(len(frames)):
            # Convert the audio sample to binary and extract the LSB
            sample = int.from_bytes(bytes([frames[i]]), byteorder='little')
            bit = sample & 1
            
            # Append the extracted bit to the message
            binary_message += str(bit)
            
            # Check if we've reached the end of the message
            if binary_message[-16:] == '0000000000000000':
                break
        
        # Convert the binary message to ASCII
        message = ''
        for i in range(0, len(binary_message), 8):
            byte = binary_message[i:i+8]
            message += chr(int(byte, 2))
            
            # Check if we've reached the end of the message
            if message[-1] == '\x00':
                break
        
        return message

