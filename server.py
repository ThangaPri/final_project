"""Module import the request library."""
from flask import Flask,render_template,request
from EmotionDetection.emotion_detection import emotion_detector

app=Flask(__name__,template_folder='templates')

#app decorator for displaying home page
@app.route("/")
def render_index_page():
    ' ' 'Demonstrates rendering the home page' ' ' 
    return render_template("index.html")

#app decorator for displaying content after clicked on Runsentimentanalysis button
@app.route("/emotionDetector")
def detect_emotion():
    ' ' 'Demonstrates rendering the result after click of Runsentimentanalysis button' ' ' 
    text_find_emotion = request.args.get('textToAnalyze')
    response = emotion_detector(text_find_emotion)
    #Save the emotions from response to variable
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    if anger is not None:
        return f"For the given statement, the system response is 'anger': {anger},\
        'disgust':{disgust}, 'fear':{fear}, 'joy':{joy} \
        and 'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    return " Invalid text! Please try again!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5560,debug=True)
