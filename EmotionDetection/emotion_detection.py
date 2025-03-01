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
    
    # Check if the response is valid
    if response.status_code == 200:
        # Format the response
        formatted_response = response.json()
        
        # Extract emotion scores
        emotions = formatted_response.get('emotionPredictions', [{}])[0].get('emotion', {})
        
        # Ensure all emotions exist in the response, defaulting to 0 if missing
        dominant_emotion = max(emotions, key=emotions.get, default="none")
        ordered_response = {
            "anger": emotions.get("anger"),
            "disgust": emotions.get("disgust"),
            "fear": emotions.get("fear"),
            "joy": emotions.get("joy"),
            "sadness": emotions.get("sadness"),
        }
        
        # Add dominant emotion at the end
        ordered_response["dominant_emotion"] = dominant_emotion
        
        return ordered_response
    elif response.status_code == 400:
        
        ordered_response = {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
        }
        
        # Add dominant emotion at the end
        ordered_response["dominant_emotion"] = None
        
        return ordered_response

    
    