import cv2
import numpy as np

def reduce_intensity_levels(image_path, levels, output_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    step = 256 // levels
    reduced = (img // step) * step
    cv2.imwrite(output_path, reduced)
    print(f"Saved intensity-reduced image to {output_path}")

    cv2.imshow(f'Intensity Levels: {levels}', reduced)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    input_image = "../images/input.jpg"
    output_image = "../images/output/intensity_levels_2.jpg"
    reduce_intensity_levels(input_image, 2, output_image)


