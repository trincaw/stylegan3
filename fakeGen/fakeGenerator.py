import torch
import torchvision
import numpy as np
import PIL.Image
import sys

sys.path.append('/home/nicolo/Documents/Replay/GAN/stylegan3')  # Adjust the path to the cloned repository

import dnnlib
import legacy

# Load the pretrained model from the .pkl file
network_pkl = '/home/nicolo/Documents/Replay/GAN/stylegan3/fakeGen/network-snapshot-000000.pkl'  # Specify the path to the downloaded .pkl file
device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

with dnnlib.util.open_url(network_pkl) as f:
    G = legacy.load_network_pkl(f)['G_ema'].to(device)

# Generate fake images
num_images = 10  # Number of images to generate
latent_size = G.z_dim
latents = torch.randn(num_images, latent_size, device=device)

# Generate images from the latent vectors
images = G(latents, None)
images = (images.clamp_(-1, 1) + 1) / 2.0  # Normalize the pixel values

# Convert the tensor images to PIL images
images = torchvision.transforms.ToPILImage()(images[0].cpu())

# Display the generated images
images.show()
