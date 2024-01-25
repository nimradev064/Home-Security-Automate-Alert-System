# Home Security Automation

 <p style="font-size: 10px; font-family: 'Arial', sans-serif;">Elevate your home security with our Tkinter Application, integrating facial detection to identify known persons stored in MongoDB and sending email alerts for unknown individuals.</p><br>
 <p style="font-size: 15px; font-family: 'Arial', sans-serif;"> Face detection uses computer vision to extract information from images to recognize human faces. In this project, we will learn how to create a Home Security Automation system using OpenCV Python. The input to the system will be in real-time via the webcam of the computer. The tkinter package (“Tk interface”) is the standard Python interface to the Tcl/Tk GUI toolkit. Both Tk and tkinter are available on most Unix platforms, including macOS, as well as on Windows systems.Embark on a Python project that seamlessly captures webcam images through Tkinter's user-friendly GUI toolkit. The interface, adorned with intuitive buttons labeled "Known" and "Unknown," empowers users to swiftly categorize detected faces. In the event of an unfamiliar visage, the user is prompted to furnish details, enriching our MongoDB database with newfound information.</p><br>
<p style="font-size: 15px; font-family: 'Arial', sans-serif;">For known faces, a simple click on the "Known" button ensures efficient data storage within MongoDB. However, when faced with an unknown persona, our vigilant system dynamically dispatches the captured image to the user's email, accompanied by a thoughtful alert message. This elegant integration of Tkinter's GUI prowess, MongoDB's robust data handling, and email notifications elevates the project into a seamless orchestration of user interaction, facial recognition, and efficient data management. Brace yourself for an immersive journey, navigating the intricacies of GUI-based image capture and intelligent data handling.</p><br> 

### Built With

![Python] ![OpenCV]

# Getting Started

### Prerequisites

* Python 3.11.6

### Installation  
<br> 
#### Windows  
  
1. `git clone https://github.com/nimradev064/Home-Security-Automation.git`  
2. `python -m venv venv`  
3. `.\venv\scripts\activate.bat`  
##### ENV Packages:  
4.  `pip install -r ./requirements.txt`

#### Linux  
  
1. `git clone https://github.com/nimradev064/Home-Security-Automation.git`  
2. `python3 -m venv venv`  
3. `source venv/bin/activate`
##### ENV Packages:  
4. `pip3 install -r requirements.txt`


### Run the program

`python main.py`

