# Streamlit_Image_Editor

mage Editor App
Overview:
The Image Editor is a simple web app built with Streamlit and Pillow (PIL) that allows users to upload an image, resize, rotate, and apply various filters to the image. The app offers an easy-to-use interface where users can customize their image edits and see the results in real-time.

Prerequisites:
Python 3.x
Streamlit: Install by running pip install streamlit
Pillow: Install by running pip install pillow
How to Run the App:
Clone the repository or save the script file to your local machine.
Navigate to the directory containing the script and install the necessary dependencies:
bash
Copy code
pip install streamlit pillow
Run the Streamlit app by executing:
bash
Copy code
streamlit run <script_name>.py
The app will launch in your default web browser, and you can start uploading images and applying transformations.
Features:
Image Upload: Upload images in JPG, PNG, or JPEG formats.
Resize: Change the dimensions of the uploaded image by specifying new width and height.
Rotate: Rotate the image by any degree.
Filters: Apply one of the following filters:
BLUR
CONTOUR
DETAIL
EMBOSS
SMOOTH
Live Preview: The edited image is displayed after clicking the "Submit" button with the applied transformations.
File Information:
Script File: Contains the main logic for uploading, editing, and displaying the image.
Pillow (PIL): Used for image manipulation tasks such as resizing, rotating, and applying filters.
Example Usage:
Upload an image.
Resize it by inputting new width and height.
Rotate it by entering a degree value.
Select a filter from the dropdown.
Click "Submit" to view the edited image.
License:
This project is under the MIT License.

Feel free to modify the app and adapt it for your specific needs!
