import cv2
from PIL import Image, ImageEnhance, ImageFilter
import os


def enhance_image(input_path, output_path):
    """
    Enhance an image by:
    1. Denoising
    2. Increasing color saturation
    3. Increasing contrast
    4. Sharpening
    """

    # Check if file exists
    if not os.path.exists(input_path):
        print("Error: Image file not found.")
        return

    # Read the image
    noisy_image = cv2.imread(input_path)

    if noisy_image is None:
        print("Error: Unable to read the image.")
        return

    # Convert to grayscale (optional denoising)
    noisy_image_gray = cv2.cvtColor(noisy_image, cv2.COLOR_BGR2GRAY)

    # Denoise grayscale image
    denoised_gray = cv2.fastNlMeansDenoising(
        noisy_image_gray,
        None,
        h=10,
        templateWindowSize=7,
        searchWindowSize=21
    )

    # Denoise colored image
    denoised_color = cv2.fastNlMeansDenoisingColored(
        noisy_image,
        None,
        h=10,
        hColor=10,
        templateWindowSize=7,
        searchWindowSize=21
    )

    # Convert OpenCV image (BGR) to PIL image (RGB)
    pil_image = Image.fromarray(
        cv2.cvtColor(denoised_color, cv2.COLOR_BGR2RGB)
    )

    # Enhance color saturation
    color_enhancer = ImageEnhance.Color(pil_image)
    enhanced_image = color_enhancer.enhance(1.5)

    # Enhance contrast
    contrast_enhancer = ImageEnhance.Contrast(enhanced_image)
    contrast_enhanced_image = contrast_enhancer.enhance(1.2)

    # Sharpen image
    sharpened_image = contrast_enhanced_image.filter(ImageFilter.SHARPEN)

    # Save final image
    sharpened_image.save(output_path)

    # Show image
    sharpened_image.show()

    print("Image enhancement completed successfully!")
    print(f"Output saved at: {output_path}")


if __name__ == "__main__":
    input_image_path = "pt.jpg"
    output_image_path = "enhanced_output.jpg"

    enhance_image(input_image_path, output_image_path)
