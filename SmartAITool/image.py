import cv2
import numpy as np
import os

def check_resize_img(img_path, target_dim):

    image = cv2.imread(img_path)    
    real_dim = image.shape[0:2]
    print(real_dim)    
    resized_image = cv2.resize(image, target_dim)
    resized_image = np.asarray(resized_image, dtype=np.uint8)
    real_image = cv2.resize(resized_image, real_dim)
    real_image = np.asarray(real_image, dtype=np.uint8)    
    input_filename = os.path.basename(img_path)
    output_dir = os.path.join(os.path.dirname(img_path), "resize")
    os.makedirs(output_dir, exist_ok=True)
    cv2.imwrite(os.path.join(output_dir, f"reconstruct_{input_filename}"), real_image)
    cv2.imwrite(os.path.join(output_dir, f"resized_{input_filename}"), resized_image)
    
    return "Resized image saved to: " + os.path.join(output_dir, f"resized_{input_filename}") + "\nReconstructed image saved to: " + os.path.join(output_dir, f"reconstruct_{input_filename}")
