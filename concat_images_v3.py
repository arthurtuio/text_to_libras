# """
# Concating letters we can create words, so this is the method that creates the words
#
# DIFERENCA EH QUE TENTO AJUSTAR A IMAGEM PRA TER ESPCACO. Impossivel, fazer com GPT
# """
# from PIL import Image
# from utils import read_image, BASE_PATH
# import os
#
# def concatenate_images_horizontally(image_paths, spacing=10):
#     images = [read_image(img_path) for img_path in image_paths]
#
#     # Filter out any None values (in case image loading failed)
#     images = [img for img in images if img is not None]
#
#     if not images:
#         print("No valid images to concatenate.")
#         return None
#
#     # Calculate the dimension of the final image
#     total_width = sum(img.width for img in images) + (spacing * (len(images) - 1))
#     max_height = max(img.height for img in images)
#
#     print(f'total_widht: {total_width}')
#     print(f'max_height: {max_height}')
#
#     # Create a new blank image with the determined size
#     concatenated_image = Image.new('RGB', (total_width, max_height), (255, 255, 255))
#
#     # Paste each image into the new image
#     current_x = 0
#     for img in images:
#         concatenated_image.paste(img, (current_x, 0))
#         current_x += img.width + spacing  # Move the x position to the right
#
#     return concatenated_image
#
# MAX_WIDTH_PER_LINE = 517*10 # o tamanho base das imagens eh 517, entao eh isso X 10 que achei ok  # Adjust this to your preferred maximum width
#
# def concatenate_images_with_line_breaks(translated_input, spacing=10, max_width=MAX_WIDTH_PER_LINE):
#
#     #### interessante adicionar isso aqui depois novamente
#     # images = [read_image(img_path) for img_path in image_paths]  # image_paths era o nome do input do metodo, mudei o nome agr
#     #
#     # # Filter out any None values (in case image loading failed)
#     # images = [img for img in images if img is not None]
#
#     # if not images:
#     #     print("No valid images to concatenate.")
#     #     return None
#
#     # Calculate dimensions with line breaks
#     lines = []
#     lines_w_space = [] # mesma coisa que acima mas tbm conta os espacos
#
#
#     current_line = []
#     current_line_w_space = [] # mesma coisa que acima mas tbm conta os espacos
#
#     current_width = 0
#     max_height = 0
#
#     for char in translated_input:
#         print(char)
#         if char['is_image']:
#             img = read_image(char['path'])
#
#             if current_width + img.width <= max_width:
#                 current_line.append(img)
#                 current_line_w_space.append(img)
#
#                 current_width += img.width + spacing
#             else:
#                 lines.append(current_line)
#                 lines_w_space.append(current_line_w_space)
#
#                 current_line = [img]
#                 current_line_w_space = [img]
#
#                 current_width = img.width + spacing
#
#         else: # é space
#             # current_width += 517
#             current_line_w_space.append('space')
#
#     #        current_line.append('space')
#
#         max_height = max(max_height, img.height)
#
#     if current_line:
#         lines.append(current_line)
#         lines_w_space.append(current_line_w_space)
#
#
#     print(f'lines: {lines}')
#     print(f'lines_w_space: {lines_w_space}')
#
#     # Calculate dimensions for the final image with line breaks
#     total_height = (max_height + spacing) * len(lines) - spacing
#
#     print(f'spacing: {spacing}')
#
#     lines_widht = []
#     for line in lines_w_space:
#         if 'space' in line:
#             spacing += 100
#             line.remove('space')
#
#         print(f'spacing: {spacing}')
#
#         line_img_widht = sum(img.width for img in line) + spacing * (len(line) - 1)
#         lines_widht.append(line_img_widht)
#
#     total_width = max(lines_widht)
#
#     # total_width = max(
#     #     sum(
#     #         img.width for img in line
#     #     )
#     #     + spacing * (len(line) - 1)
#     #     for line in lines
#     # )
#
#     # Create a new blank image with calculated size
#     concatenated_image = Image.new('RGB', (total_width, total_height), (255, 255, 255))
#
#
#     current_y = 0
#     for line in lines_w_space:
#         current_x = 0
#         for item in line:
#             if item != 'space':
#                 img = item # pq se tratam de imagens
#                 concatenated_image.paste(img, (current_x, current_y))
#                 current_x += img.width + spacing
#             else: # eh um espaco
#                 print('aaaaaaa')
#                 current_x += 100
#
#         print(f'current_x, y: {current_x, current_y, line}')
#
#         current_y += max_height + spacing
#
#     return concatenated_image
#
# # # Example usage:
# # image_paths = ['braile_a.png', 'braile_b.png']
# # concatenated_image = concatenate_images_horizontally(image_paths)
# #
# # if concatenated_image:
# #     concatenated_image.show()  # Display the concatenated image
# #     # concatenated_image.save(os.path.join(BASE_PATH, 'concatenated_image.jpg'))  # Save the concatenated image
# #