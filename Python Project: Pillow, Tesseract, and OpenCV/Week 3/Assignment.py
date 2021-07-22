import zipfile
from PIL import Image
import cv2 as cv
import numpy as np
from IPython.display import display
import pytesseract

# loading the face detection classifier
face_cascade = cv.CascadeClassifier('readonly/haarcascade_frontalface_default.xml')

# the rest is up to you!
zip_file = zipfile.ZipFile(file='readonly/small_img.zip')
lst = zip_file.infolist()

# Create a list with the name of the pics
name_list = []

# Create a dictionary to store pics.
images = {}

# Iterate over each file in zip_file and append images to dictionary and filenames to name_list
for file in lst:
    images[file.filename] = []
    images[file.filename].append(Image.open(zip_file.open(file.filename)))
    name_list.append(file.filename)

# Iterate over each filename in name_list
for name in name_list:

    # Create a variable pic that will be the picture from dictionary
    pic = images[name][0]

    # Pass image text to text variable
    text = pytesseract.image_to_string(pic).replace('\n', '')

    # Append text to image
    images[name].append(text)

    # Look for Mark in dictionary
    if "Mark" in images[name][1]:
        print("Results found in file", name)

        # Try the following code if Mark is in images
        try:

            # Detect face
            faces = (face_cascade.detectMultiScale(np.array(pic), 1.35, 4)).tolist()

            # Append faces to dictionary
            images[name].append(faces)

            # Create a list that will hold all the faces in the pictures
            faces_in_pics = []

            # Append to faces_in_pics a cropped version of the picture facec
            for x, y, w, h in images[name][2]:
                faces_in_pics.append(pic.crop((x, y, x + w, y + h)))

            # Create contact sheet to place the faces found
            contact_sheet = Image.new(pic.mode, (550, 110 * int(np.ceil(len(faces_in_pics) / 5))))
            x = 0
            y = 0

            # Iterate over each face in faces_in_pics to paste them onto contact sheet
            for face in faces_in_pics:
                face.thumbnail((110, 110))
                contact_sheet.paste(face, (x, y))

                # If no more pics fit in x-axis, move to y-axis
                if x + 110 == contact_sheet.width:
                    x = 0
                    y = y + 110
                # Else continue on x-axis
                else:
                    x = x + 110

            display(contact_sheet)

        # If try doesn't find any faces, say that no faces were detected.
        except:
            print('But there were no faces in that file!')
