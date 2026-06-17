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

        # -------------------------------
        # Step 1: Resize image
        # -------------------------------
        image = cv2.resize(image, (512, 512))

        # -------------------------------
        # Step 2: Contrast Enhancement
        # -------------------------------

        # Convert image to LAB color space
        lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

        # Split channels
        l, a, b = cv2.split(lab)

        # Apply CLAHE to brightness channel
        clahe = cv2.createCLAHE(
            clipLimit=2.0,
            tileGridSize=(8, 8)
        )

        cl = clahe.apply(l)

        # Merge channels back
        enhanced_lab = cv2.merge((cl, a, b))

        # Convert back to BGR
        image = cv2.cvtColor(
            enhanced_lab,
            cv2.COLOR_LAB2BGR
        )

        # -------------------------------
        # Step 3: Light Noise Reduction
        # -------------------------------
        image = cv2.GaussianBlur(
            image,
            (3, 3),
            0
        )

        # -------------------------------
        # Step 4: Save processed image
        # -------------------------------
        output_path = os.path.join(
            OUTPUT_FOLDER,
            filename
        )

        cv2.imwrite(output_path, image)

        print(f"Processed: {filename}")

print("Preprocessing complete 🚀")