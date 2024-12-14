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
    
