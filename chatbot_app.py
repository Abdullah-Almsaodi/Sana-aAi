from flask import Flask, render_template, request
import json
import random
import tensorflow as tf

app = Flask(__name__)

# Load the trained model
best_model = tf.keras.models.load_model('chatbot/chatbot_model.h5')
print("Model loaded")

# Load the intents data
with open('chatbot/intents.json', 'r') as f:
    intents = json.load(f)
print("Intents loaded")

def chatbot_response(user_input):
    predicted_intent = best_model.predict([user_input])[0]
    print(f"Predicted intent: {predicted_intent}")

    for intent in intents['intents']:
        if intent['tag'] == predicted_intent:
            response = random.choice(intent['responses'])
            print(f"Response: {response}")
            break

    return response

@app.route('/')
def home():
    print("Home route accessed")
    return render_template('frontend\templates\base.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    print(f"User input: {user_input}")
    response = chatbot_response(user_input)
    return response

if __name__ == '__main__':
    app.run(debug=True)
    print("App started")