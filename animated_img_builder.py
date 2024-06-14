import os
import glob
import contextlib
import numpy as np
import cv2
from PIL import Image

###########################################################################################
###################################### Configuration ######################################
###########################################################################################

duration=1200
output_format = 'WEBP' # or GIF
output_name='exercise.' + output_format.lower()

###########################################################################################

root_folder = 'exercises'

for folder_name in os.listdir(root_folder):
    folder_path = os.path.join(root_folder, folder_name)
    if os.path.isdir(folder_path):
        folder_path_images = os.path.join(folder_path, '*.png')
        output_img = os.path.join(folder_path, output_name)
        print(f'Processing {folder_path_images}')
        with contextlib.ExitStack() as stack:
            raw_imgs = [stack.enter_context(Image.open(f)) for f in sorted(glob.glob(folder_path_images))]
            if len(raw_imgs) == 0:
                print(' -> no images found')
                continue
            # Get the maximum width and height
            max_width = max(img.width for img in raw_imgs)
            max_height = max(img.height for img in raw_imgs)

            # Add padding to each image to make them the same size
            padded_imgs = []
            for img in raw_imgs:
                # add padding using white background
                new_img = Image.new('RGB', (max_width, max_height), (255, 255, 255))  
                new_img.paste(img, ((max_width - img.width) // 2, (max_height - img.height) // 2))
                
                # update the white background using context color
                # Convert PIL image to OpenCV format
                image_cv = cv2.cvtColor(np.array(new_img), cv2.COLOR_RGB2BGR)

                # Create a mask of the white areas (band) to be filled
                mask = cv2.inRange(image_cv, np.array([255, 255, 255]), np.array([255, 255, 255]))

                # Dilate the mask to cover the edges properly
                kernel = np.ones((5, 5), np.uint8)
                mask_dilated = cv2.dilate(mask, kernel, iterations=1)

                # Inpaint the white areas using the surrounding pixels
                result = cv2.inpaint(image_cv, mask_dilated, 3, cv2.INPAINT_TELEA)

                # Convert the result back to PIL format
                result_img = Image.fromarray(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
                
                padded_imgs.append(result_img)
            
            imgs = (img for img in padded_imgs)
            img = next(imgs)
            
            img.save(fp=output_img, format='WEBP', append_images=imgs, save_all=True, duration=duration, loop=0)
            