from flask import Flask, request, jsonify
import os
import nltk
from nltk.stem import WordNetLemmatizer
import pickle
import numpy as np
from keras.models import load_model
import json
import random

app = Flask(__name__)


# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Specify absolute paths to the required files
words_path = os.path.join(script_dir, 'words.pkl')
classes_path = os.path.join(script_dir, 'classes.pkl')
model_path = os.path.join(script_dir, 'chatbot_model.h5')
intents_path = os.path.join(script_dir, 'intents.json')

# Load preprocessed data
words = pickle.load(open(words_path, 'rb'))
classes = pickle.load(open(classes_path, 'rb'))

# Load the model
model = load_model(model_path)

# Load intents
intents = json.loads(open(intents_path).read())

lemmatizer = WordNetLemmatizer()

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def bow(sentence, words, show_details=True):
    sentence_words = clean_up_sentence(sentence)
    bag = [0]*len(words) 
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s: 
                bag[i] = 1
                if show_details:
                    print("found in bag: %s" % w)
    return(np.array(bag))

def predict_class(sentence, model):
    p = bow(sentence, words, show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

def get_response(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result

def chatbot_response(text):
    ints = predict_class(text, model)
    res = get_response(ints, intents)
    return res

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data['message']
    response = chatbot_response(message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
