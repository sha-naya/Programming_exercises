'''
Title: Anagram function
Author: Ayan Ashkenov
Date: 23/01/2021
Description: This function determines if two words are anagrams.
Two words are anagrams if they have the same letters, but they could have
a different arrangement of them. For ex. binary & brainy
'''

def anagram_finder(word1, word2):

        if len(word1) != len(word2):
                return "These words are NOT anagrams."
        
        else:                
                for l in list(word1):
                        if l not in list(word2):
                                return "These words are NOT anagrams."
                return "These words ARE anagrams."