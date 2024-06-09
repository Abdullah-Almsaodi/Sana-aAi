import numpy as np
import random
import pickle
import json
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import SGD

# Set GPU device memory growth
physical_devices = tf.config.list_physical_devices('GPU')
if physical_devices:
    try:
        # TensorFlow >= 2.3
        for gpu in physical_devices:
            tf.config.experimental.set_memory_growth(gpu, True)
        print("GPU memory growth set successfully")
    except:
        # Invalid device or cannot modify virtual devices once initialized.
        print("Cannot set GPU memory growth")

# Generate and save training data
def generate_training_data():
    # Generate your training data here
    # Example:
    training_data = [...]  # Your generated training data
    with open('training_data.pkl', 'wb') as f:
        pickle.dump(training_data, f)

# Load preprocessed data
def load_data():
    import nltk
    from nltk.stem import WordNetLemmatizer
    
    nltk.download('punkt')
    nltk.download('wordnet')
    
    lemmatizer = WordNetLemmatizer()
    
    words = pickle.load(open('words.pkl', 'rb'))
    classes = pickle.load(open('classes.pkl', 'rb'))
    training_data = pickle.load(open('training_data.pkl', 'rb'))
    random.shuffle(training_data)
    
    train_x, train_y = [], []
    for pattern, tag in training_data:
        # Create bag of words
        bag = [0] * len(words)
        for w in pattern:
            w = lemmatizer.lemmatize(w.lower())
            if w in words:
                bag[words.index(w)] = 1
        train_x.append(bag)
        
        # One-hot encode the tag
        label = classes.index(tag)
        train_y.append([1 if i == label else 0 for i in range(len(classes))])  # One-hot encoding
    
    return np.array(train_x), np.array(train_y), words, classes



# Build the model
def build_model(train_x, train_y):
    model = Sequential()
    model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(len(train_y[0]), activation='softmax'))
    return model

# Compile model
def compile_model(model):
    sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
    model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

# Fit the model
def fit_model(model, train_x, train_y):
    early_stopping = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=5)
    model.fit(train_x, train_y, epochs=200, batch_size=5, verbose=1, validation_split=0.2, callbacks=[early_stopping])

# Save the model
def save_model(model, words, classes):
    model.save('chatbot_model.h5')
    model_json = model.to_json()
    with open("model.json", "w") as json_file:
        json_file.write(model_json)
    with open('words.pkl', 'wb') as f:
        pickle.dump(words, f)
    with open('classes.pkl', 'wb') as f:
        pickle.dump(classes, f)

# Load data
train_x, train_y, words, classes = load_data()

# Build the model
model = build_model(train_x, train_y)

# Compile model
compile_model(model)

# Fit the model
fit_model(model, train_x, train_y)

# Save the model
save_model(model, words, classes)
print("Model created and saved successfully!")
