"""
19 - Natural Language Processing Basics

Learn:
- Text preprocessing
- Tokenization
- Text vectorization
- Simple text classification
"""

import tensorflow as tf
from tensorflow import keras


texts = [
    "I love this product",
    "This product is excellent",
    "Amazing experience",
    "I really like it",
    "I hate this product",
    "This is terrible",
    "Very bad experience",
    "I do not like it"
]

labels = [
    1,
    1,
    1,
    1,
    0,
    0,
    0,
    0
]


# Text vectorization
vectorizer = keras.layers.TextVectorization(
    max_tokens=1000,
    output_mode="int",
    output_sequence_length=10
)

vectorizer.adapt(texts)


# Convert text to numerical sequences
X = vectorizer(
    tf.constant(texts)
)

y = tf.constant(labels)


print("Vocabulary:")
print(vectorizer.get_vocabulary())

print("\nVectorized Text:")
print(X)


# Simple NLP model
model = keras.Sequential([
    keras.layers.Embedding(
        input_dim=1000,
        output_dim=16
    ),

    keras.layers.GlobalAveragePooling1D(),

    keras.layers.Dense(
        16,
        activation="relu"
    ),

    keras.layers.Dense(
        1,
        activation="sigmoid"
    )
])


model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)


# Train
model.fit(
    X,
    y,
    epochs=30,
    verbose=0
)


# Test
new_text = [
    "This product is amazing"
]

new_text_vectorized = vectorizer(
    tf.constant(new_text)
)

prediction = model.predict(
    new_text_vectorized,
    verbose=0
)[0][0]


print("\nPrediction Probability:", prediction)

if prediction >= 0.5:
    print("Prediction: Positive")
else:
    print("Prediction: Negative")
