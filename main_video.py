import cv2
from simple_facerec import SimpleFacerec
from email_notification import EmailNotification

# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("train_dataset_images/")


# Load Camera
cap = cv2.VideoCapture('http://192.168.18.109:4747/video')

def send_email_notification(email_img):

    email_sender = 'aizaashraf3645@gmail.com'
    email_password = 'basb qrpc sgxf pnfn'
    email_receiver = 'mehernimra064@gmail.com'
    email_subject = "Security alert"
    email_body = """ Unautherized person has entered in your house
                                                                
            """  
    email_img =  email_img
    e = EmailNotification(email_sender,email_password,email_receiver,email_subject,email_body,email_img)
    e.emailfunc()


unauth = "Unknown"
while True:
    ret, frame = cap.read()

    # Detect Faces
    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):

        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
        cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 2)

    #Security alert for unauthorized person
    if unauth == name:  
             
            cv2.imwrite('capture_image/unrecognized_pic.jpg', frame)
            # for i in range (3):
            #     cv2.imwrite('unrecognize'+str(i)+'.png', frame)

            email_img = "capture_image/unrecognized_pic.jpg"
            send_email_notification(email_img)

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()


  