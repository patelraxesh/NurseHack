from twilio import twiml
import nltk
from flask import Flask, request
import urllib2
from twilio.rest import TwilioRestClient
import requests
import pandas as pd
from collections import Counter
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
import smtplib

ACCOUNT_SID = "ACa7be370a093da413ffc38778e5365171" 
AUTH_TOKEN = "cf96f1247b96d64852db5f3c0db16175"
TWILIO_NUMBER = '+17819718068'

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
app = Flask(__name__)

@app.route("/")
def hello():
	out_text = "Hi, How can i help you ?"
	response = twiml.Response()
	response.message(out_text)
	return str(response)

@app.route("/sms", methods=['POST'])
def nursechat():
	in_text = request.form["Body"]
	ph_number = request.form["From"]
	in_text = in_text.lower()
	out_text = get_response(in_text)
	response = twiml.Response()
	response.message(out_text)
	return str(response)

@app.route('/call', methods=['POST'])
def call():
    # Make an outbound call to the provided number from your Twilio number
    call = client.calls.create(to='+18574520056', from_=TWILIO_NUMBER, 
                               url="http://demo.twilio.com/docs/voice.xml")

    # Return a message indicating the call is coming
    return 'Call coming in!'


def send_mail():
	msg = MIMEMultipart()
	msg['From'] = 'raxeshp1991@gmail.com'
	msg['To'] = 'raxesh4you@gmail.com'
	msg['Subject'] = "BENS REPORT"
	msg.attach(MIMEText(file("sample.pdf").read()))
	output_txt = "Bens latest data as on 03/27/2017 7:00 PM:\
        \nBP = 122\
        \nHR = 72\
        \nWeight = 187 lb\
        \nBlood Sugar = 130"
	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.starttls()
	s.login('raxeshp1991@gmail.com','sahajanand')
	s.sendmail('raxeshp1991@gmail.com',['raxesh4you@gmail.com'], output_txt)
	s.quit()

def get_response(input_str):
    '''
    Get the response output from input
    '''
    input_str = input_str.lower()
    input_words = input_str.split()

    # patients
    patient1 = ['my','blood','pressure']
    patient2 = ['when', "my",'caretaker','coming']
    patient3 = ['when', 'my', 'appointment', 'doctor']
    patient4 = ['my', 'diet', 'today']
    patient5 = ['mayday']

    # Caretakers
    caretaker = ['login', 'caretaker']
    caretaker1 = ["ben","what", "medication"]
    caretaker2 = ['remind', "ben", "at", "exercises"]
    caretaker3 = ['ben', 'family', 'urgent']

    #doctor and Nurses
    nurdoc1 = ['what', 'blood', 'pressure', 'ben']
    nurdoc2 = ['latest', 'data', 'ben']
    nurdoc3 = ['report', 'ben', 'mail']
    nurdoc4 = ['ben', 'average', 'weight']

    whoisthis = ['who', 'is', 'this']

    if all(x in input_str for x in patient1):
        output_txt = "Your blood pressure was 132 Yesterday"
        return output_txt
    elif all(x in input_str for x in patient2):
        output_txt = "Caretaker John is scheduled to come at 10 AM today"
        return output_txt
    elif all(x in input_str for x in caretaker):
        output_txt = "Now you are logged in as a Caretaker"
        return output_txt
    elif all(x in input_str for x in patient3):
        output_txt = "Your Next appointment with doctor Meleis is on Monday, 27th March at 4 PM"
        return output_txt
    elif all(x in input_str for x in patient4):
        output_txt = "As per your medical record, it is found that you have high cholestrol. So you should avoid Oil and can have any of the following food : Oat, Salad, cucumber etc."
        return output_txt
    elif all(x in input_str for x in caretaker1):
        output_txt = "Ben is scheduled to receive 1 tablet of Tamoxifen everyday at 9:00 PM"
        return output_txt
    elif all(x in input_str for x in caretaker2):
        output_txt = "Ben's Reminder is set for leg exercise tomorrow at 7 AM".format(time_e)
        return output_txt
    elif all(x in input_str for x in caretaker3):
        output_txt = "Emergency message have been sent to the family members and the doctor. You will be transfered to a call with Doctor immediately."
        new_msg = call()
        return output_txt
    elif all(x in input_str for x in nurdoc1):
        output_txt = "Bens latest blood pressure recorded was 132 Yesterday"
        return output_txt
    elif all(x in input_str for x in nurdoc2):
        output_txt = "Bens latest data as on 03/27/2017 7:00 PM:\
        \nBP = 122\
        \nHR = 72\
        \nWeight = 187 lb\
        \nBlood Sugar = 130"
        return output_txt
    elif all(x in input_str for x in nurdoc3):
        output_txt = "Bens report is sent at raxesh4you@gmail.com"
        send_mail()
        return output_txt
    elif all(x in input_str for x in nurdoc4):
        output_txt = "Bens average weight over last 7 days in 189 lbs"
        return output_txt
    elif ('mayday' in input_str):
    	output_txt = "Hold on.. you will receive a call immediately"
    	new_msg = call()
        return output_txt
    elif all(x in input_str for x in whoisthis):
        return "This is QkChat, your personal assistant."
    elif "hi" in input_str:
        return "Hi. Good afternoon, How can i help you today?"
    elif 'help' in input_str:
        return "\
        Here are some things you can try:\
        \n1) What was my blood pressure yesterday ?\
        \n2) When is the caretaker coming ?\
        \n3) When is my next appointment with the doctor ?\
        \n4) Whats in my diet plan for today ?\
        \n5) What are Bens medications ?\
        \n6) Remind Ben to do leg exercise tomorrow at 7 AM\
        \n7) What is the latest blood pressure reading for Ben\
        \n8) Get me the latest data of Ben\
		\n9) Mail me the detailed report of Ben\
        \n10) Contact Bens family urgently"
    else:
        return "\
        Here are some things you can try:\
        \n1) What was my blood pressure yesterday ?\
        \n2) When is the caretaker coming ?\
        \n3) When is my next appointment with the doctor ?\
        \n4) Whats in my diet plan for today ?\
        \n5) What are Bens medications ?\
        \n6) Remind Ben to do leg exercise tomorrow at 7 AM\
        \n7) What is the latest blood pressure reading for Ben\
        \n8) Get me the latest data of Ben\
		\n9) Mail me the detailed report of Ben\
        \n10) Contact Bens family urgently"

if __name__ == "__main__":
	app.run(debug=True)