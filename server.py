""" rout users requests to the appropriate pages
"""

from flask import Flask, request, render_template, jsonify

app = Flask("Emotion Detector")

@app.rout("/emotionDetector", methods='POST')
def emotion_detect():
    """ Routes users to emotion detection page
    """
    text_to_analyze = request.form['text']
    result = emotion_detector(text_to_analyze)
    if result:
        return jsonify(result)
    else:
        return jsonify(f'failed to analyze emotion: {}')
