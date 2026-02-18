import cv2
from PIL import Image, ImageEnhance, ImageFilter

# Read the image
image_path = 'pt.jpg'
noisy_image = cv2.imread(image_path)

# Convert the image to grayscale
noisy_image_gray = cv2.cvtColor(noisy_image, cv2.COLOR_BGR2GRAY)

# Denoise the grayscale image
denoised_image_gray = cv2.fastNlMeansDenoising(noisy_image_gray, None, h=10, templateWindowSize=7, searchWindowSize=21)

# Denoise the colored image
denoised_image_color = cv2.fastNlMeansDenoisingColored(noisy_image, None, h=10, hColor=10, templateWindowSize=7, searchWindowSize=21)

# Convert the denoised image to PIL Image
denoised_pil_image = Image.fromarray(cv2.cvtColor(denoised_image_color, cv2.COLOR_BGR2RGB))

# Enhance the denoised image
enhancer = ImageEnhance.Color(denoised_pil_image)
enhanced_image = enhancer.enhance(1.5)  # Increase color saturation by a factor of 1.5

# Enhance contrast
contrast_enhancer = ImageEnhance.Contrast(enhanced_image)
contrast_enhanced_image = contrast_enhancer.enhance(1.2)  # Increase contrast by a factor of 1.2

# Sharpen the image
sharpened_image = contrast_enhanced_image.filter(ImageFilter.SHARPEN)

# Show the sharpened image
sharpened_image.show()
