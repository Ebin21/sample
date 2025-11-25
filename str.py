def reverse_string(s):
    return s[::-1]
def is_palindrome(s):
    return s == s[::-1]
def to_uppercase(s):
    return s.upper()
def to_lowercase(s):
    return s.lower()    
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)   
Word=input("Enter a string: ")
print(f"Reversed String of  {Word} :", reverse_string(Word))
print(f"Is Palindrome of  {Word} :", is_palindrome(Word))
print(f"Uppercase of  {Word} :", to_uppercase(Word))
print(f"Lowercase of  {Word} :", to_lowercase(Word))
print(f"Vowel Count of  {Word} :", count_vowels(Word))