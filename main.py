from encryptor import AESEncryptor, Cipher
from imageSteganography import kmeans_encode, text_to_binary, binary_to_text, lsb_encode, lsb_decode



print("Enter Source Image Path")
src = input()
print("Enter Message to Hide")
message = input()
print("Enter Destination Image Path")
dest = input()

aesEncryptor = AESEncryptor()
# Encrypting the text into a Cipher object
cipher = aesEncryptor.encrypt(message)

print("Encoding...")
lsb_encode(src, cipher.encryptedText, dest)



print("Original text: ", message)
print("Encrypted text: ", cipher.encryptedText)

print("Enter Source Image Path")
src2 = input()
print("Decoding...")
eText = lsb_decode(src2)
if (eText != None):
    print(aesEncryptor.decrypt(Cipher(eText,cipher.key,cipher.iv)))


# Load input image

# Convert text to binary string
# binary_text = text_to_binary(cipher.encryptedText)

# Perform k-means clustering
# labels, centers = kmeans_encode(img)

# Encode binary text in LSB of blue channel
# encrypted_img = lsb_encode(img, binary_text)

# Save encrypted image
# cv2.imwrite('encrypted.jpg', encrypted_img)

# Print original and encrypted text





# Decrypting the Cipher object to plain text
# print(aesEncryptor.decrypt(cipher))


# img2 = cv2.imread('encrypted.jpg')

# labels2, centers2 = kmeans_encode(img2)


# # Decode binary text from image
# decoded_text = lsb_decode(img2)

# Print decoded text
# print("Decoded from Image",decoded_text)
