from pathlib import Path
import cv2
import os

def recordVideo():
    cap = cv2.VideoCapture(0)

    if(cap.isOpened() == False):
        print("Error opening video stream or file")

    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    recordVideo.counter = int(readCounterVal())

    filename = Path("vidrecord.avi")

    if filename.is_file():
        filename = f"vidrecord{str(recordVideo.counter)}.avi"
        recordVideo.counter += 1
        writeCounterVal(str(recordVideo.counter))

    out = cv2.VideoWriter(str(filename),cv2.VideoWriter_fourcc('M','J','P','G'), 10, 
    (frame_width,frame_height))

    print("Recording...")

    while(True):
        ret, frame = cap.read()
    
        if ret == True:
            out.write(frame)

            cv2.imshow('frame', frame)
        
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else: 
            break

    print("Video Recording done!")

    print(os.path.abspath(str(filename)))

    cap.release()
    out.release()
    cv2.destroyAllWindows()

def writeCounterVal(value):
    f = open("counterValVIDR.txt", "w")

    if not Path("counterValVIDR.txt").is_file():
        f.write("0")
    else:
        f.write(value)

    f.close()

def readCounterVal():
    if not Path("counterValVIDR.txt").is_file():
        content = "0"
    else:
        f = open("counterValVIDR.txt", "r")
        content = f.read()
        f.close()

    return content

if __name__ == "__main__":
    recordVideo()
