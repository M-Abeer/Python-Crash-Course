# 4a
# Write a program to remove punctuations from the given string?
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

my_str = "Hello!!!, he said ---and went."
# To take input from the user
# my_str = input("Enter a string: ")
# remove punctuation from the string
no_punct = ""
for char in my_str:
 if char not in punctuations:
    no_punct = no_punct + char
# display the unpunctuated string
print(no_punct)

# 4 b
# Write a program to sort the sentence in alphabetical order?
my_str = "Hello this Is an Example With cased letters"

# Split the string into words and sort them
words = my_str.split()
for i in range(len(words)):
    words[i]=words[i].lower()
words.sort()

# Print the sorted words
print("The sorted words are:")
for word in words:
  print(word)
