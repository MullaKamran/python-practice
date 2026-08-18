def fizzbuzz(n):
    if n%3==0 and n%5==0:
        return "FizzBuzz"
    elif n%3==0:
        return "Fizz"
    elif  n%5==0:
        return "Buzz"
    else:
        return str(n)
print(fizzbuzz(4))  

def count_vowels(word):
    #vowels="aeiouAEIOU"
    counter=0
    for letter in word:
        if letter in "aeiouAEIOU":
            counter+=1
    return counter
print(count_vowels("hello"))            
    