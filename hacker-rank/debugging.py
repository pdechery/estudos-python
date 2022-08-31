#!/bin/python3

# https://www.hackerrank.com/challenges/words-score

def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    score = 0
    for word in words:
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
        print('num vogais: {}'.format(num_vowels))
        if num_vowels % 2 == 0:
            score += 2
            print(f'{word} score par {score}')
        else:
            # ++score <-- este era o erro
            score += 1
            print(f'{word} score impar {score}')
    return score

if __name__ == '__main__':
    
    n = int(input())
    words = input().split()
    print(score_words(words))