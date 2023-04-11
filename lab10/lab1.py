import datetime
import math
import string
import random
import itertools

def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(chars, k=length))
    return password

def get_combinations(lst):
    return list(itertools.combinations(lst, 2))

def get_factorial(num):
    return math.prod(range(1, num+1))

def encode_message(message, shift):
    encoded = ''
    for char in message:
        if char.isalpha():
            char_code = ord(char.lower()) - 97
            new_char_code = (char_code + shift) % 26
            encoded += chr(new_char_code + 97)
        else:
            encoded += char
    return encoded

def decode_message(message, shift):
    return encode_message(message, -shift)

def get_current_time():
    return datetime.datetime.now()



# Пример использования функций
password = generate_password(4)
combinations = get_combinations(list(password))
factorial = get_factorial(len(password))
encoded_message = encode_message(password, 3)
decoded_message = decode_message(encoded_message, 3)
current_time = get_current_time()


print('Password:', password)
print('Combinations:', combinations)
print('Factorial:', factorial)
print('Encoded message:', encoded_message)
print('Decoded message:', decoded_message)
print('Current time:', current_time)
