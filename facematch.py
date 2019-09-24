import face_recognition

image_of_elon_musk = face_recognition.load_image_file('/home/avs/Python_practice/face/known/elon_musk.jpg')
elon_musk_face_encoding = face_recognition.face_encodings(image_of_elon_musk)[0]


unknown_image = face_recognition.load_image_file('/home/avs/Python_practice/face/unknown/elon.jpeg')
unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]


# compare faces 
results = face_recognition.compare_faces([elon_musk_face_encoding],unknown_face_encoding)

if results[0]:
    print('This is elon musk')
else:
    print("this is not bill gates")
