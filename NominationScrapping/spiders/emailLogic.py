import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def getUserName():
    gmail_user = 'hkpatel247@gmail.com'
    return gmail_user


def getPassword():
    gmail_password = 'Hlove$K247'
    return gmail_password


def getRecipients():
    to = ['harshitpatel24@gmail.com',"khushalipatel487@gmail.com"]
    return to


def getSubjectLine():
    subject = 'Important: OINP Update'
    return subject


def getMailBody():
    body = '<h3><b>Some update is there on site</b></h3><br/>Login Fast<br/><h4><a href="https://www.ontarioimmigration.gov.on.ca/oinp_index/resources/app/guest/index.html">Click to Login on OINP</a></h4>'
    return body


def getEmailText(smtpserver):
    for email in getRecipients():
        msg = MIMEMultipart()  # create a message
        message = getMailBody()
        # setup the parameters of the message
        msg['From'] = getUserName()
        msg['To'] = email
        msg['Subject'] = "Update Related to OINP"
        msg.attach(MIMEText(message, 'html'))
        smtpserver.send_message(msg)


def sendEmail():
    smtpserver = smtplib.SMTP(host='smtp.gmail.com', port=587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login(getUserName(), getPassword())
    getEmailText(smtpserver)
