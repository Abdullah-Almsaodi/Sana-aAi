import nltk
from nltk.stem import WordNetLemmatizer
import json
import pickle

nltk.download('punkt')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

words = []
classes = []
documents = []
ignore_words = ['?', '!']

# Load intents from JSON file
data_file = open('intents.json').read()
intents = json.loads(data_file)

# Preprocess data
for intent in intents['intents']:
    for pattern in intent['patterns']:
        # Tokenize each word
        w = nltk.word_tokenize(pattern)
        words.extend(w)
        # Add documents to the corpus
        documents.append((w, intent['tag']))

        # Add to our classes list
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

# Lemmatize, lower each word, and remove duplicates
words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
words = sorted(list(set(words)))
classes = sorted(list(set(classes)))

# Save preprocessed data
def save_preprocessed_data():
    pickle.dump(words, open('words.pkl', 'wb'))
    pickle.dump(classes, open('classes.pkl', 'wb'))
    pickle.dump(documents, open('training_data.pkl', 'wb'))

# Save preprocessed data
save_preprocessed_data()
