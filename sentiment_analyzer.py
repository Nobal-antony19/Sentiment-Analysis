from textblob import TextBlob

def analyze_sentiment(text):
    """
    Analyzes the sentiment of a given text and returns 'Positive', 'Negative', or 'Neutral'.
    """
    analysis = TextBlob(text)
    # Polarity ranges from -1 (negative) to 1 (positive)
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

if __name__ == "__main__":
    # Example usage with a single text
    text1 = "This is an absolutely wonderful day!"
    print(f"'{text1}' is: {analyze_sentiment(text1)}")

    text2 = "I really dislike this situation, it's terrible."
    print(f"'{text2}' is: {analyze_sentiment(text2)}")

    text3 = "The car is blue."
    print(f"'{text3}' is: {analyze_sentiment(text3)}")