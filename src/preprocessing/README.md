# Preprocessing Module

## Purpose

The preprocessing module improves the quality and consistency of blood smear images before segmentation and classification.

Since microscopy images captured from low-cost devices or smartphone-attached microscopes may suffer from blur, uneven lighting, low contrast, and inconsistent staining, preprocessing helps standardize images and improve downstream model performance.

## Preprocessing Steps

### 1. Image Resizing

All images are resized to **512 × 512 pixels**.

**Why?**

* Maintains consistent image dimensions
* Reduces computational complexity
* Ensures compatibility with segmentation models

### 2. Contrast Enhancement (CLAHE)

CLAHE (Contrast Limited Adaptive Histogram Equalization) is applied to improve visibility of blood cells.

**Why?**

* Enhances local contrast
* Improves cell visibility in poorly illuminated images
* Helps reveal subtle blood cell structures

### 3. Gaussian Blur (Denoising)

A light Gaussian blur is applied to reduce image noise.

**Why?**

* Removes unwanted graininess
* Smooths minor artifacts
* Preserves important blood cell structures

### Input and Output

**Input Folder:**
`data/raw/`

Contains original microscopy images.

**Output Folder:**
`data/processed/`

Contains enhanced and standardized images ready for segmentation.

## Workflow

Raw Blood Smear Image
↓
Resize (512 × 512)
↓
CLAHE Contrast Enhancement
↓
Gaussian Blur Denoising
↓
Processed Image
