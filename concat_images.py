"""
Concating letters we can create words, so this is the method that creates the words
"""
from PIL import Image
from utils import read_image, BASE_PATH
import os

def concatenate_images_horizontally(image_paths, spacing=10):
    images = [read_image(img_path) for img_path in image_paths]

    # Filter out any None values (in case image loading failed)
    images = [img for img in images if img is not None]

    if not images:
        print("No valid images to concatenate.")
        return None

    # Calculate the dimension of the final image
    total_width = sum(img.width for img in images) + (spacing * (len(images) - 1))
    max_height = max(img.height for img in images)

    # Create a new blank image with the determined size
    concatenated_image = Image.new('RGB', (total_width, max_height), (255, 255, 255))

    # Paste each image into the new image
    current_x = 0
    for img in images:
        concatenated_image.paste(img, (current_x, 0))
        current_x += img.width + spacing  # Move the x position to the right

    return concatenated_image


# # Example usage:
# image_paths = ['braile_a.png', 'braile_b.png']
# concatenated_image = concatenate_images_horizontally(image_paths)
#
# if concatenated_image:
#     concatenated_image.show()  # Display the concatenated image
#     # concatenated_image.save(os.path.join(BASE_PATH, 'concatenated_image.jpg'))  # Save the concatenated image
#