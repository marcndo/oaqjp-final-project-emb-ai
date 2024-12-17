"""router file for emotion detection
"""
from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector 

app = Flask("Emotion Detector")
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def emotion_detect():
    text_to_analyze = request.args.get("textToAnalyze", "")
    logging.debug(f"Text to analyze: {text_to_analyze}")
    
    # Handle blank entries
    if not text_to_analyze.strip():
        result = {
            "text": text_to_analyze,
            "emotions": {
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
            },
            "dominant_emotion": None
        }
        return jsonify(result), 400

    result = emotion_detector(text_to_analyze)
    try:
        if result and result["dominant_emotion"] is not None:
            emotions = result["emotions"]
            response_message = (
                f"For the given statement, the system response is "
                f"'anger': {emotions['anger']}, 'disgust': {emotions['disgust']}, "
                f"'fear': {emotions['fear']}, 'joy': {emotions['joy']} and 'sadness': {emotions['sadness']}. "
                f"The dominant emotion is {result['dominant_emotion']}."
            )
            return jsonify({"message": response_message})
        else:
            return jsonify({"error": "Invalid text! Please try again."}), 400
    except KeyError as e:
        logging.error(f"Missing key in result: {e}")
        return jsonify({"error": f"Missing key in result: {e}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)



