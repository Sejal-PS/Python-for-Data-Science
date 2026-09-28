"""
Project: Basic Sentiment Analysis(NLP beginner level project)

This beginner project demonstrates simple
rule-based sentiment analysis.

Skills:
- Text Processing
- Strings
- Lists
- Dictionaries
- Basic NLP concepts
"""

import re


# --------------------------------------------------
# Sample Reviews
# --------------------------------------------------

reviews = [
    "This product is excellent and amazing",
    "The service was good and helpful",
    "I love this product",
    "This was bad and disappointing",
    "The product is terrible",
    "The service was okay"
]


# --------------------------------------------------
# Sentiment Words
# --------------------------------------------------

positive_words = {
    "excellent",
    "amazing",
    "good",
    "helpful",
    "love",
    "great",
    "happy"
}

negative_words = {
    "bad",
    "terrible",
    "disappointing",
    "poor",
    "hate",
    "worst"
}


# --------------------------------------------------
# Sentiment Function
# --------------------------------------------------

def analyze_sentiment(text):

    words = re.findall(
        r"\b[a-zA-Z]+\b",
        text.lower()
    )

    positive_count = sum(
        word in positive_words
        for word in words
    )

    negative_count = sum(
        word in negative_words
        for word in words
    )

    if positive_count > negative_count:
        return "Positive"

    if negative_count > positive_count:
        return "Negative"

    return "Neutral"


# --------------------------------------------------
# Analyze Reviews
# --------------------------------------------------

for review in reviews:

    sentiment = analyze_sentiment(
        review
    )

    print(
        f"Review: {review}"
    )

    print(
        f"Sentiment: {sentiment}\n"
    )


# --------------------------------------------------
# Practice
# --------------------------------------------------

# 1. Add more positive words.
# 2. Add more negative words.
# 3. Add your own reviews.
# 4. Count positive and negative reviews.
# 5. Calculate the percentage of each sentiment.
