# image-improving-diminished-image
### About the Project
[cite_start]This project's code is for **denoising and enhancing images**[cite: 1]. [cite_start]It uses the `cv2` and `Pillow` libraries in Python to improve image quality[cite: 1, 2].

---

### Features
The project performs the following actions on an image:

* [cite_start]**Denoising**: It removes noise from both grayscale and color images[cite: 2]. [cite_start]The code uses the `cv2.fastNlMeansDenoising()` function for grayscale images and `cv2.fastNlMeansDenoisingColored()` for color images[cite: 2].
* [cite_start]**Color and Contrast Enhancement**: It improves the image's color saturation and contrast[cite: 5]. [cite_start]The `ImageEnhance` module from the `Pillow` library is used to increase color by a factor of 1.5 and contrast by a factor of 1.2[cite: 7, 9, 13, 14].
* [cite_start]**Sharpening**: The image is sharpened using the `ImageFilter.SHARPEN` function to make details clearer[cite: 15, 17].
* [cite_start]**Display**: The final, sharpened image is displayed using `sharpened_image.show()`[cite: 19, 20].

---

### How to Run
1.  **Dependencies**: Make sure you have the `cv2` (OpenCV) and `Pillow` (PIL) libraries installed.
2.  [cite_start]**Image**: Place your image file in the same directory as the script and name it `gt.jpg`[cite: 2].
3.  **Execution**: Run the Python script. [cite_start]The script will process the image and display the improved version[cite: 2, 20].

---

### Image Examples
* [cite_start]**Denoised Image**: The provided document shows a denoised grayscale image[cite: 22].
* [cite_start]**Improved Image**: An example of an improved image (after denoising, enhancing, and sharpening) is also shown, featuring a white bird[cite: 21]. 
