import random
import sys

def fetch_words(num_words):
    num_words = int(num_words)
    with open("/usr/share/dict/words","r") as dict:
        stored_lines = [word.strip('\n') for word in dict]
        random_words = random.choices(stored_lines, k=num_words)
        return random_words

if __name__ == '__main__':
    num_words = sys.argv[1]
    print(' '. join(fetch_words(num_words)))