import os

from utils import BASE_PATH
from concat_images import concatenate_images_horizontally


def generate_word_image(word):
    image_paths = [f'braile_{letter}.png' for letter in word.lower()]  # assuming you have images named 'a.jpg', 'b.jpg', etc.
    concatenated_image = concatenate_images_horizontally(image_paths)

    if concatenated_image:
        concatenated_image.show()  # Display the concatenated image
        concatenated_image.save(os.path.join(BASE_PATH, f'{word}_concatenated_image.jpg'))  # Save the concatenated image

# Example usage: Prompt the user to input a word
user_input = input("Digite a palavra que voce quer converter para LIBRAS: ")
generate_word_image(user_input)