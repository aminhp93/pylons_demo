import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
def send_mail(SUBJECT, BODY, TO, FROM):
	
	MESSAGE = MIMEMultipart('alternative')
	MESSAGE['subject'] = SUBJECT
	MESSAGE['To'] = TO
	MESSAGE['From'] = FROM
 
	HTML_BODY = MIMEText(BODY, 'html')
 
	MESSAGE.attach(HTML_BODY)
 
	server = smtplib.SMTP('smtp.gmail.com:587')
 
	if __name__ == "__main__":
		server.set_debuglevel(1)
 
	password = "miamikki521"
 
	server.starttls()
	server.login(FROM,password)
	server.sendmail(FROM, [TO], MESSAGE.as_string())
	server.quit()