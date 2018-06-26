import face_recognition
from os import listdir
from os.path import isfile, join


def list_file(path):
    lis = []
    for f in listdir(path):
        if isfile(join(path, f)):
            lis.append(join(path, f))
    return lis

if __name__ == "__main__":
    taylor_folder = list_file("taylor_imgs")
    encodings = []
    for img in taylor_folder:
        picture_of_me = face_recognition.load_image_file(img)
        my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]
        encodings.append(my_face_encoding)

    unknown_picture = face_recognition.load_image_file("test.png")
    unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

    results = face_recognition.compare_faces(encodings, unknown_face_encoding)

    print(results)
    if True in results:
        print("Taylor Swift")
    else:
        print("not found")