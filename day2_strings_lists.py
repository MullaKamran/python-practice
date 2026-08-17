# def reverse_string(user_input):
#     return user_input[::-1]

# print(reverse_string("hello"))

def find_longest_word(sentence):
    words = sentence.split()
    longest = ""
    
    for word in words:
        if len(word) > len(longest):  
            longest = word  
    
    return longest  # ← this line is missing 
    
print(find_longest_word("hello world, this is a test sentence"))    
