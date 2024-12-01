from encrypt_utils import char_to_num, num_to_char
from sympy import mod_inverse


def encrypt(a, b, text: str):
    text = text.upper()
    encrypted_text = ""
    for letter in text:
        encrypted_text += num_to_char[((a * char_to_num[letter]) + b) % 29]

    return encrypted_text


def most_common_letter(text: str):
    letter_counter = {}
    most_common = ("A", 0)
    text = text.upper()
    for letter in text:
        if letter not in letter_counter:
            letter_count = text.count(letter)
            letter_counter[letter] = letter_count, [text.index(letter)]
            if letter_count > most_common[1]:
                most_common = (letter, letter_count)
        else:
            if letter_counter[letter][1][-1] + 1 < len(text) - 1:
                letter_counter[letter][1].append(
                    text.index(letter, letter_counter[letter][1][-1] + 1)
                )
    return most_common[0], letter_counter[most_common[0]]


def desencrypt(a, b, text):
    a_inverse = mod_inverse(a, 29)
    text = text.upper()
    desencrypted = []
    for letter in text:
        desencrypted.append(num_to_char[(a_inverse * (char_to_num[letter] - b)) % 29])
    return desencrypted
