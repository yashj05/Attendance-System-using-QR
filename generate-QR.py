from MyQR import myqr  # To create QR code
import os
import base64  # To encode name into QR code

# Create and Read Student file
f = open('student.txt', 'r')  # Reading the student text file
lines = f.read().split('\n')  # Separating each name with the help of split function and storing in line var.
print(lines)

# Generating multiple QR codes
for i in range(0, len(lines)):
    data = lines[i].encode()  # We are encoding the name of the student in each line into data variable.
    name = base64.b64encode(data)  # Encode the string names into encoded string form.
    version, level, qr_name = myqr.run(str(name),
                                       level='H',
                                       version=1,
                                       # Background
                                       picture='bg-image.png',
                                       colorized=True,
                                       contrast=1.0,
                                       brightness=1.0,
                                       save_name=str(lines[i] + '.bmp'),  # Saving the QR code with their resp names.
                                       save_dir=os.getcwd()) # Saving the QR code in the same directory of current file.
