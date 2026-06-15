import cv2
import os

# Define input and output folders
INPUT_FOLDER = "data/raw"
OUTPUT_FOLDER = "data/processed"

# Create output folder if it does not exist
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Loop through all images in raw folder
for filename in os.listdir(INPUT_FOLDER):

    # Process only image files
    if filename.endswith((".jpg", ".jpeg", ".png")):

        image_path = os.path.join(INPUT_FOLDER, filename)

        # Read image
        image = cv2.imread(image_path)

        # Skip invalid files
        if image is None:
            print(f"Could not read {filename}")
            continue

        # Resize image to standard size
        image = cv2.resize(image, (512, 512))

        # Convert image to LAB color space
        lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

        # Split color channels
        l, a, b = cv2.split(lab)

        # Apply CLAHE for contrast enhancement
        clahe = cv2.createCLAHE(
            clipLimit=2.0,
            tileGridSize=(8, 8)
        )

        cl = clahe.apply(l)

        # Merge channels after enhancement
        enhanced_lab = cv2.merge((cl, a, b))

        # Convert back to normal color format
        enhanced_image = cv2.cvtColor(
            enhanced_lab,
            cv2.COLOR_LAB2BGR
        )

        # Apply light Gaussian blur for denoising
        final_image = cv2.bilateralFilter(
            enhanced_image,
            9,
            75,
            75
        )

        # Save processed image
        save_path = os.path.join(
            OUTPUT_FOLDER,
            filename
        )

        cv2.imwrite(save_path, final_image)

        print(f"Processed: {filename}")

print("Preprocessing complete 🚀")