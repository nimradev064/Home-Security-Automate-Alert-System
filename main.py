import cv2
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from pymongo import MongoClient
from datetime import datetime
import face_recognition
import base64
import numpy as np
import io
from io import BytesIO
from PIL import Image
import base64
from email_notification import EmailNotification



# MongoDB connection
connection_string = "mongodb+srv://mehernimra064:shahzadi123456789@cluster0.mgo1zg0.mongodb.net/"
client = MongoClient(connection_string)
db = client.get_database("security_alert")
collection = db["visitor_data"]


def send_email_notification(frame):

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cv2.imwrite('capture_image/unknown_person.jpg', frame)

    email_sender = ''
    email_password = ''
    email_receiver = ''
    email_subject = "Security Alert"
    email_body = """ Unauthorized person has entered in your house
                                                                
            """  
    email_img =  "capture_image/unknown_person.jpg"
    e = EmailNotification(email_sender, email_password, email_receiver, 
                        email_subject, email_body, email_img)

    e.emailfunc()


class SecurityApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Security System")

        # Load encoding images from the database
        self.known_face_encodings = []
        self.load_known_face_encodings()
        self.page_1()


    def load_known_face_encodings(self):
        for record in collection.find():
            try:
                person_image_base64 = record["person_image"]

                # Decode the base64 string back to a PIL Image
                image_bytes = base64.b64decode(person_image_base64)
                image = Image.open(io.BytesIO(image_bytes))

                # Convert the PIL Image to a NumPy array
                image_np = np.array(image)

                if image_np is not None:
                    # Load the image for face recognition
                    known_face_encoding = face_recognition.face_encodings(image_np)
                    if known_face_encoding:
                        self.known_face_encodings.append(known_face_encoding[0])
                    else:
                        print(f"No face found in the image for {record['name']}")
                else:
                    print(f"Failed to decode image for {record['name']}")

            except Exception as e:
                print(f"Error processing image for {record['name']}: {str(e)}")

    def page_1(self):
        self.frame = ttk.Frame(self.root)
        self.frame.pack()

        self.label = ttk.Label(self.frame, text="Checking for authorized person...")
        self.label.pack(pady=20)

        # Capture image from webcam
        self.capture_image()

    def capture_image(self):

        # cap = cv2.VideoCapture("train_dataset_images/Elon Musk.jpg")
        cap = cv2.VideoCapture('http://192.168.18.109:4747/video')

        ret, frame = cap.read()
        # cap.release()

        frame = cv2.resize(frame, (480, 480), interpolation=cv2.INTER_LINEAR)


        # Perform face recognition
        face_locations = face_recognition.face_locations(frame)
        if face_locations:
            input_face_encoding = face_recognition.face_encodings(frame, face_locations)[0]

            # Check if the input face matches any known face
            match_results = face_recognition.compare_faces(
                self.known_face_encodings, input_face_encoding
            )

            if any(match_results):
                name = collection.find()[match_results.index(True)]["name"]
                self.label.config(text=f"Welcome back, {name}!")
                self.root.after(2000, self.root.destroy)  # Close the app after 2 seconds
            else:
                self.label.config(text="Unauthorized person detected. Is this person known or unknown?")
                self.load_webcam_image(frame)

                ttk.Button(self.frame, text="Known", command=self.page_2_known).pack(side=tk.LEFT, padx=20)
                ttk.Button(self.frame, text="Unknown", command=self.page_2_unknown).pack(side=tk.RIGHT, padx=20)
        else:
            self.label.config(text="No face detected. Please try again.")
            self.root.after(2000, self.root.destroy)  # Close the app after 2 seconds

    def load_webcam_image(self, frame):
        self.cv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.photo = ImageTk.PhotoImage(image=Image.fromarray(self.cv_img))
        self.label_img = ttk.Label(self.frame, image=self.photo)
        self.label_img.pack()

    def page_2_known(self):
        person_data = self.check_person_in_record()
        if person_data:
            self.label.config(text=f"Welcome back, {person_data['name']}!")
        else:
            self.show_page_2()

    def check_person_in_record(self):
        person_name = "John Doe"  # Replace with the detected person's name
        query = {"name": person_name}
        result = collection.find_one(query)
        return result

    def page_2_unknown(self):
        
        print("Alert has been generated")

        # Pass the captured frame to the send_email_notification function
        send_email_notification(self.cv_img)

        print("Email notification has been sent!")

        self.label.config(text=f"Alert notification email has been sent!")
        self.root.after(2000, self.root.destroy)  # Close the app after 2 seconds


    def show_page_2(self):
        self.frame.destroy()

        self.frame = ttk.Frame(self.root)
        self.frame.pack()

        ttk.Label(self.frame, text="Additional Information").pack(pady=20)

        ttk.Label(self.frame, text="Name:").pack()
        self.name_entry = ttk.Entry(self.frame)
        self.name_entry.pack()

        ttk.Label(self.frame, text="Gender:").pack()
        self.gender_entry = ttk.Entry(self.frame)
        self.gender_entry.pack()

        ttk.Label(self.frame, text="Relation:").pack()
        self.relation_entry = ttk.Entry(self.frame)
        self.relation_entry.pack()

        ttk.Button(self.frame, text="Save", command=self.save_data).pack(pady=20)

    def save_data(self):
        name = self.name_entry.get()
        gender = self.gender_entry.get()
        relation = self.relation_entry.get()

        # Capture image from webcam
        # cap = cv2.VideoCapture("C:\\Users\\Heady\\Downloads\\home automation\\train_dataset_images\\Elon Musk.jpg")
        cap = cv2.VideoCapture('http://192.168.18.109:4747/video')

        ret, frame = cap.read()
        cap.release()

        frame_bytes = cv2.imencode('.jpg', frame)[1].tobytes()
        base64_img = base64.b64encode(frame_bytes)


        current_date_time = datetime.now()
        dt_string = current_date_time.strftime("%d/%m/%Y %H:%M:%S")

        # Save the data into MongoDB or perform any required action
        person_data = {
            "name": name,
            "gender": gender,
            "relation": relation,
            "time_stamp": dt_string,
            "person_image": base64_img
        }

        # Insert the data into MongoDB
        collection.insert_one(person_data)

        print("Data saved:")

        # self.label.config(text=f"Welcome, {name}!")
        self.root.after(2000, self.root.destroy)  # Close the app after 2 seconds

if __name__ == "__main__":
    root = tk.Tk()
    app = SecurityApp(root)
    root.mainloop()
