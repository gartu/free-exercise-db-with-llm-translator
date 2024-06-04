import os
import glob
import contextlib
from PIL import Image

###########################################################################################
###################################### Configuration ######################################
###########################################################################################

duration=800
output_format = 'WEBP' # or GIF
output_name='exercise.' + output_format.lower()


###########################################################################################

root_folder = 'exercises'

duration = 800
output_format = 'WEBP'  # or GIF
output_name = 'exercise.' + output_format.lower()

root_folder = 'exercises'

for folder_name in os.listdir(root_folder):
    folder_path = os.path.join(root_folder, folder_name)
    if os.path.isdir(folder_path):
        folder_path_images = os.path.join(folder_path, '*.jpg')
        output_img = os.path.join(folder_path, output_name)
        print(f'Processing {folder_path_images}')
        with contextlib.ExitStack() as stack:
            raw_imgs = [stack.enter_context(Image.open(f)) for f in sorted(glob.glob(folder_path_images))]
            
            # Get the maximum width and height
            max_width = max(img.width for img in raw_imgs)
            max_height = max(img.height for img in raw_imgs)

            # Add padding to each image to make them the same size
            padded_imgs = []
            for img in raw_imgs:
                new_img = Image.new('RGB', (max_width, max_height), (255, 255, 255))  # white background
                new_img.paste(img, ((max_width - img.width) // 2, (max_height - img.height) // 2))
                padded_imgs.append(new_img)
            
            imgs = (img for img in padded_imgs)
            img = next(imgs)
            img.save(fp=output_img, format='WEBP', append_images=imgs, save_all=True, duration=duration, loop=0)
