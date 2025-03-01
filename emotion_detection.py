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

    # format the response
    formatted_response = json.loads(response.text)

    # Extract emotion scores
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    # Determine the dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Construct the final response
    final_response = {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "dominant_emotion": dominant_emotion
    }
    
    # Returning a final response containing emotion predict results
    return final_response