import cv2
import numpy as np

def block_average(image_path, block_size, output_path):

    img = cv2.imread(image_path)
    
    h, w = img.shape[:2]
    
    h_new = h - (h % block_size)
    w_new = w - (w % block_size)
    img_cropped = img[:h_new, :w_new]
    
    img_blocks = img_cropped.reshape(
        h_new // block_size, block_size, 
        w_new // block_size, block_size, 
        3)
    
    reduced = img_blocks.mean(axis=(1, 3)).astype(np.uint8)
    
    reduced_upscaled = cv2.resize(reduced, (w, h), interpolation=cv2.INTER_NEAREST)
    
    cv2.imwrite(output_path, reduced_upscaled)
    print(f"Saved {block_size}x{block_size} block-averaged image to {output_path}")
    
    cv2.imshow(f'Block Avg {block_size}x{block_size}', reduced_upscaled)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    input_image = "../images/input.jpg"
    block_average(input_image, 3, "../images/output/block_3x3.jpg")
    block_average(input_image, 5, "../images/output/block_5x5.jpg")
    block_average(input_image, 7, "../images/output/block_7x7.jpg")
