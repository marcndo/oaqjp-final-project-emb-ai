""" This function classifies emotions expressed in text and briefs on the
authors current state
"""
import requests
import json

def emotion_detector(text_to_analyze):
    """Classify emotions expressed in text.
    Parameters:
        text_to_analyze: str
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    doc = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(url, headers=headers, json=doc, timeout=10)
    
    # Extract required 
    response_dict = json.loads(response.text)
    emotions = response_dict.get("emotionPredictions", [{}])[0].get("emotion", {}) 
    required_emotions = { "anger": emotions.get("anger", 0), 
    "disgust": emotions.get("disgust", 0), 
    "fear": emotions.get("fear", 0), 
    "joy": emotions.get("joy", 0), 
    "sadness": emotions.get("sadness", 0) } 

    # Find the dominant emotion 
    dominant_emotion = max(required_emotions, key=required_emotions.get) 
    output = { "text": text_to_analyze, "emotions": required_emotions, "dominant_emotion": dominant_emotion } 

    return output
