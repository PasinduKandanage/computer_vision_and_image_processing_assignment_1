import cv2

def spatial_average_filter(image_path, kernel_size, output_path):
    img = cv2.imread(image_path)
    blurred = cv2.blur(img, (kernel_size, kernel_size))
    cv2.imwrite(output_path, blurred)
    print(f"Saved {kernel_size}x{kernel_size} averaged image to {output_path}")

    cv2.imshow(f'{kernel_size}x{kernel_size} Average Filter', blurred)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    input_image = "../images/input.jpg"
    spatial_average_filter(input_image, 3, "../images/output/avg_3x3.jpg")
    spatial_average_filter(input_image, 10, "../images/output/avg_10x10.jpg")
    spatial_average_filter(input_image, 20, "../images/output/avg_20x20.jpg")