import cv2
import pyzbar.pyzbar as pyzbar
import time

# Starting web cam
cap = cv2.VideoCapture(0)
names = []

# Creating a text file to create the record of the attendance
# function for attendance file
fob = open('attendance.txt', 'a+')  # Creating the file in append mode


def enterData(z):
    if z in names:
        pass
    else:
        names.append(z)
        z = "" .join(str(z))
        fob.write(z + '\n')
        return names


print("Reloading code........................................")


# function for data present or not
def checkData(data):
    data = str(data)
    if data in names:
        print("Already present")
    else:
        print("\n" + str(len(names) + 1) + '\n' + 'Present done')
        enterData(data)


while True:
    _, frame = cap.read()
    decodeObject = pyzbar.decode(frame)  # Decoding the frame with the help of pyzbar.
    for obj in decodeObject:
        checkData(obj.data)
        time.sleep(1)

    cv2.imshow('frame', frame)

    # Closing all the windows
    if cv2.waitKey(1) & 0xff == ord('s'):
        cv2.destroyAllWindows()
        break

fob.close()
