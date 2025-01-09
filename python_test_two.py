import re
from collections import Counter


# Python Test 2
def count_word_frequencies(text):
    # Remove punctuation and convert to lowercase
    words = re.findall(r'\b\w+\b', text.lower())
    # Count the frequency of each word
    word_counts = Counter(words)
    # Sort words by frequency in descending order
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_word_counts

def display_word_frequencies(word_frequencies):
    print("Word Frequencies:")
    for word, count in word_frequencies:
        print(f"{word}: {count}")

# Example input
text = "Hello world! This is a test. Hello, this test is only a test."

# Count and display word frequencies
word_frequencies = count_word_frequencies(text)
display_word_frequencies(word_frequencies)
