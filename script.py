word = raw_input("Enter a word to translate into PygLatin: ")

if word.isalpha():
    end_char = word[0] #get value at string index 0
    word= word[:0] + word[1:] + end_char + "ay" #slice starting after 0 and before 1
    print word
else:
    print "invalid entry"
