import cv2 
cap = cv2.VideoCapture('/home/nghi/Pictures/data_tlsc/nghi2.mp4')

number = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    crop_img = frame

    # x ,y ,w, h = 1300, 1000, 1000, 1000
    # crop_img = frame[y:y+h, x:x+w]

    if number % 8 == 0:
        cv2.imwrite("./nghi2/nghi_frame_" + str(number) + ".jpg", crop_img)
    number += 1
    # Display the resulting frame
    # cv2.imshow('frame',crop_img)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break
    if number == 625:
        break

print('done')
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()