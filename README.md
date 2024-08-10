# # Stable Diffusion Image Generator and Enhancer

This project utilizes the [Stable Diffusion](https://huggingface.co/CompVis/stable-diffusion-v1-4) model to generate high-resolution images based on textual prompts. Additionally, the generated images are enhanced for sharpness using Python's PIL library.

## Features

- **Text-to-Image Generation**: Convert textual descriptions into high-quality images using Stable Diffusion.
- **Image Enhancement**: Automatically enhances the sharpness of generated images.
- **GPU Acceleration**: Leverages CUDA-enabled GPUs for faster image generation.
- **No Restriction** : It supports Unlimited creation of text-to-image and also support nsfw content creation as well.
- **Customization** : Like other text-to-image model where you cannot change the dimension of the image , Well here you can change the dimension (width and height).
- **Free To Use** : you dont need any premium subscription or anything like that is completely free , no need to provide any tokken which usually exhaust after few creation . 

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.8 or higher
- pip (Python package installer)
- CUDA (if using GPU for acceleration)

### Required Python Libraries

You can install the necessary Python libraries using the following commands:

```bash
pip install torch torchvision torchaudio
pip install diffusers
pip install pillow

