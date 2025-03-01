"""
This module provides an emotion detection function that sends text input
to an external API and returns the predicted emotions with a dominant emotion.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """
    API endpoint to perform emotion detection on input text.
    
    Returns:
        str or dict: A message indicating invalid input or a JSON response with emotion scores.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        response_text = "Invalid Input! Please try again."
    else:
        response_text = f"For the given statement, the system response is 'anger': \
                        {response['anger']}, 'disgust': {response['disgust']}, \
                        'fear': {response['fear']}, 'joy': {response['joy']}, \
                        'sadness': {response['sadness']}. The dominant emotion is \
                        {response['dominant_emotion']}."

    return response_text

@app.route("/")
def render_index_page():
    """
    Renders the index page for the web application.
    
    Returns:
        str: Rendered HTML page.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
