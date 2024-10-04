import numpy as np
from segment_anything import SamAutomaticMaskGenerator, sam_model_registry
from PIL import Image
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

# Initialize global variables
selected_mask = None
masks = []
image_np = None

def on_mouse_move(event):
    global selected_mask, masks, image_np, fig, ax
    
    if event.inaxes != ax:
        return  # Ignore if mouse is not over the image

    # Get the coordinates of the mouse position
    x, y = int(event.xdata), int(event.ydata)
    
    # Ensure coordinates are within the image dimensions
    if x < 0 or x >= image_np.shape[1] or y < 0 or y >= image_np.shape[0]:
        return

    # Find the mask that corresponds to the hovered location
    for mask in masks:
        if mask['segmentation'][y, x] > 0:
            selected_mask = mask['segmentation']
            break

    # Update the display to highlight the object under the cursor
    overlay = image_np.copy()
    if selected_mask is not None:
        overlay[selected_mask > 0] = [255, 0, 0]  # Apply red color to the segmented area

    # Clear the current axis and redraw the image with the highlighted mask
    ax.clear()
    ax.imshow(overlay)
    ax.set_title('Hover to highlight object')
    ax.axis('off')
    fig.canvas.draw()

def on_mouse_click(event):
    global selected_mask, masks, image_np
    
    # Get the coordinates of the mouse click
    x, y = int(event.xdata), int(event.ydata)
    
    # Ensure coordinates are within the image dimensions
    if x < 0 or x >= image_np.shape[1] or y < 0 or y >= image_np.shape[0]:
        print("Clicked outside of image bounds.")
        return
    
    # Find the mask that corresponds to the clicked location
    for mask in masks:
        if mask['segmentation'][y, x] > 0:
            selected_mask = mask['segmentation']  # Save the selected mask
            print("Mask selected.")
            break
    else:
        print("No mask selected at the clicked location.")

    if selected_mask is not None:
        # Overlay red mask on the image
        overlay = image_np.copy()
        overlay[selected_mask > 0] = [255, 0, 0]  # Apply red color to the segmented area
        
        # Display using Matplotlib
        plt.imshow(overlay)
        plt.title('Image with Selected Mask')
        plt.axis('off')
        plt.show()
        
        # Save the result
        output_image = Image.fromarray(overlay)
        output_image.save('output_segmented.png')
        print("Segmented image saved as 'output_segmented.png'.")

def shift_segmented_object(dx, dy):
    global selected_mask, image_np

    if selected_mask is None:
        print("No object selected for shifting.")
        return

    # Create a copy of the original image to modify
    updated_image = image_np.copy()

    # Get coordinates of the original selected mask
    mask_coords = np.argwhere(selected_mask)

    # Collect background color samples, avoiding the selected object
    background_colors = []

    for coord in mask_coords:
        y, x = coord
        
        # Sample a wider area around the selected object
        for dy_offset in range(-10, 11):  # Sample 10 pixels above and below
            for dx_offset in range(-10, 11):  # Sample 10 pixels left and right
                new_y, new_x = y + dy_offset, x + dx_offset
                # Ensure we stay within the image bounds
                if (0 <= new_y < image_np.shape[0] and 
                    0 <= new_x < image_np.shape[1] and 
                    selected_mask[new_y, new_x] == 0):  # Ensure it's not part of the selected object
                    background_colors.append(image_np[new_y, new_x].tolist())
    
    # Calculate the median background color from samples
    if background_colors:
        background_color = np.median(background_colors, axis=0).astype(int)
    else:
        background_color = [255, 255, 255]  # Fallback to white if no valid background color found

    # Shift the mask
    shifted_mask = np.zeros_like(selected_mask)
    
    for y in range(selected_mask.shape[0]):
        for x in range(selected_mask.shape[1]):
            if selected_mask[y, x] > 0:
                new_x = x + dx
                new_y = y + dy
                
                # Ensure the new coordinates are within bounds
                if 0 <= new_x < updated_image.shape[1] and 0 <= new_y < updated_image.shape[0]:
                    # Move the pixel color from the original image to the new position
                    shifted_mask[new_y, new_x] = 1  # Set the shifted mask position

    # Clear the original object's position with the background color
    updated_image[selected_mask > 0] = background_color

    # Overlay the shifted object on top of the updated image
    updated_image[shifted_mask > 0] = image_np[selected_mask > 0]

    # Display the updated image
    plt.imshow(updated_image)
    plt.title('Image with Shifted Mask')
    plt.axis('off')
    plt.show()

    # Save the updated image
    output_image = Image.fromarray(updated_image)
    output_image.save('output_shifted.png')
    print("Updated image saved as 'output_shifted.png'.")

def segment_image_interactively(image_path):
    global masks, image_np, fig, ax
    
    # Load the image using PIL, then convert to NumPy array
    image = Image.open(image_path)
    image_np = np.array(image)

    # Initialize SAM model
    sam_model = sam_model_registry["default"]("sam_vit_h.pth")
    mask_generator = SamAutomaticMaskGenerator(sam_model)
    
    # Generate masks for the objects in the scene
    masks = mask_generator.generate(image_np)

    # Display the image using Matplotlib
    fig, ax = plt.subplots()  # Correct initialization
    ax.imshow(image_np)
    ax.set_title('Hover over the object to highlight it')
    ax.axis('off')

    # Connect the hover and click events to Matplotlib's event system
    fig.canvas.mpl_connect('motion_notify_event', on_mouse_move)
    fig.canvas.mpl_connect('button_press_event', on_mouse_click)
    plt.show()

    # Ask for shift values after selecting the object
    dx = int(input("Enter the x shift (negative to shift left, positive to shift right): "))
    dy = int(input("Enter the y shift (negative to shift up, positive to shift down): "))
    shift_segmented_object(dx, dy)

def open_image_file():
    # Initialize Tkinter root (hidden window)
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Open a file dialog to select an image file
    file_path = filedialog.askopenfilename(
        title="Select an image file",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")]
    )
    if file_path:
        print(f"Selected file: {file_path}")
        segment_image_interactively(file_path)
    else:
        print("No file selected.")

# Start the process
open_image_file()
