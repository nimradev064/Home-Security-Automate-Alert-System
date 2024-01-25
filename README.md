# Home Security Automation

 <p style="font-size: 10px; font-family: 'Arial', sans-serif;">Elevate your home security with our Tkinter Application, integrating facial detection to identify known persons stored in MongoDB and sending email alerts for unknown individuals.</p><br>
 <p style="font-size: 10px; font-family: 'Arial', sans-serif;"> Face detection uses computer vision to extract information from images to recognize human faces. In this project, we will learn how to create a Home Security Automation system using OpenCV Python. The input to the system will be in real-time via the webcam of the computer. The tkinter package (“Tk interface”) is the standard Python interface to the Tcl/Tk GUI toolkit. Both Tk and tkinter are available on most Unix platforms, including macOS, as well as on Windows systems.Embark on a Python project that seamlessly captures webcam images through Tkinter's user-friendly GUI toolkit. The interface, adorned with intuitive buttons labeled "Known" and "Unknown," empowers users to swiftly categorize detected faces. In the event of an unfamiliar visage, the user is prompted to furnish details, enriching our MongoDB database with newfound information.</p><br>
<p style="font-size: 10px; font-family: 'Arial', sans-serif;">For known faces, a simple click on the "Known" button ensures efficient data storage within MongoDB. However, when faced with an unknown persona, our vigilant system dynamically dispatches the captured image to the user's email, accompanied by a thoughtful alert message. This elegant integration of Tkinter's GUI prowess, MongoDB's robust data handling, and email notifications elevates the project into a seamless orchestration of user interaction, facial recognition, and efficient data management. Brace yourself for an immersive journey, navigating the intricacies of GUI-based image capture and intelligent data handling.</p><br> 

### Built With

![Python]  ![OpenCV] 

# Getting Started

### Prerequisites

* Python 3.11.6

### Installation  

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

### Application Demo 

1. Run App.
    <br>

   `python main.py`
 <br>
   
![image](https://github.com/nimradev064/Home-Security-Automation/assets/157350960/eafbc237-7ed6-4c7f-896b-a88f894da4fc)


 <br>
 
2. Detect the Face from Webcam and Checking for unauthorized or authorized person.<br>


   ![image](https://github.com/nimradev064/Home-Security-Automation/assets/157350960/ef814eb1-b288-42e1-a46f-f533016f6683)
   
<br>

3. For unknown person, the alert email notification is sent to the user. <br>

   ![image](https://github.com/nimradev064/Home-Security-Automation/assets/157350960/3f70f381-c27a-405a-9138-2082c2366547)

<br>
   
#### Alert notification being sent: <br>
Output of the notification process:  <br>
   ![image](https://github.com/nimradev064/Home-Security-Automation/assets/157350960/2d867712-fc99-40b1-a9b8-4733d502bfee)
Email received result: <br>
![image](https://github.com/nimradev064/Home-Security-Automation/assets/157350960/3ff115e6-b99d-4689-9088-d84d279e2810)

<br>
4. For known person : <br>
The system asks user to enter further detail of the entered person. <br>
![image](https://github.com/nimradev064/Home-Security-Automation/assets/157350960/0f9131d8-8356-495c-8147-6acb3f07a5c3)
<br>
Input screen for person data <br>
![image](https://github.com/nimradev064/Home-Security-Automation/assets/157350960/67ebac29-a895-4857-9010-e08b4733bd9d)
<br>
Process output in the command line <br>
![image](https://github.com/nimradev064/Home-Security-Automation/assets/157350960/79c3ae5d-3779-4d27-960c-033cec82304a)
<br>
Known Person Data is entered into the database <br>
![image](https://github.com/nimradev064/Home-Security-Automation/assets/157350960/33645fbe-fa99-472d-8ae5-0fa5c017a526)












   


