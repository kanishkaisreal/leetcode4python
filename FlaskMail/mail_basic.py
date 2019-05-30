from flask import Flask
from flask_mail import Mail, Message
import os

app = Flask(__name__)

mail_settings = {
"MAIL_SERVER": 'smtp.gmail.com', 
    "MAIL_USE_TLS": False, #Transport Layer Security
    "MAIL_USE_SSL": True,  #Secure Sockets Layer
    "MAIL_PORT": 465, 		 #For using SSL
    "MAIL_USERNAME": 'kanishkaugee@gmail.com',
    "MAIL_PASSWORD": 'cnvxxwgxggxultfz'
    }
app.config.update(mail_settings)
mail = Mail(app)

if __name__ == '__main__':
	with app.app_context():
		msg = Message(sender=app.config.get("MAIL_USERNAME"),recipients=["kanishkaugee@gmail.com"])
		msg.subject = " Hello "
		msg.html =  """This is Awesome"""
		mail.send(msg)

