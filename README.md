# Deep-and-Generative-Learning-Project

## 📌 Project Overview
This project explores the use of Deep Convolutional Generative Adversarial Networks (DCGAN) to generate synthetic images based on a custom dataset. The goal is to train a GAN model to learn the underlying patterns of the dataset and generate new images with similar characteristics.

## 📂 Dataset
- **Dataset Type**: Custom dataset (e.g., cartoon avatars, hand-written digits, etc.)
- **Preprocessing**: Resized images to 64x64, normalized pixel values.


## 🔧 Model Architecture
- **Generator**: Deep transposed convolutional network.
- **Discriminator**: Deep convolutional classifier.
- **Loss Function**: Binary Cross-Entropy Loss.
- **Optimizer**: Adam optimizer (learning rate 0.0002, beta1=0.5).


## 📊 Results & Visualization
- **Generated Images**: Output samples are saved every 50 epochs.
- **Loss Curves**: Generator and Discriminator loss are plotted throughout training.

Improvements in image quality can be observed as training progresses.


## 🔍 Challenges & Future Improvements
- **Challenges**:
- Mode collapse during training.
- Instability with small dataset size.
- **Future Enhancements**:
- Experiment with StyleGAN for better image quality.
- Implement attention mechanisms for fine-grained details.
- Introduce progressive growing training strategies.


## ⚙️ Requirements

- Python 3.8+
- torch >= 1.12.0
- torchvision >= 0.13.0
- matplotlib

(Optional: CUDA-enabled GPU for faster training)

Install required packages using pip:

```bash
pip install torch torchvision matplotlib
