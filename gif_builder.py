import os
import glob
import contextlib
from PIL import Image

###########################################################################################
###################################### Configuration ######################################
###########################################################################################

duration=800
output_name='exercise.gif'

###########################################################################################

root_folder = 'exercises'

# Boucle sur tous les dossiers du répertoire parent
for folder_name in os.listdir(root_folder):
    folder_path = os.path.join(root_folder, folder_name)
    if os.path.isdir(folder_path):
        folder_path_images = os.path.join(folder_path, '*.jpg')
        output_gif = os.path.join(folder_path, output_name)
        print(f'Processing {folder_path_images}')
        # use exit stack to automatically close opened images
        with contextlib.ExitStack() as stack:

            # lazily load images
            imgs = (stack.enter_context(Image.open(f)) for f in sorted(glob.glob(folder_path_images)))

            # extract  first image from iterator
            img = next(imgs)
            
            # https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#gif
            img.save(fp=output_gif, format='GIF', append_images=imgs, save_all=True, duration=duration, loop=0)
            
