def decode(image_path):
#     # Load the image
#     image = Image.open(image_path)

#     # Check if the image mode is RGB
#     if image.mode != "RGB":
#         raise ValueError("Image mode must be RGB.")

#     # Get the width and height of the image
#     width, height = image.size

#     # Initialize the decoded string
#     decoded_str = ""

#     # Loop through the pixels of the image
#     for y in range(height):
#         for x in range(width):
#             # Get the RGB values of the current pixel
#             r, g, b = image.getpixel((x, y))

#             # Get the least significant bit of each color value
#             bit_r = r & 1
#             bit_g = g & 1
#             bit_b = b & 1

#             # Convert the least significant bits to a character
#             char_val = chr((bit_r << 2) + (bit_g << 1) + bit_b)

#             # Check if the character is a null character (end of message)
#             if char_val == "\0":
#                 return decoded_str

#             # Append the character to the decoded string
#             decoded_str += char_val

#     # Return the decoded string
#     return decoded_str

# decode("E:/Study Lectures notes/3rd Year/Sem 6/CS/Course Project/encoded_image.png")