A.Title:
Image Segmentation and shifting using SAM.

B.Overview:
This project implements interactive image segmentation using the Segment Anything Model (SAM). Users can select an image, 
interactively highlight objects, click to segment them, and shift the segmented object by providing x and y shift values. The updated image is saved as output.

C.Features:
1. Interactive Segmentation: Hover over an object to highlight it.
2. Object Manipulation: Click to select an object and shift it along x and y axes.
3. Save Results: The segmented object and the shifted image can be saved as PNG files.

D.Setup and Installation:
Prerequisites
Python 3.x
Required libraries (install them using pip).
Dependencies
The project depends on several Python libraries. You can install them all at once using the requirements.txt file provided in the repository.

Here's the list of the dependencies:
1. numpy: For numerical operations and image processing.
2. Pillow: For handling image loading and saving.
3. matplotlib: For displaying the images and handling interactive events.
4. segment-anything: The SAM (Segment Anything Model) for generating object masks.
5. tkinter: For creating a file dialog to select images.
   
To install the dependencies, run the following command in your terminal:
pip install -r requirements.txt

E.Files Required:
sam_vit_h.pth: The SAM model's weights. You can download the model from the official SAM repository. (https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth)

F.How to Run the Project:
1. Clone the repository or download the project files.
2. Install the required dependencies using the requirements.txt
(pip install -r requirements.txt)
3. Run the finalapp.py script to start the segmentation
(python finalapp.py)
4. A file dialog will appear for you to select an image file (.jpg, .jpeg, .png, .bmp, or .gif).
5. Hover over objects in the image to highlight them. Click to select a mask.
6. Enter the x and y shift values when prompted (e.g., x = 20, y = -10), and the selected object will be shifted.
7. The output image will be saved as output_shifted.png.

Example Workflow:
Original Image:
![wall hanging](https://github.com/user-attachments/assets/f3ebc3be-2893-4612-a646-5a91f9b4cd3b)

Segmented Image:
![output_segmented](https://github.com/user-attachments/assets/62cb3eee-1518-46ba-8b3c-17f9700bd6b5)

Shifted Image:
![output_shifted](https://github.com/user-attachments/assets/00e27765-4b15-44ac-a8ee-0bb26117a4b8)



