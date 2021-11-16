from flask import Flask, render_template, request
from pyngrok import ngrok
from chatgui import *
from flask import jsonify
import nltk
nltk.download('punkt')
nltk.download('wordnet')

app = Flask(__name__)
public_url = ngrok.connect(5000).public_url
@app.route("/")
    return render_template('homepage.html')


@app.route('/chatbot', methods=["GET", "POST"])
def chatbotResponse():
    if request.method == 'POST':
        the_question = request.form['question']
        response = chatbot_response(the_question)
        return jsonify({"response": response })



if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)