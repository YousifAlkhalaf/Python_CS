# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 13:12:35 2021

@author: Computer Science ~ B
"""
#Two to three stars

def fill_char(word, index, new_char):
    word = word[:index] + new_char + word[index + 1:]
    return word

def hashed(word):
    new_word = ''
    for c in word:
        new_word += c + ' '
    new_word = new_word[0: len(new_word) - 1]
    return new_word
        
    
def hangman():
    tries = 4
    used_words = ''
    ans = 'abecadarian'
    word = '___________'
    
    while tries > 0 and ans != word:
        print(f'Tries remaining: {tries}')
        print('Used letters: ' + used_words)
        print('\n' + hashed(word))
        
        while True:
            guess = input('Enter a character: ')
            if len(guess) > 1:
                print('Try again.')
            else:
                guess = guess.lower()
                break
        
        if ans.find(guess) == -1:
            tries -= 1
            if used_words == '':
                used_words += guess
            else:
                used_words += ', ' + guess
            print('Not in the word!')
        
        if word.find(guess) != -1:
            tries -= 1
            print('Already used!')
        
        else:
            for i in range(0, len(word), 1):
                if ans[i] == guess:
                    word = fill_char(word, i, guess)
    
    print('\n' + word)
    if word == ans:
        print('You won!')
    else:
        print('You lost!')

hangman()
            
                
    