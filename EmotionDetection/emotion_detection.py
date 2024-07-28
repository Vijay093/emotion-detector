import requests
import json

def emotion_detector(text_to_analyze): # Define a function named emotion detector that takes string input
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } } 
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    formattedResponse = json.loads(response.text)
    result = {}
    if response.status_code == 200:
        result = formattedResponse['emotionPredictions'][0]['emotion']
        result['dominant_emotion'] = max(result, key=result.get)
    elif response.status_code == 400:
        result['dominant_emotion'] = None

    return result

         