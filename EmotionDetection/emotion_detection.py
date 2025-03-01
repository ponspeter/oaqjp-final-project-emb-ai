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
    if response.status_code != 200:
        return {"error": "Failed to fetch emotion data"}
    
    # Format the response
    formatted_response = response.json()
    
    # Extract emotion scores
    emotions = formatted_response.get('emotionPredictions', [{}])[0].get('emotion', {})
    
    # Ensure all emotions exist in the response, defaulting to 0 if missing
    dominant_emotion = max(emotions, key=emotions.get, default="none")
    ordered_response = {
        "anger": emotions.get("anger", 0.0),
        "disgust": emotions.get("disgust", 0.0),
        "fear": emotions.get("fear", 0.0),
        "joy": emotions.get("joy", 0.0),
        "sadness": emotions.get("sadness", 0.0),
    }
    
    # Add dominant emotion at the end
    ordered_response["dominant_emotion"] = dominant_emotion
    
    return ordered_response