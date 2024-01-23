import smtplib
import mimetypes
from email.message import EmailMessage

class EmailNotification:
     def __init__(self, sender,password, receiver,subject,body,img):
        self.sender= sender
        self.password = password
        self.receiver= receiver        
        self.subject= subject
        self.body= body
        self.img = img
     def emailfunc(self):  
        em = EmailMessage()
        em['From'] = self.sender
        em['To'] = self.receiver
        em['Subject'] = self.subject
        em.set_content(self.body)
        mime_type, _ = mimetypes.guess_type(self.img)
        mime_type, mime_subtype = mime_type.split('/')
        with open(self.img, 'rb') as file:
           em.add_attachment(file.read(),
           maintype=mime_type,
           subtype=mime_subtype,
           filename=self.img)

      #   print(em)  
        mail_server = smtplib.SMTP_SSL('smtp.gmail.com')
        mail_server.set_debuglevel(1)
        mail_server.login(self.sender, self.password)
        mail_server.send_message(em)
        mail_server.quit()
        
        print("Email sent")
       
                    
                                           