"""Module import the request library."""
# Import the requests library to handle HTTP requests
import requests,json

' ' 'Demonstrates the extracting the finer emotions like joy' ' ' 
# Define a function named emotion_detector that takes a string input (text_to_analyse)
def emotion_detector(text_to_analyze):
    # URL of the emotion_detector
    url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create a dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = myobj, headers=header)

    #format the response
    
    formatted_response=json.loads(response.text)

    #Extract required set if emotionns
    anger   =   formatted_response['emotionPredictions'][0]['emotion']['anger']

    disgust =   formatted_response['emotionPredictions'][0]['emotion']['disgust']

    fear    =   formatted_response['emotionPredictions'][0]['emotion']['fear']

    joy     =   formatted_response['emotionPredictions'][0]['emotion']['joy']

    sadness =   formatted_response['emotionPredictions'][0]['emotion']['sadness']
    

    #logic to find dominant emotion which has highest score
    emotions    =   {'anger': anger, 'disgust': disgust,'fear': fear,'joy': joy,'sadness': sadness}

    dominant_emotion    =   max(emotions, key= lambda x: emotions[x])
    
    #return the result as outout
    return {'anger': anger, 'disgust': disgust,'fear': fear,'joy': joy,'sadness': sadness,'dominant_emotion':dominant_emotion}

    


