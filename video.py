import cv2

def encode_message(video_path, message):
    # Read the video file
    cap = cv2.VideoCapture(video_path)

    # Get the video codec
    fourcc = int(cap.get(cv2.CAP_PROP_FOURCC))

    # Get the video frame rate and dimensions
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Calculate the total number of frames
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Calculate the maximum number of bits that can be encoded in the video
    max_bits = width * height * total_frames * 3 // 8

    # Convert the message to binary
    binary_message = ''.join(format(ord(c), '08b') for c in message)

    # Check if the message can be encoded in the video
    if len(binary_message) > max_bits:
        raise ValueError('Message too large to encode in video')

    # Loop through each frame of the video
    for i in range(total_frames):
        # Read the current frame
        ret, frame = cap.read()

        # Check if the frame was successfully read
        if not ret:
            break

        # Loop through each pixel in the frame
        for row in range(height):
            for col in range(width):
                # Get the pixel values
                b, g, r = frame[row, col]

                # Encode the message in the least significant bit of each color channel
                if len(binary_message) > 0:
                    b = int(format(b, '08b')[:-1] + binary_message[0], 2)
                    binary_message = binary_message[1:]
                if len(binary_message) > 0:
                    g = int(format(g, '08b')[:-1] + binary_message[0], 2)
                    binary_message = binary_message[1:]
                if len(binary_message) > 0:
                    r = int(format(r, '08b')[:-1] + binary_message[0], 2)
                    binary_message = binary_message[1:]

                # Set the pixel values
                frame[row, col] = (b, g, r)

        # Write the modified frame to the output video file
        cv2.imshow('frame', frame)
        cv2.waitKey(1)
        
    # Release the video capture and destroy all windows
    cap.release()
    cv2.destroyAllWindows()

def decode_message(video_path):

    # Read the input video file
    cap = cv2.VideoCapture(video_path)

    # Define the codec for the output video file
    fourcc = cv2.VideoWriter_fourcc(*'H264')

    # Get the frames per second (fps) and frame size from the input video
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

    # Create the VideoWriter object for the output video file
    out = cv2.VideoWriter('output.mp4', fourcc, 10.0, (640, 480))

    # Loop through the frames of the input video
    while cap.isOpened():
        # Read the current frame
        ret, frame = cap.read()
        
        if ret:
            # Extract the least significant bit of each pixel value in the blue channel
            message_bits = ''
            for row in frame:
                for pixel in row:
                    message_bits += bin(pixel[0])[-1]
                    
            # Convert the binary message back to ASCII characters
            decoded_message = ''.join(chr(int(message_bits[i:i+8], 2)) for i in range(0, len(message_bits), 8))
            
            # Print the decoded message to the console
            print(decoded_message)
            
            # Write the current frame to the output video file
            out.write(frame)
            
            # Display the current frame
            cv2.imshow('frame', frame)
            
            # Exit if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    # Release the resources
    cap.release()
    out.release()
    cv2.destroyAllWindows()


encode_message('trial.mp4',"Hello this is ashish")