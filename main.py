from PIL import Image
import cv2
import PIL
import glob
import easyocr
import sys
path = 'C:\\Users\\Administrator\\Desktop\\SARKARI\\*.jpg'

for files in glob.glob(path):
    image = PIL.Image.open(files)
    width, height = image.size
    print(width, height)
    if height >= 1550:                   # for images with box
        img = Image.open(files)
        img2 = img.crop((1, 180, 1009, 781))
        img2.save(str(files))
    else:                                # for images without box
        img = Image.open(files)
        img3 = img.crop((1, 105, 1009, 699))
        img3.save(str(files))

########################################################################################################################

for files in glob.glob(path):
    image = PIL.Image.open(files)
    img = cv2.imread(files, 2)
    ret, bw_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# cv2.imshow("Binary", bw_img)
# filename = 'savedImage.jpg'
    cv2.imwrite(files, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

########################################################################################################################
path = 'C:\\Users\\Administrator\\Desktop\\SARKARI\\*.jpg'
for files in glob.glob(path):                                     # for taluka
    image = PIL.Image.open(files)
    width, height = image.size
    if height >= 599:
        img = Image.open(files)
        img2 = img.crop((642, 6, 701, 28))
        img2.save("2.jpg")
        reader = easyocr.Reader(['mr', 'hi'], gpu=False)
        output1 = reader.readtext('2.jpg', detail=0)
        sys.stdout = open(str(files) + ".txt", "w", encoding="utf-8")
        print(output1, end=' ')

        img2 = img.crop((0, 0, 1, 1))
        img2.save("2.jpg")
        reader = easyocr.Reader(['mr', 'hi'], gpu=False)
        output1 = reader.readtext('2.jpg', detail=0)
        sys.stdout = open(str(files) + ".txt", "a", encoding="utf-8")
        print(output1, end=',,, ')
    else:
        img = Image.open(files)
        img2 = img.crop((362, 4, 420, 27))
        img2.save("2.jpg")
        reader = easyocr.Reader(['mr', 'hi'], gpu=False)
        output1 = reader.readtext('2.jpg', detail=0)
        sys.stdout = open(str(files) + ".txt", "w", encoding="utf-8")
        print(output1, end=' ')

        img3 = img.crop((642, 81, 699, 102))
        img3.save("3.jpg")
        reader = easyocr.Reader(['mr', 'hi'], gpu=False)
        output1 = reader.readtext('3.jpg', detail=0)
        sys.stdout = open(str(files) + ".txt", "a", encoding="utf-8")
        print(output1, end=',,, ')
########################################################################################################################

for files in glob.glob(path):                                     # for gaav
    image = PIL.Image.open(files)
    width, height = image.size
    if height >= 599:
        img = Image.open(files)
        img2 = img.crop((190, 6, 342, 30))
        img2.save("2.jpg")
        reader = easyocr.Reader(['mr', 'hi'], gpu=False)
        output1 = reader.readtext('2.jpg', detail=0)
        sys.stdout = open(str(files) + ".txt", "a", encoding="utf-8")
        print(output1, end=' ')

        img2 = img.crop((0, 0, 1, 1))
        img2.save("2.jpg")
        reader = easyocr.Reader(['mr', 'hi'], gpu=False)
        output1 = reader.readtext('2.jpg', detail=0)
        sys.stdout = open(str(files) + ".txt", "a", encoding="utf-8")
        print(output1, end=',,, ')

    else:
        img = Image.open(files)
        img2 = img.crop((60, 4, 136, 27))
        img2.save("2.jpg")
        reader = easyocr.Reader(['mr', 'hi'], gpu=False)
        output1 = reader.readtext('2.jpg', detail=0)
        sys.stdout = open(str(files) + ".txt", "a", encoding="utf-8")
        print(output1, end=' ')

        img3 = img.crop((193, 82, 341, 106))
        img3.save("3.jpg")
        reader = easyocr.Reader(['mr', 'hi'], gpu=False)
        output1 = reader.readtext('3.jpg', detail=0)
        sys.stdout = open(str(files) + ".txt", "a", encoding="utf-8")
        print(output1, end=',,, ')

########################################################################################################################
for files in glob.glob(path):                                     # for bhoomi warga
    image = PIL.Image.open(files)
    width, height = image.size
    if height >= 599:
        img = Image.open(files)
        img2 = img.crop((122, 249, 185, 280))
        img2.save("2.jpg")
        reader = easyocr.Reader(['mr', 'hi', 'en'], gpu=False)
        output1 = reader.readtext('2.jpg', detail=0)
        sys.stdout = open(str(files) + ".txt", "a", encoding="utf-8")
        print(output1, end=' ')

        img2 = img.crop((0, 0, 1, 1))
        img2.save("2.jpg")
        reader = easyocr.Reader(['mr', 'hi', 'en'], gpu=False)
        output1 = reader.readtext('2.jpg', detail=0)
        sys.stdout = open(str(files) + ".txt", "a", encoding="utf-8")
        print(output1, end=',,, ')

    else:
        img = Image.open(files)
        img2 = img.crop((189, 334, 257, 376))
        img2.save("2.jpg")
        reader = easyocr.Reader(['mr', 'hi', 'en'], gpu=False)
        output1 = reader.readtext('2.jpg', detail=0)
        sys.stdout = open(str(files) + ".txt", "a", encoding="utf-8")
        print(output1, end=' ')

        img3 = img.crop((193, 82, 341, 106))
        img3.save("3.jpg")
        reader = easyocr.Reader(['mr', 'hi', 'en'], gpu=False)
        output1 = reader.readtext('3.jpg', detail=0)
        sys.stdout = open(str(files) + ".txt", "a", encoding="utf-8")
        print(output1, end=',,, ')
########################################################################################################################
for files in glob.glob(path):                                                # for jirayat
    image = PIL.Image.open(files)
    width, height = image.size
    if height >= 599:
        img = Image.open(files)
        img2 = img.crop((118, 163, 185, 180))
        img2.save("2.jpg")
        reader = easyocr.Reader(['mr', 'hi', 'en'], gpu=False)
        output1 = reader.readtext('2.jpg', detail=0)
        sys.stdout = open(str(files) + ".txt", "a", encoding="utf-8")
        print(output1, end=' ')

        img2 = img.crop((0, 0, 1, 1))
        img2.save("2.jpg")
        reader = easyocr.Reader(['mr', 'hi', 'en'], gpu=False)
        output1 = reader.readtext('2.jpg', detail=0)
        sys.stdout = open(str(files) + ".txt", "a", encoding="utf-8")
        print(output1, end=',,, ')

    else:
        img = Image.open(files)
        img2 = img.crop((186, 176, 280, 200))
        img2.save("2.jpg")
        reader = easyocr.Reader(['mr', 'hi', 'en'], gpu=False)
        output1 = reader.readtext('2.jpg', detail=0)
        sys.stdout = open(str(files) + ".txt", "a", encoding="utf-8")
        print(output1, end=' ')

        img3 = img.crop((123, 237, 186, 256))
        img3.save("3.jpg")
        reader = easyocr.Reader(['mr', 'hi', 'en'], gpu=False)
        output1 = reader.readtext('3.jpg', detail=0)
        sys.stdout = open(str(files) + ".txt", "a", encoding="utf-8")
        print(output1, end=',,, ')
########################################################################################################################
for files in glob.glob(path):                                                # for bagayat
    image = PIL.Image.open(files)
    width, height = image.size
    if height >= 599:
        img = Image.open(files)
        img2 = img.crop((118, 183, 185, 194))
        img2.save("2.jpg")
        reader = easyocr.Reader(['mr', 'hi', 'en'], gpu=False)
        output1 = reader.readtext('2.jpg', detail=0)
        sys.stdout = open(str(files) + ".txt", "a", encoding="utf-8")
        print(output1, end=' ')

        img2 = img.crop((0, 0, 1, 1))
        img2.save("2.jpg")
        reader = easyocr.Reader(['mr', 'hi', 'en'], gpu=False)
        output1 = reader.readtext('2.jpg', detail=0)
        sys.stdout = open(str(files) + ".txt", "a", encoding="utf-8")
        print(output1, end=',,, ')

    else:
        img = Image.open(files)
        img2 = img.crop((186, 198, 275, 217))
        img2.save("2.jpg")
        reader = easyocr.Reader(['mr', 'hi', 'en'], gpu=False)
        output1 = reader.readtext('2.jpg', detail=0)
        sys.stdout = open(str(files) + ".txt", "a", encoding="utf-8")
        print(output1, end=' ')

        img3 = img.crop((122, 254, 186, 2567))
        img3.save("3.jpg")
        reader = easyocr.Reader(['mr', 'hi', 'en'], gpu=False)
        output1 = reader.readtext('3.jpg', detail=0)
        sys.stdout = open(str(files) + ".txt", "a", encoding="utf-8")
        print(output1, end=',,, ')
########################################################################################################################
for files in glob.glob(path):                                                # for ekun kshetra
    image = PIL.Image.open(files)
    width, height = image.size
    if height >= 599:
        img = Image.open(files)
        img2 = img.crop((113, 305, 193, 320))
        img2.save("2.jpg")
        reader = easyocr.Reader(['mr', 'hi', 'en'], gpu=False)
        output1 = reader.readtext('2.jpg', detail=0)
        sys.stdout = open(str(files) + ".txt", "a", encoding="utf-8")
        print(output1, end=' ')

        img2 = img.crop((0, 0, 1, 1))
        img2.save("2.jpg")
        reader = easyocr.Reader(['mr', 'hi', 'en'], gpu=False)
        output1 = reader.readtext('2.jpg', detail=0)
        sys.stdout = open(str(files) + ".txt", "a", encoding="utf-8")
        print(output1, end=',,, ')

    else:
        img = Image.open(files)
        img2 = img.crop((186, 291, 266, 309))
        img2.save("2.jpg")
        reader = easyocr.Reader(['mr', 'hi', 'en'], gpu=False)
        output1 = reader.readtext('2.jpg', detail=0)
        sys.stdout = open(str(files) + ".txt", "a", encoding="utf-8")
        print(output1, end=' ')

        img3 = img.crop((120, 378, 186, 395))
        img3.save("3.jpg")
        reader = easyocr.Reader(['mr', 'hi', 'en'], gpu=False)
        output1 = reader.readtext('3.jpg', detail=0)
        sys.stdout = open(str(files) + ".txt", "a", encoding="utf-8")
        print(output1, end=',,, ')
########################################################################################################################
for files in glob.glob(path):                                                # for ekun potkharaba
    image = PIL.Image.open(files)
    width, height = image.size
    if height >= 599:
        img = Image.open(files)
        img2 = img.crop((120, 285, 186, 300))
        img2.save("2.jpg")
        reader = easyocr.Reader(['mr', 'hi', 'en'], gpu=False)
        output1 = reader.readtext('2.jpg', detail=0)
        sys.stdout = open(str(files) + ".txt", "a", encoding="utf-8")
        print(output1, end=' ')

        img2 = img.crop((0, 0, 1, 1))
        img2.save("2.jpg")
        reader = easyocr.Reader(['mr', 'hi', 'en'], gpu=False)
        output1 = reader.readtext('2.jpg', detail=0)
        sys.stdout = open(str(files) + ".txt", "a", encoding="utf-8")
        print(output1, end=',,, ')

    else:
        img = Image.open(files)
        img2 = img.crop((185, 382, 258, 401))
        img2.save("2.jpg")
        reader = easyocr.Reader(['mr', 'hi', 'en'], gpu=False)
        output1 = reader.readtext('2.jpg', detail=0)
        sys.stdout = open(str(files) + ".txt", "a", encoding="utf-8")
        print(output1, end=' ')

        img3 = img.crop((124, 360, 187, 375))
        img3.save("3.jpg")
        reader = easyocr.Reader(['mr', 'hi', 'en'], gpu=False)
        output1 = reader.readtext('3.jpg', detail=0)
        sys.stdout = open(str(files) + ".txt", "a", encoding="utf-8")
        print(output1, end=',,, ')
########################################################################################################################
for files in glob.glob(path):                                                # for akarani
    image = PIL.Image.open(files)
    width, height = image.size
    if height >= 599:
        img = Image.open(files)
        img2 = img.crop((120, 322, 185, 339))
        img2.save("2.jpg")
        reader = easyocr.Reader(['mr', 'hi', 'en'], gpu=False)
        output1 = reader.readtext('2.jpg', detail=0)
        sys.stdout = open(str(files) + ".txt", "a", encoding="utf-8")
        print(output1, end=' ')

        img2 = img.crop((0, 0, 1, 1))
        img2.save("2.jpg")
        reader = easyocr.Reader(['mr', 'hi', 'en'], gpu=False)
        output1 = reader.readtext('2.jpg', detail=0)
        sys.stdout = open(str(files) + ".txt", "a", encoding="utf-8")
        print(output1, end=',,, ')

    else:
        img = Image.open(files)
        img2 = img.crop((188, 405, 251, 428))
        img2.save("2.jpg")
        reader = easyocr.Reader(['mr', 'hi', 'en'], gpu=False)
        output1 = reader.readtext('2.jpg', detail=0)
        sys.stdout = open(str(files) + ".txt", "a", encoding="utf-8")
        print(output1, end=' ')

        img3 = img.crop((123, 397, 185, 412))
        img3.save("3.jpg")
        reader = easyocr.Reader(['mr', 'hi', 'en'], gpu=False)
        output1 = reader.readtext('3.jpg', detail=0)
        sys.stdout = open(str(files) + ".txt", "a", encoding="utf-8")
        print(output1, end=',,, ')
########################################################################################################################
for files in glob.glob(path):
    image = PIL.Image.open(files)
    sys.stdout = open(str(files) + ".txt", "a", encoding="utf-8")
    print(str(files), end=' ')

########################################################################################################################

########################################################################################################################

# file_list = glob.glob('*.txt')
# print(file_list)
path = 'C:\\Users\\Administrator\\Desktop\\SARKARI\\*.txt'

for files in glob.glob(path):
    with open(files, 'r', encoding="utf8") as f:
        read = f.read()
        sys.stdout = open("vadgaon sarkari.csv", "a", encoding="utf-8")
        print(read)
