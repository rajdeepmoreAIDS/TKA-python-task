word1 = input("enter first word: ")
word2 = input("enter second word: ")

if sorted(word1) == sorted(word2):
    print("words are anagram")
else:
    print("words are Not anagram")