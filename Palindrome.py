string = input('Type the word or sentence you want to check: ').upper()

reverse_word = ''
split_string = list(string)

for i in split_string:
    reverse_word=i+reverse_word
    
if split_string == list(reverse_word):
    print("The entered text is Palindrome.") 
else:
    print("The word is not Palindrome.")
       
