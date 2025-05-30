# Deep-and-Generative-Learning-Project

This project explores the use of Deep Convolutional Generative Adversarial Networks (DCGAN) to generate synthetic anime-style character images based on a custom dataset.  
The main goal is to train a GAN model that captures the underlying patterns in the training images and generates new samples with similar visual characteristics.

---

## 📂 Dataset

We use a custom dataset consisting of anime-style character images.  
Before training, all images are resized to 64x64 pixels and normalized to a pixel range of [-1, 1].  
The dataset must be organized under the following folder structure:

```bash
data/
└── dcgan_dataset/
    └── anime/
        ├── image1.jpg
        ├── image2.jpg
        └── ...
```

Images can be collected from publicly available sources such as Google Images, anime art databases, or provided by the instructor.  
Detailed preparation instructions can be found in `data/readme_data.txt`.

---

## 🔧 Model Architecture

The project implements a standard DCGAN architecture:
- **Generator**: A deep transposed convolutional network that maps random noise vectors to images.
- **Discriminator**: A convolutional classifier that distinguishes between real and fake images.
- **Loss Function**: Binary Cross-Entropy Loss is used for both networks.
- **Optimizer**: Adam optimizer with a learning rate of 0.0002 and β₁=0.5.

This architecture follows best practices for stable GAN training, ensuring consistent gradient flows.

---

## 📊 Training and Results

Training proceeds for up to 800 epochs.  
During the process:
- Generated sample images are saved every 50 epochs.
- Loss curves for both Generator and Discriminator are plotted to monitor training stability.
- The best-performing Generator model is selected based on minimum Generator loss and saved automatically.
- Final outputs include the saved model (`best_generator.pth`) and a sample image (`best_generated_image.png`) generated by the best model.

Continuous improvements in image quality can be observed as training progresses.

---

## 🔍 Challenges and Future Improvements

Training GANs with small datasets often leads to mode collapse and instability.  
Future enhancements for this project include:
- Experimenting with more advanced architectures such as StyleGAN.
- Incorporating self-attention mechanisms for capturing fine-grained details.
- Using progressive growing strategies to stabilize training.

---

## ⚙️ Requirements

The following packages are required:

- Python 3.8+
- torch >= 1.12.0
- torchvision >= 0.13.0
- matplotlib

Install all packages using pip:

```bash
pip install torch torchvision matplotlib
```

If a CUDA-capable GPU is available, the code will automatically utilize it to accelerate training.

---

## 🚀 Instructions to Run

1. Clone this repository:

```bash
git clone https://github.com/your_username/your_project_name
cd your_project_name
```

2. Ensure your dataset is prepared following the directory structure described above.

3. Start training by running:

```bash
python dsci498_final.py
```

The script will:
- Train both Generator and Discriminator.
- Save generated images every 50 epochs.
- Plot loss curves throughout training.
- Automatically save the best Generator model and best sample image.

All outputs will be saved in the project directory.

---

## ✨ Notes

- Make sure that all input images are RGB and resized correctly.
- Adjust batch size or learning rate in `dsci498_final.py` if running into resource issues.
- This project was completed as part of the DSCI498 Deep and Generative Learning coursework.

