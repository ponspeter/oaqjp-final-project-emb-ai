import requests
import json

def emotion_detector(text_to_analyze):
    # URL of the emotion predict service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Custom header specifying the model ID for the emotion predict service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Sending a POST request to the emotion analysis API
    response = requests.post(url, json=myobj, headers=header)
    
    # get the status code
    status_code = response.status_code
    print(status_code)

    if status_code == 400:
        return_response = { 'anger': None,
                             'disgust': None,
                             'fear': None,
                             'joy': None,
                             'sadness': None,
                             'dominant_emotion': None }
    else:
        # format the response
        formatted_response = json.loads(response.text)

        # extract the emotion predictions
        return_response = formatted_response['emotionPredictions'][0]['emotion']

        # get the dominant emotio
        dominant_emotion = max(return_response, key = lambda x: return_response[x])

        # add dominant_emotion in the return response
        return_response['dominant_emotion'] = dominant_emotion

    #  return response
    return return_response

    

    
    