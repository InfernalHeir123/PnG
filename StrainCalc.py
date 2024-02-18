import numpy as np
import matplotlib.pyplot as plt
import imageio
import pandas as pd
from scipy.ndimage import gaussian_filter

df = pd.read_csv('VerticalStrainR2.csv', usecols=range(12), skiprows=1, nrows=19) 
df_array = df.values

print(df_array)
# Create a list to store frames
frames = []

# Define common colorbar limits
vmin = df_array.min()
vmax = df_array.max()

# Define Gaussian filter parameters
sigma = 0.4

for i in range(len(df_array)):
    # Apply Gaussian filter to the data
    smoothed_data = gaussian_filter(df_array[i].reshape(4, 3), sigma=sigma)
    
    plt.figure()  # Create a new figure for each plot
    plt.imshow(smoothed_data, vmin=vmin, vmax=vmax, interpolation='bicubic')
    cbar = plt.colorbar()  # Display colorbar
    cbar.set_label('Normalized X Strain')  # Set colorbar label
    plt.title("Razor 1 - Prototype 1")
    plt.savefig(f'frame_{i}.png')  # Save the plot as a PNG file
    plt.close()  # Close the current figure to free memory
    
    # Append the PNG file to the list of frames
    frames.append(imageio.imread(f'frame_{i}.png'))

frame_duration = 5
# Save frames as a GIF with adjusted duration
with imageio.get_writer('Smoothed_Interpolated_Strain_X_R2.gif', duration=frame_duration) as writer:
    for frame in frames:
        writer.append_data(frame)

# Remove temporary frame images
import os
for i in range(len(df_array)):
    os.remove(f'frame_{i}.png')