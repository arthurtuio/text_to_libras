import os

from utils import BASE_PATH
from concat_images import concatenate_images_horizontally, concatenate_images_with_line_breaks


def _translate_input(phrase):
    """
    Quando eh letra, ja associa a imagem lib.
    QUando eh espaco, associa a uma string `space`
    :param phrase: O texto exatamente igual do input
    :return:
    """
    ordered_frase_characters = []

    for character in phrase:
        if character == ' ':
            ordered_frase_characters.append({
                'is_image': False
            })
        else:
            ordered_frase_characters.append({
                'is_image': True,
                'path': f'braile_{character}.png'}
            )

    print(f"translated input: {ordered_frase_characters}")
    return ordered_frase_characters

def generate_word_image(word):
    image_paths = [f'braile_{letter}.png' for letter in word.lower()]  # assuming you have images named 'a.jpg', 'b.jpg', etc.
    # translated_input = _translate_input(word)  # V3

    # concatenated_image = concatenate_images_horizontally(image_paths)
    concatenated_image = concatenate_images_with_line_breaks(image_paths) # v2, mas o metodo ta bugado ainda

    _NEW_SAVE_PATH = '/Users/arthur.antonia/dev/personal_projects/text_to_libras/saved_words'

    # if concatenated_image:
    #     # concatenated_image.show()  # Display the concatenated image
    #     concatenated_image.save(os.path.join(_NEW_SAVE_PATH, f'{word}_concatenated_image.jpg'))  # Save the concatenated image

    return concatenated_image

# # Example usage: Prompt the user to input a word
# user_input = input("Digite a palavra que voce quer converter para LIBRAS: ")
# generate_word_image(user_input)

# _translate_input(user_input)