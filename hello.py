import boto3
from pathlib import Path

client = boto3.client('comprehend')

alice_text = Path('firstPart.txt').read_text()
response = client.detect_sentiment(Text=alice_text, LanguageCode='en')
print(response)

