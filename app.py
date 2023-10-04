# Import necessary libraries
from flask import Flask, render_template, request
from google.cloud import language_v1

# Initialize Flask app
app = Flask(__name__)

# Configure the Natural Language API client
client = language_v1.LanguageServiceClient.from_service_account_json('/Users/harshitajogi/Desktop/CC_LAB/EXP_5/ccexpt4-401009-f3e46f6e1a10.json')

# Define the home route
@app.route('/')
def home():
    return render_template('index.html')

# Define the sentiment analysis route
@app.route('/analyze', methods=['POST'])
def analyze():
    # Get the text input from the form
    text = request.form['text']

    # Analyze sentiment using Google Cloud NLP API
    document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
    sentiment = client.analyze_sentiment(document=document).document_sentiment

    # Determine sentiment score and label
    score = sentiment.score
    magnitude = sentiment.magnitude
    if score >= 0.2:
        label = 'Positive'
    elif score <= -0.2:
        label = 'Negative'
    else:
        label = 'Neutral'

    # Render the results
    return render_template('result.html', text=text, score=score, magnitude=magnitude, label=label)

if __name__ == '__main__':
    app.run(debug=True)