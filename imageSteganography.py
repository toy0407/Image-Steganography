import numpy as np
import cv2
from PIL import Image

# Function to convert text to binary string
def text_to_binary(text_str):
    # Convert each character to its ASCII code and then to binary
    binary_str = ''.join([bin(ord(char))[2:].zfill(8) for char in text_str])
    return binary_str


# Function to convert binary string to text
def binary_to_text(binary_str):
    # Convert binary string to integer
    int_val = int(binary_str, 2)
    # Convert integer to ASCII character
    text_val = chr(int_val)
    return text_val

# Function to perform k-means clustering
def kmeans_encode(img, k=5):
    # Reshape image into 2D array
    pixel_values = img.reshape((-1, 3))

    # Convert to float type
    pixel_values = np.float32(pixel_values)

    # Define criteria and apply k-means clustering
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.85)
    _, labels, centers = cv2.kmeans(pixel_values, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    # Reshape labels back into original image shape
    labels = labels.reshape(img.shape[0], img.shape[1])

    # Return labels and centers
    return labels, centers

# Function to encode text in image using LSB encryption
def lsb_encode(src, message, dest):

    img = Image.open(src, 'r')
    width, height = img.size
    array = np.array(list(img.getdata()))

    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4
    total_pixels = array.size//n

    message += "$t3g0"
    b_message = ''.join([format(ord(i), "08b") for i in message])
    req_pixels = len(b_message)

    if req_pixels > total_pixels:
        print("ERROR: Need larger file size")

    else:
        index=0
        for p in range(total_pixels):
            for q in range(0, 3):
                if index < req_pixels:
                    array[p][q] = int(bin(array[p][q])[2:9] + b_message[index], 2)
                    index += 1

        array=array.reshape(height, width, n)
        enc_img = Image.fromarray(array.astype('uint8'), img.mode)
        enc_img.save(dest)
        print("Image Encoded Successfully")



def lsb_decode(src):

    img = Image.open(src, 'r')
    array = np.array(list(img.getdata()))

    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4
    total_pixels = array.size//n

    hidden_bits = ""
    for p in range(total_pixels):
        for q in range(0, 3):
            hidden_bits += (bin(array[p][q])[2:][-1])

    hidden_bits = [hidden_bits[i:i+8] for i in range(0, len(hidden_bits), 8)]

    message = ""
    for i in range(len(hidden_bits)):
        if message[-5:] == "$t3g0":
            break
        else:
            message += chr(int(hidden_bits[i], 2))
    if "$t3g0" in message:
        print("Hidden Message:", message[:-5])
        return message[:-5]
    else:
        print("No Hidden Message Found")