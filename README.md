# Deep-and-Generative-Learning-Project

## 📌 Project Overview
This project explores the use of Deep Convolutional Generative Adversarial Networks (DCGAN) to generate synthetic images based on a custom dataset. The goal is to train a GAN model to learn the underlying patterns of the dataset and generate new images with similar characteristics.

## 📂 Dataset
- **Dataset Type**: Custom dataset (e.g., cartoon avatars, hand-written digits, etc.)
- **Preprocessing**: Resized images to 64x64, normalized pixel values.

## 🔧 Model Architecture
- **Generator**: Uses transposed convolution layers to generate images.
- **Discriminator**: A CNN that classifies images as real or fake.
- **Loss Function**: Binary Cross-Entropy Loss
- **Optimizer**: Adam Optimizer
