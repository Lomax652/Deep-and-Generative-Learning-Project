
# Data Preparation Instructions

## Overview
This project trains a Deep Convolutional GAN (DCGAN) model to generate stylized anime character images based on a custom dataset.

The dataset must be placed inside the `data/` directory with the following structure:

data/
└── dcgan_dataset/
    └── anime/
        ├── image1.jpg
        ├── image2.jpg
        ├── ...

---

## How to Obtain the Data
- You may collect anime-style character images (public domain, licensed for use) from online sources such as:
  - Google Images
  - Anime character databases
  - ArtStation (anime section)
- Alternatively, you can create your own sample images or use datasets provided by the instructor.

Please ensure that the images are appropriate for academic use and comply with copyright policies.

---

## Data Requirements
- File Format: JPG or PNG
- Color Mode: RGB
- Resolution: Images must be resized to 64x64 pixels before training.
- Folder Organization: All images must be placed inside `data/dcgan_dataset/anime/`.

Example:

data/
└── dcgan_dataset/
    └── anime/
        ├── naruto.jpg
        ├── luffy.jpg
        ├── ichigo.jpg
        └── ...

---

## Important Notes
- Images should be centered and properly cropped.
- Backgrounds should be relatively clean for better model convergence.
- At least 50 diverse anime-style images are recommended for stable training.
- Avoid grayscale, corrupted, or low-resolution images.

---

## Final Reminder
After placing your data, you can run the training code as explained in the project ReadMe.txt.  
Make sure to verify the data format and placement before starting training.
