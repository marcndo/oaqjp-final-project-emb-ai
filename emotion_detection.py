""" This functions detect emotion from a text and brief on the 
authors current state
"""
import json
import requests

def emotion_detection(text_to_analyze):
    """classify emotions expressed in text """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, headers=headers, json=payload, timeout=10)
    return json.loads(response.text)


