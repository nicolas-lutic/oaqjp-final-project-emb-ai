"""Module for detecting emotions in text using Watson NLP API."""

import requests
import json


def emotion_detector(text_to_analyse):
    """Detect emotions in the given text using Watson NLP Emotion API.

    Args:
        text_to_analyse (str): The text to analyze for emotions.

    Returns:
        dict: A dictionary containing emotion scores and the dominant emotion.
    """
    url = (
        'https://sn-watson-emotion.labs.skills.network/v1/'
        'watson.runtime.nlp.v1/NlpService/EmotionPredict'
    )
    myobj = {"raw_document": {"text": text_to_analyse}}
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    response = requests.post(url, json=myobj, headers=header)

    # If status code is 400, return all None values
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # If status code is 200, parse and return emotion scores
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        emotions = formatted_response['emotionPredictions'][0]['emotion']

        emotion_scores = {
            'anger': emotions['anger'],
            'disgust': emotions['disgust'],
            'fear': emotions['fear'],
            'joy': emotions['joy'],
            'sadness': emotions['sadness']
        }

        dominant_emotion = max(emotion_scores, key=emotion_scores.get)

        return {**emotion_scores, 'dominant_emotion': dominant_emotion}

    # For any other unexpected status codes, return all None values
    return {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
    }