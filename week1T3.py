import requests
import string
from collections import Counter

url = "https://raw.githubusercontent.com/spyguessgame-boop/own_dataset/refs/heads/main/data.txt"

response = requests.get(url)
response.raise_for_status()

text_data = response.text[:1000]

# Remove punctuation
clean_text = text_data.translate(
    str.maketrans('', '', string.punctuation)
)

# Tokenization
tokens = clean_text.split()

print("First 20 Tokens:")
print(tokens[:20])

# Total tokens
print("Total Tokens =", len(tokens))

# Most frequent token
counter = Counter(tokens)

word, count = counter.most_common(1)[0]

print("Most Frequent Token =", word)
print("Frequency =", count)
