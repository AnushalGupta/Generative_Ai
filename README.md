# Stable Diffusion Image Generation and Enhancement

This project provides a Python script that leverages the Stable Diffusion model to generate high-resolution images from text prompts. The script also enhances the generated images by increasing their sharpness before saving the final output.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)

## Features

- **Image Generation:** Creates high-resolution images (1024x1024) based on text input.
- **Image Enhancement:** Enhances the generated image by increasing its sharpness.
- **Save Output:** Saves the enhanced image to a specified file path.

## Prerequisites

To run this script, you'll need:

- Python 3.7 or later
- PyTorch (with GPU support for optimal performance)
- `diffusers` library from Hugging Face
- `Pillow` library for image manipulation

## Installation

Follow these steps to set up your environment:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/your-repository-name.git
   cd your-repository-name
