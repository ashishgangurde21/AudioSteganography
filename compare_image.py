from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def compare_images(image1_path, image2_path):
    # Load the two images
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)

    # Check if the two images have the same dimensions
    if image1.size != image2.size:
        raise ValueError("Images must have the same dimensions.")

    # Convert the images to grayscale
    image1_gray = image1.convert("L")
    image2_gray = image2.convert("L")

    # Convert the images to numpy arrays
    image1_array = np.array(image1_gray)
    image2_array = np.array(image2_gray)

    # Calculate the absolute difference between the two images
    diff_array = np.abs(image1_array - image2_array)

    # Convert the difference array to an image
    diff_image = Image.fromarray(diff_array)

    # Convert the difference image to RGB
    diff_image_rgb = diff_image.convert("RGB")

    # Colorize the difference image with red and green
    pixels = diff_image_rgb.load()
    width, height = diff_image_rgb.size
    for y in range(height):
        for x in range(width):
            if pixels[x, y][0] > 10 or pixels[x, y][1] > 10:
                pixels[x, y] = (255, 0, 0)
            else:
                pixels[x, y] = (0, 255, 0)

    # Create a composite image with the original images and the difference image
    composite_image = Image.new("RGB", (image1.width * 3, image1.height))
    composite_image.paste(image1, (0, 0))
    composite_image.paste(image2, (image1.width, 0))
    composite_image.paste(diff_image_rgb, (image1.width * 2, 0))

    # Save the composite image
    composite_image.save("compare_images.png")
    # Load the images
    img1 = Image.open('image.png')
    img2 = Image.open('hello.png')

    # Convert the images to grayscale
    img1 = img1.convert('L')
    img2 = img2.convert('L')

    # Convert the images to arrays
    arr1 = np.array(img1)
    arr2 = np.array(img2)

    # Compute the absolute difference between the arrays
    diff = np.abs(arr1 - arr2)

    # Plot the original images and the difference
    fig, ax = plt.subplots(1, 3, figsize=(10, 5))
    ax[0].imshow(img1, cmap='gray')
    ax[0].set_title('Image 1')
    ax[1].imshow(img2, cmap='gray')
    ax[1].set_title('Image 2')
    ax[2].imshow(diff, cmap='gray')
    ax[2].set_title('Difference')
    plt.show()

    # # Plot a histogram of the pixel-wise difference
    # fig, ax = plt.subplots()
    # ax.hist(diff.ravel(), bins=256)
    # ax.set_title("Pixel-wise Difference Histogram")
    # ax.set_xlabel("Pixel Difference")
    # ax.set_ylabel("Frequency")
    # plt.show()



