<<<<<<< HEAD
import numpy as np
import matplotlib.pyplot as plt
import os


# Function to read the mask file and parse the polygons
def read_mask_file(mask_file_path):
    polygons = []
    with open(mask_file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) > 1:  # Ensuring that there is more than just a category label
                category = int(parts[0])
                coordinates = np.array(parts[1:], dtype=float).reshape(-1, 2)
                polygons.append((category, coordinates))
    return polygons


# Function to calculate the area of a polygon using the shoelace formula
def calculate_polygon_area(polygon):
    n = len(polygon)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += polygon[i][0] * polygon[j][1]
        area -= polygon[j][0] * polygon[i][1]
    area = abs(area) / 2.0
    return area


# Function to process a single image and its corresponding mask file
def process_image_mask(image_path, mask_file_path):
    img = plt.imread(image_path)
    image_height, image_width, _ = img.shape
    polygons = read_mask_file(mask_file_path)

    # Initialize a dictionary to hold the total area for each category
    category_areas = {}

    for category, polygon in polygons:
        # Scale the polygon coordinates to the image size
        polygon[:, 0] *= image_width
        polygon[:, 1] *= image_height
        # Calculate the area
        area = calculate_polygon_area(polygon)
        # Add to the respective category's total area
        if category in category_areas:
            category_areas[category] += area
        else:
            category_areas[category] = area
    return category_areas


# Function to process all images in a given directory
def process_directory(directory_path):
    # Dictionary to hold the results for each image
    results = {}

    # List all files in the given directory
    for filename in os.listdir(directory_path):
        if filename.endswith('.jpg'):
            # Construct the full file paths
            image_path = os.path.join(directory_path, filename)
            mask_file_name = filename.replace('.jpg', '.txt')
            mask_file_path = os.path.join(directory_path, mask_file_name)

            # Process each image and its mask file
            if os.path.exists(mask_file_path):
                category_areas = process_image_mask(image_path, mask_file_path)
                results[filename] = category_areas
            else:
                print(f"Mask file for {filename} not found.")

    return results


# Path to the directory containing the images and mask files
directory_path = r'C:\Users\38492\ultralytics\workspace'

# Process the directory and calculate the areas
directory_results = process_directory(directory_path)

# Output the full results
print(directory_results)
=======
import numpy as np
import matplotlib.pyplot as plt
import os


# Function to read the mask file and parse the polygons
def read_mask_file(mask_file_path):
    polygons = []
    with open(mask_file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) > 1:  # Ensuring that there is more than just a category label
                category = int(parts[0])
                coordinates = np.array(parts[1:], dtype=float).reshape(-1, 2)
                polygons.append((category, coordinates))
    return polygons


# Function to calculate the area of a polygon using the shoelace formula
def calculate_polygon_area(polygon):
    n = len(polygon)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += polygon[i][0] * polygon[j][1]
        area -= polygon[j][0] * polygon[i][1]
    area = abs(area) / 2.0
    return area


# Function to process a single image and its corresponding mask file
def process_image_mask(image_path, mask_file_path):
    img = plt.imread(image_path)
    image_height, image_width, _ = img.shape
    polygons = read_mask_file(mask_file_path)

    # Initialize a dictionary to hold the total area for each category
    category_areas = {}

    for category, polygon in polygons:
        # Scale the polygon coordinates to the image size
        polygon[:, 0] *= image_width
        polygon[:, 1] *= image_height
        # Calculate the area
        area = calculate_polygon_area(polygon)
        # Add to the respective category's total area
        if category in category_areas:
            category_areas[category] += area
        else:
            category_areas[category] = area
    return category_areas


# Function to process all images in a given directory
def process_directory(directory_path):
    # Dictionary to hold the results for each image
    results = {}

    # List all files in the given directory
    for filename in os.listdir(directory_path):
        if filename.endswith('.jpg'):
            # Construct the full file paths
            image_path = os.path.join(directory_path, filename)
            mask_file_name = filename.replace('.jpg', '.txt')
            mask_file_path = os.path.join(directory_path, mask_file_name)

            # Process each image and its mask file
            if os.path.exists(mask_file_path):
                category_areas = process_image_mask(image_path, mask_file_path)
                results[filename] = category_areas
            else:
                print(f"Mask file for {filename} not found.")

    return results


# Path to the directory containing the images and mask files
directory_path = r'C:\Users\38492\ultralytics\workspace'

# Process the directory and calculate the areas
directory_results = process_directory(directory_path)

# Output the full results
print(directory_results)
>>>>>>> 94c54e4f848ace37bf7c1afad41b08a90af25c23
