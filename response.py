import pandas as pd
from collections import Counter

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
    patient4 = ['what', 'my', 'diet', 'today']

    # Caretakers
    caretaker1 = ["ben","what", "medications"]
    caretaker2 = ['Remind', "ben", "at", "exercise"]
    caretaker3 = ['ben', 'family', 'urgent']

    #doctor and Nurses
    nurdoc1 = ['what', 'blood', 'pressure', 'ben']
    nurdoc2 = ['latest', 'data', 'ben']
    nurdoc3 = ['report', 'ben', 'mail']
    nurdoc4 = ['ben', 'average', 'weight', 'days']

    if all(x in input_str for x in patient1):
        output_txt = "Your blood pressure was 132 Yesterday"
        return output_txt
    elif all(x in input_str for x in patient2):
        output_txt = "Caretaker John is scheduled to come at 10 AM today"
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
        if 'exercise' in input_words:
            indx_e = input_words.index('exercise')
            time_e = input_words[indx_e-1]
        else:
            time_e = ''
        if 'am'in input_words:
            indx = input_words.index('am')
            time = input_words[indx-1]
            output_txt = "Ben's Reminder is set for exercise at {} AM tomorrow".format(time_e, time)
        elif 'pm'in input_words:
            indx = input_words.index('pm')
            time = input_words[indx-1]
            output_txt = "Ben's Reminder is set for {} exercise at {} PM tomorrow".format(time_e, time)
        else:
            output_txt = "Ben's Reminder is set for {} exercise tomorrow".format(time_e)
        return output_txt
    elif all(x in input_str for x in caretaker3):
        output_txt = "Emergency message have been sent to the family members and the doctor. You will be transfered to a call with Doctor immediately."
        return output_txt
    elif any(x in input_str for x in nurdoc1):
        output_txt = "Bens latest blood pressure recorded was 132 Yesterday"
        return output_txt
    elif any(x in input_str for x in nurdoc2):
        output_txt = "Bens latest data as on 03/27/2017 7:00 PM:\
        \nBP = 122\
        \nHR = 72\
        \nWeight = 187 lb\
        \nBlood Sugar = 130"
        return output_txt
    elif any(x in input_str for x in nurdoc3):
        output_txt = "Bens latest blood pressure recorded was 132 Yesterday"
        return output_txt
    elif any(x in input_str for x in nurdoc4):
        output_txt = "Bens average weight over last 7 days in 189 lbs"
        return output_txt
    elif "hi" in input_str:
        return "Hi. Good afternoon, How can i help you today?"
    else:
        return "\
        Here are some things you can try:\
        \n1) Tell me something about part 2340582T23\
        \n2) what is hs code for washer\
        \n3) What is the HS code for part 1277M90G02\
        \n4) Charles, can i export crashplan to India ?\
        \n5) Tell me about something about part 00704-0845-0001\
        \n6) Things to know for export of model engine 7LM2500AA107G01\
        \n7) Provide me details for export of part 1275M68P01\
        \n8) Help me know details for export of drawing 1275M68\
        \n9) Tell me engine models where part 102A358P05 is used"
