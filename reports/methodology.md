# Methodology

## Overview

The proposed system is a low-cost AI-assisted blood smear screening framework designed for use in resource-constrained clinical environments. The system processes blood smear microscope images and performs automated cell segmentation, morphological analysis, and preliminary screening for abnormalities such as malaria-infected cells and sickle-shaped red blood cells.

The framework is intended as a screening and triaging aid rather than a diagnostic device.

---

## 1. Image Acquisition

Blood smear images are obtained from publicly available hematology datasets and are intended to simulate images captured using low-cost digital microscopes or smartphone-attached microscopy systems.

The datasets used in this project include:

* BBBC041 Malaria Dataset
* ErythrocytesIDB2
* ErythrocytesIDB3

These datasets provide examples of healthy red blood cells, white blood cells, malaria-infected cells, and sickle-shaped cells.

---

## 2. Image Preprocessing

Before analysis, each image undergoes a preprocessing stage using OpenCV.

The preprocessing pipeline consists of:

1. Image Resizing (512 × 512 pixels)
2. Contrast Enhancement using CLAHE (Contrast Limited Adaptive Histogram Equalization)
3. Noise Reduction using Gaussian Blur

The objective of preprocessing is to improve image quality while preserving important cellular morphology required for segmentation and feature extraction.

---

## 3. Cell Segmentation

Cell segmentation is performed using YOLOv8-Seg.

Several segmentation approaches were evaluated, including:

* U-Net
* Cellpose
* StarDist
* YOLOv8-Seg

YOLOv8-Seg was selected because it provides:

* Fast inference
* Instance-level segmentation
* Good performance on overlapping cells
* Real-time deployment capability
* Compatibility with low-cost hardware

The segmentation model is trained to identify the following classes:

* RBC
* WBC
* Infected_RBC
* Sickle_RBC

The output of this stage is a segmentation mask for each detected cell.

---

## 4. Morphological Analysis

Following segmentation, morphological features are extracted from the generated cell masks.

The extracted features include:

* Area
* Perimeter
* Circularity
* Aspect Ratio

These features provide quantitative information about cell shape and structure.

Circularity is particularly useful for distinguishing healthy red blood cells from elongated or sickle-shaped cells.

Aspect ratio helps identify abnormal cell elongation associated with sickle-cell morphology.

---

## 5. Screening Logic

The extracted morphological features are used to generate screening flags.

Examples include:

* Healthy Cell
* Possible Sickle Cell
* Malaria-Infected Cell

The screening module acts as a decision-support mechanism and highlights cells that may require further clinical review.

The system does not provide a medical diagnosis and is intended only for preliminary screening purposes.

---

## 6. Dashboard and Visualization

A Streamlit-based dashboard is used to visualize the results.

The dashboard provides:

* Image upload functionality
* Segmentation visualization
* Morphological feature display
* Cell statistics
* Screening flags

This interface enables healthcare personnel to quickly review results and identify potentially abnormal samples.

---

## 7. Overall Workflow

Blood Smear Image

↓

Preprocessing

↓

YOLOv8 Instance Segmentation

↓

Morphological Feature Extraction

↓

Screening Logic

↓

Streamlit Dashboard

↓

Screening Output

The final output is a visual and quantitative screening report that assists healthcare workers in identifying potentially abnormal blood smear samples for further investigation.
