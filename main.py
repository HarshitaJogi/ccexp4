from google.cloud import language_v1
client = language_v1.LanguageServiceClient()

text = u"""I am very happy."""

document = language_v1.Document(
    content=text, type_=language_v1.Document.Type.PLAIN_TEXT
)

sentiment = client.analyze_sentiment(
    request={"document": document}
).document_sentiment

print("Text: {}".format(text))
print("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude))



