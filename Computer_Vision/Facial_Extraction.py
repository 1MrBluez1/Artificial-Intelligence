@author: Gandalf
"""

import PIL.ImageDraw
import face_recognition
import PIL.Image

#Image loaded as png
image = face_recognition.load_image_file("faces.jpg")

#Save image to PIL
pil_image =PIL.Image.fromarray(image)

#location of faces
face_location = face_recognition.face_locations(image)

#Number of faces
num_of_faces = len(face_location)
print('The number of faces are {}'.format(num_of_faces),'\n')

for facelocation in face_location:
    top, right, bottom, left = facelocation
    print("A face is located at pixel location \
 Top:{}, Right:{}, Bottom:{}, Left:{}".format(top,right,bottom,left))
    #draw red rect around faces
    draw2 = PIL.ImageDraw.Draw(pil_image)
    draw2.rectangle([left,top,right,bottom], outline="red")
    
pil_image.show()
#pil_image


#Extrtact and print faces from bounding boxes
for extract_face in (face_location):
    face = 1
    top, right, bottom, left = extract_face
    while face > 0:
        face_img = image[top:bottom, left:right]
        pil_face = PIL.Image.fromarray(face_img)
        face = face -1
        pil_face.show()
