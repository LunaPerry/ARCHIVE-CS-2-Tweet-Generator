import random
import sys

def rearrange(word):
    return random.shuffle(word)
    # return word
    
if __name__ == '__main__':
    word = sys.argv[1:]
    random_word = rearrange(word)
    print(random_word)