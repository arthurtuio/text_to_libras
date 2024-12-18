from PIL import Image
import os

# BASE_PATH = '/Users/arthur.antonia/dev/personal_projects/text_to_libras/image_library/'
HOME_DIR = os.path.dirname(os.path.abspath(__file__))

BASE_PATH = HOME_DIR + '/image_library/'


def read_image(path):
    full_path = os.path.join(BASE_PATH, path)
    try:
        image = Image.open(full_path)
        # image.show()  # This will open the default viewer and display the image
        return image
    except Exception as e:
        print(f'Error opening image {full_path}: {e}')
        return None


def read_alphabet_image():
    alphabet_path = BASE_PATH + 'alfabeto/alfabeto.png'
    try:
        image = Image.open(alphabet_path)
        # image.show()  # This will open the default viewer and display the image
        return image
    except Exception as e:
        print(f'Error opening image {alphabet_path}: {e}')
        return None


# def convert_letter_string_to_image_name(string_letter: str):
#     # todo: raise exception se o input n for letra
#
#     return 'braile_' + string_letter + '.png'
#
#



# Example usage:
# image_path = 'braile_a.png'
# read_image(convert_letter_string_to_image_name('a'))
