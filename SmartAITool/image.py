import cv2
import numpy as np
import os

def check_resize_img(img_path, target_dim):
    """
    Reads an image from the specified path, resizes it to the target dimensions, 
    and then reconstructs it back to its original dimensions. The resized and 
    reconstructed images are saved in a subdirectory named 'resize' within the 
    same directory as the input image.
    Args:
        img_path (str): The file path to the input image.
        target_dim (tuple): The target dimensions (width, height) to resize the image to.
    Returns:
        None
    Side Effects:
        - Saves the resized image as 'resized_<original_filename>' in the 'resize' directory.
        - Saves the reconstructed image as 'reconstruct_<original_filename>' in the 'resize' directory.
        - Prints the original dimensions of the image and the file paths of the saved images.
    Notes:
        - The function creates the 'resize' directory if it does not already exist.
        - The input image is read using OpenCV, and the resized and reconstructed images 
          are saved in the same format as the input image.
    """

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
    
    print("Resized image saved to: " + os.path.join(output_dir, f"resized_{input_filename}") + "\nReconstructed image saved to: " + os.path.join(output_dir, f"reconstruct_{input_filename}"))
