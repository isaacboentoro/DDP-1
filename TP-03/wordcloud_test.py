import string
import itertools

def count_words(file):
    with open("stopwords.txt",  'r') as s, open(file, 'r') as f:
        stopwords = s.read().lower().split()
        text  = f.read().lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        words = text.split()

    word_frequency = {}
    for word in words:
        if word not in stopwords:
            if word in word_frequency:
                word_frequency[word] += 1
            else:
                word_frequency[word] = 1
    word_frequency = dict(sorted(word_frequency.items(), key=lambda item: item[1], reverse=True))
    word_frequency = dict(itertools.islice(word_frequency.items(), 60))
    return word_frequency


def main():
    filename = input("Please enter filename: ")
    word_frequency = count_words(filename)
    print(f"{len(word_frequency)} words in frequency order as (count:word) pairs")
    max_word_length = max(len(word) for word in word_frequency.keys())
    max_count_length = max(len(str(count)) for count in word_frequency.values())

    for i, (word, count) in enumerate(word_frequency.items(), 1):
        print(str(count).rjust(max_count_length) + ":" + word.ljust(max_word_length), end="\t")
        if i % 3 == 0:
            print()


main()