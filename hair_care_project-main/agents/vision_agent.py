from PIL import Image
import numpy as np

def analyze_hair_density(image):
    image = image.convert("L")
    arr = np.array(image)

    dark_pixels = (arr < 100).sum()
    total_pixels = arr.size

    ratio = dark_pixels / total_pixels

    if ratio > 0.5:
        return "High Density", ratio
    elif ratio > 0.3:
        return "Medium Density", ratio
    else:
        return "Low Density", ratio