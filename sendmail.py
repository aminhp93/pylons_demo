# import smtplib


# from datetime import datetime, timedelta

# import cryptography
# from cryptography.fernet import Fernet

# class ExpiringTokenGenerator:
#   FERNET_KEY = 'H-gvBa31So7ZWRlIleY7q5xYPIytGnRHRcBpRbASyao='
#   fernet = Fernet(FERNET_KEY)

#   DATE_FORMAT = '%Y-%m-%d %H-%M-%S'
#   EXPIRATION_DAYS = 3

#   def _get_time(self):
#     """Returns a string with the current UTC time"""
#     return datetime.utcnow().strftime(self.DATE_FORMAT)

#   def _parse_time(self, d):
#     """Parses a string produced by _get_time and returns a datetime object"""
#     return datetime.strptime(d, self.DATE_FORMAT)

#   def generate_token(self, text):
#     """Generates an encrypted token"""
#     full_text = text + '|' + self._get_time()
#     token = self.fernet.encrypt(bytes(full_text))

#     return token

#   def get_token_value(self, token):
#     """Gets a value from an encrypted token.
#     Returns None if the token is invalid or has expired.
#     """
#     try:
#       value = self.fernet.decrypt(bytes(token))
#       separator_pos = value.rfind('|')

#       text = value[: separator_pos]
#       token_time = self._parse_time(value[separator_pos + 1: ])
      
#       if token_time + timedelta(self.EXPIRATION_DAYS) < datetime.utcnow():
#         return None

#     except cryptography.fernet.InvalidToken:
#       return None

#     return text 

#   def is_valid_token(self, token):
#     return self.get_token_value(token) != None

# a = ExpiringTokenGenerator()
# a.generate_token("testss")
# print(a)#content = a

# mail = smtplib.SMTP('smtp.gmail.com', 587)

# mail.starttls()
# mail.login('minhpn.org.ec@gmail.com', 'miamikki521')
# mail.sendmail('minhpn.org.ec@gmail.com', 'minhpn@rikkeisoft.com', str(a))
# mail.close()


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
def py_mail(SUBJECT, BODY, TO, FROM):
    """With this function we send out our html email"""
 
    # Create message container - the correct MIME type is multipart/alternative here!
    MESSAGE = MIMEMultipart('alternative')
    MESSAGE['subject'] = SUBJECT
    MESSAGE['To'] = TO
    MESSAGE['From'] = FROM
    MESSAGE.preamble = """
Your mail reader does not support the report format.
Please visit us <a href="http://www.mysite.com">online</a>!"""
 
    # Record the MIME type text/html.
    HTML_BODY = MIMEText(BODY, 'html')
 
    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    MESSAGE.attach(HTML_BODY)
 
    # The actual sending of the e-mail
    server = smtplib.SMTP('smtp.gmail.com:587')
 
    # Print debugging output when testing
    if __name__ == "__main__":
        server.set_debuglevel(1)
 
    # Credentials (if needed) for sending the mail
    password = ""
 
    server.starttls()
    server.login(FROM,password)
    server.sendmail(FROM, [TO], MESSAGE.as_string())
    server.quit()
 
if __name__ == "__main__":
    """Executes if the script is run as main script (for testing purposes)"""
 
    email_content = """
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>html title</title>
  <style type="text/css" media="screen">
    table{
        background-color: #AAD373;
        empty-cells:hide;
    }
    td.cell{
        background-color: white;
    }
  </style>
</head>
<body>
  <table style="border: blue 1px solid;">
    <tr><td class="cell">Cell 1.1</td><td class="cell">Cell 1.2</td></tr>
    <tr><td class="cell">Cell 2.1</td><td class="cell"></td></tr>
  </table>
</body>
"""
 
    FROM = 'minhpn.org.ec@gmail.com'
    TO ='minhpn@rikkeisoft.com'
 
    py_mail("Test email subject", email_content, TO, FROM)