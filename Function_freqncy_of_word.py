def frequency(s):
    s= s.lower().split()
    word_frequency ={}
    for char in s:
        if char.isspace():
            continue
        if char in word_frequency:
            word_frequency[char] += 1
        else :
            word_frequency[char] = 1
        
    for word,item in word_frequency.items():
        print(f"'{word}':{item}")

frequency("Crazy Fredrick bought many very exquisite opal jewels")

# def frequency(s):
#     """
#     Computes the frequency of words in a string and returns them in sorted order.

#     Args:
#         s (str): Input string.

#     Returns:
#         dict: A dictionary where keys are unique words in the string and values are their frequencies.
#     """
#     # Create an empty dictionary to store the word frequencies
#     word_freq = {}

#     # Convert the input string to lowercase and split it into words
#     words = s.lower().split()

#     # Iterate through each word and update the word frequencies in the dictionary
#     for word in words:
#         if word in word_freq:
#             word_freq[word] += 1
#         else:
#             word_freq[word] = 1

#     # Sort the word frequencies dictionary by keys in alphabetical order
#     sorted_word_freq = dict(sorted(word_freq.items()))

#     return sorted_word_freq
# input_string = "The quick brown fox jumps over the lazy dog"
# result = frequency(input_string)
# print(result)
# s="vaikhasdk vdsqg shsgdjh g"
# print(s.split())
# help(split)