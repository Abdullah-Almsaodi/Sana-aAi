import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
import pickle
import nltk
from nltk.stem import WordNetLemmatizer
import json

nltk.download('punkt')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

def load_preprocessed_data():
    words = pickle.load(open('chatbot/words.pkl', 'rb'))
    classes = pickle.load(open('chatbot/classes.pkl', 'rb'))
    return words, classes

def load_trained_model():
    model = load_model('chatbot/chatbot_model.h5')
    return model

def predict_class(message, model, words, classes):
    word_list = nltk.word_tokenize(message)
    word_list = [lemmatizer.lemmatize(word.lower()) for word in word_list]

    bag = [0] * len(words)
    for w in word_list:
        if w in words:
            bag[words.index(w)] = 1

    input_array = np.array(bag).reshape(1, -1)
    predictions = model.predict(input_array)
    predicted_class_index = np.argmax(predictions)
    predicted_class = classes[predicted_class_index]
    
    return predicted_class

def get_response(predicted_class, intents):
    for intent in intents['intents']:
        if intent['tag'] == predicted_class:
            responses = intent['responses']
            return np.random.choice(responses)
    return "I'm sorry, I didn't understand that."
