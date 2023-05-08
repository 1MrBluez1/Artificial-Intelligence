# -*- coding: utf-8 -*-
"""
@author: Gandalf
"""

import PIL.Image
import PIL.ImageDraw
import face_recognition
#import numpy as np
#import pandas as pd

# Load the known images
image_of_person_1 = face_recognition.load_image_file("person1.jpg")

# Get the face encoding of each person. This can fail if no one is found in the photo.
person_1_face_encoding = face_recognition.face_encodings(image_of_person_1)[0]

#location of faces
face_location1 = face_recognition.face_locations(image_of_person_1)
pil_image1 =PIL.Image.fromarray(image_of_person_1)

for facelocation1 in face_location1:
    top, right, bottom, left = facelocation1
    #print("A face is located at pixel location Top:{}, Right:{}, Bottom:{}, Left:{}".format(top,right,bottom,left))
    #draw red rect around faces
    draw2 = PIL.ImageDraw.Draw(pil_image1)
    draw2.rectangle([left,top,right,bottom], outline="red")
    
pil_image1.show()
print("\nThis gentleman in a suit and tie has been identified as known person 1\n")

# Create a list of all known face encodings
known_face_encodings = [person_1_face_encoding]

# Load the image we want to check
unknown_image = face_recognition.load_image_file("people1.jpg")

print("Second image with a group of unknown people\n")
pil_image2 =PIL.Image.fromarray(unknown_image)
pil_image2.show()

# Get face encodings for any people in the picture
face_locations = face_recognition.face_locations(unknown_image, number_of_times_to_upsample=2)
unknown_face_encodings = face_recognition.face_encodings(unknown_image, known_face_locations=face_locations)

# There might be more than one person in the photo, so we need to loop over each face we found
for unknown_face_encoding in unknown_face_encodings:
    # Test if this unknown face encoding matches any of the three people we know
    results = face_recognition.compare_faces(known_face_encodings, unknown_face_encoding, tolerance=0.6)

    name = "known person 1"
    name1 = "known person 1 from the first image"

    if results[0]:
        name = name
        print(f"Found {name} in the group of people!")
else:
    name1 = name1
    print(f"The {name1} is not in this group of people")


