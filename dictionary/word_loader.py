import nltk
nltk.download('words')

import random
from nltk.corpus import words

def load_word_dict_by_length(max_len):
    all_words = words.words()
    random.shuffle(all_words)  # 💥 Randomize word order

    word_dict = {}

    for w in all_words:
        w = w.lower()
        if not w.isalpha():
            continue
        if len(w) > max_len:
            continue
        word_dict.setdefault(len(w), []).append(w)

    return word_dict

word_dict = load_word_dict_by_length(max_len=15)
print(word_dict[5][:10])  # Sample test
# for length in sorted(word_dict.keys()):
#     print(f"\n📏 {length}-letter words ({len(word_dict[length])} total):")
#     print(", ".join(word_dict[length]))