'''
Module that runs the Flask Server
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    '''
    Accepts text to run against Emotion Detector
    '''
    text_to_detect = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_detect)
    if response['dominant_emotion'] is not None:
        dominant = response['dominant_emotion']
        del response['dominant_emotion']
        return f"For given statement,system response {response}.The dominant emotion is {dominant}."
    return "Invalid text! Please enter again."

@app.route("/")
def render_index_page():
    '''
    Renders Main Index.html Page
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(port=5000, debug = True)
