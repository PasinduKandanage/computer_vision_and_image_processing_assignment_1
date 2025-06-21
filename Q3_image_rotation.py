import cv2

def rotate_image(image_path, angle, output_path):
    img = cv2.imread(image_path)
    h, w = img.shape[:2]
    M = cv2.getRotationMatrix2D((w//2, h//2), angle, 1.0)
    rotated = cv2.warpAffine(img, M, (w, h))
    cv2.imwrite(output_path, rotated)
    print(f"Saved rotated image ({angle}°) to {output_path}")

    cv2.imshow(f'Rotated {angle}°', rotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    input_image = "../images/input.jpg"
    rotate_image(input_image, 45, "../images/output/rotated_45.jpg")
    rotate_image(input_image, 90, "../images/output/rotated_90.jpg")