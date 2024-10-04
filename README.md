# Image Segmentation and Shifting Using SAM

## Overview
This project implements **interactive image segmentation** using the **Segment Anything Model (SAM)**. Users can select an image, interactively highlight objects, segment them with a click, and shift the segmented object by providing x and y shift values. The updated image is saved as output.

## Features
- **Interactive Segmentation**: Hover over an object to highlight it.
- **Object Manipulation**: Click to select an object and shift it along the x and y axes.
- **Save Results**: Both the segmented object and the shifted image can be saved as PNG files.

## Setup and Installation

### Prerequisites
- Python 3.x

### Required Libraries
This project depends on several Python libraries, which can be easily installed using the provided `requirements.txt` file. Here’s the list of dependencies:

1. **numpy**: For numerical operations and image processing.
2. **Pillow**: For handling image loading and saving.
3. **matplotlib**: For displaying images and managing interactive events.
4. **segment-anything**: The SAM (Segment Anything Model) for generating object masks.
5. **tkinter**: For creating a file dialog to select images.

To install the dependencies, run the following command in your terminal:

```bash
pip install -r requirements.txt
```



##  Files Required
To run this project, you will need the following file:

- **`sam_vit_h.pth`**: The weights for the SAM model. You can download the model from the official SAM repository using the link below:
  - [Download SAM Weights](https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth)

##  How to Run the Project
Follow these steps to run the project:

1. **Clone the Repository**: Download the project files by cloning the repository or downloading it as a ZIP file.
   
2. **Install Dependencies**: Open your terminal and install the required libraries using the provided `requirements.txt` file:
   ```bash
   pip install -r requirements.txt

3. Run the `finalapp.py` script to start the segmentation
```bash
python finalapp.py
```
4. A file dialog will appear for you to select an image file (.jpg, .jpeg, .png, .bmp, or .gif).
5. Hover over objects in the image to highlight them. Click to select a mask.
6. Enter the x and y shift values when prompted (e.g., x = 20, y = -10), and the selected object will be shifted.
7. The output image will be saved as output_shifted.png.

## Example Workflow

### Original Image
![Original Image](https://github.com/user-attachments/assets/afa38e64-ff14-4a5b-b20a-b3993f38f7cb)

### Segmented Image
![Segmented Image](https://github.com/user-attachments/assets/d97e2672-9cdd-4f88-94f6-f710da18e52f)

### Shifted Image
![Shifted Image](https://github.com/user-attachments/assets/0689000e-3583-452d-b1d2-fdcb72c7acb5)





