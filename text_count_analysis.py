import string  # required for using string.punctuation function

"""
@author: Salik Tariq
@date: 21 March 2023
"""

# Step 7: create a single script that performs all of the operations on the original 's' string

s = """Imagine a vast sheet of paper on which straight Lines, Triangles, Squares, Pentagons, Hexagons, and other 
figures, instead of remaining fixed in their places, move freely about, on or in the surface, but without the power 
of rising above or sinking below it, very much like shadows - only hard and with luminous edges - and you will then 
have a pretty correct notion of my country and countrymen. Alas, a few years ago, I should have said "my universe": 
but now my mind has been opened to higher views of things."""

# Step 1: Normalize the Letter Casing
s_lower = s.lower()

print("Step 1: Normalize the Letter Casing\n")
print(s_lower)
print("\n\n")

# Step 2: Split the lowercase string into individual words
words = list()
words = s_lower.split()

print("Step 2: Using the str.split() method, divide the s_lower string into separate words.\n")
print(words)
print("\n\n")

# Step 3: Use the len method to return the number of words in the string.
no_of_words = len(words)

print("Step 3: Use the len method to return the number of words in the string.\n")
print("number of words in the string: ", no_of_words)
print("\n\n")

# Step 4: Use a set to compute the number of distinct words in the string.
distinct_words = len(set(words))

print("Step 4: Use a set to compute the number of distinct words in the string.\n")
print("number of distinct words in the string: ", distinct_words)
print("\n\n")

# Step 5 The next step is to compute the frequency of the distinct words in our string.
word_freq = dict()

for i in words:
    found = word_freq.get(i)
    if found is not None:
        word_freq[i] += 1
    else:
        word_freq[i] = 1

print("Step 5 The next step is to compute the frequency of the distinct words in our string.\n")
print("the frequency of the distinct words in our string: ", word_freq)
print("\n\n")

# Step 6: Remove Punctuation Marks from 'words' list
punctuation_list = list(string.punctuation)
w_clean = list()

for word in words:
    if word not in punctuation_list:
        temp_word = word
        if temp_word[0] in punctuation_list:
            temp_word = temp_word[1:]
        if temp_word[len(temp_word) - 1] in punctuation_list:

            while temp_word[len(temp_word)- 1] in punctuation_list:
                temp_word = temp_word[:len(temp_word) - 1]

        w_clean.append(temp_word)

print("Step 6: Remove Punctuation Marks.\n")
print(w_clean)
print("\nthe frequency of the words in our string: ", len(w_clean))


# Step 6: Remove Punctuation Marks AND print distinct words (Extra step)
punctuation_list = list(string.punctuation)
w_clean = list()

for word in words:
    if word not in punctuation_list:
        if word not in w_clean:
            temp_word = word
            if temp_word[0] in punctuation_list:
                temp_word = temp_word[1:]
            if temp_word[len(temp_word) - 1] in punctuation_list:

                while temp_word[len(temp_word) - 1] in punctuation_list:
                    temp_word = temp_word[:len(temp_word) - 1]

            w_clean.append(temp_word)


print("\nStep 6b: Remove Punctuation Marks and print list without repeating characters\n")
print(w_clean)
print("\nthe frequency of the distinct words in our string: ", len(w_clean))