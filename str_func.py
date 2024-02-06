def uppercase_string(input_string):
    """"Делает буквы заглавными"""
    return input_string.upper()

def capitalize_words(input_string):
    """"Делает первые буквы заглавными"""
    words = input_string.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)

string = "hello, world!"
result2 = capitalize_words(string)
result1 = uppercase_string(string)
print(result1) #Вывод: HELLO, WORLD!
print(result2) # Вывод: Hello, World!