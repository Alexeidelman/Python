Python 3.12.0 (v3.12.0:0fb18b02c8, Oct  2 2023, 09:45:56) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def pig_latin(text):
...   say = ""
...   # Separate the text into words
...   words = text.split()
...   for word in words:
...     # Create the pig latin word and add it to the list
...     pig_latin_word= word[1:]+word[0] +"ay"
...     say+= pig_latin_word+" "
...     # Turn the list back into a phrase
...   return say.strip()
... 		
... print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
