import torch
from diffusers import StableDiffusionPipeline
from PIL import Image, ImageEnhance
from IPython.display import display

# Initialize the pipeline
pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", torch_dtype=torch.float16)
pipe.to("cuda")  # Move model to GPU if available
pipe.enable_model_cpu_offload()

# Function to generate and enhance image
def generate_and_enhance_image(prompt):
    try:
        with torch.no_grad():
            # Generate high-resolution image
            image = pipe(
                prompt,
                height=1024,
                width=1024,
                guidance_scale=3.5,
                num_inference_steps=200,
                generator=torch.Generator("cpu").manual_seed(0)
            ).images[0]

            # Display image before enhancement
            print(f"Image type: {type(image)}")
            print(f"Image size: {image.size}")
            display(image)

            # Enhance image
            enhancer = ImageEnhance.Sharpness(image)
            image = enhancer.enhance(2.0)  # Increase sharpness

            # Save enhanced image
            output_path = "/content/enhanced_image.png"
            image.save(output_path)
            print(f"Enhanced image saved to {output_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Generate and enhance image
generate_and_enhance_image(input("Enter text to convert into Image => "))

# Clear CUDA cache if needed
torch.cuda.empty_cache()