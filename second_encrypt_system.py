import numpy as np
from encrypt_utils import char_to_num


def three_letters_chunks(text):
    chunks = []
    current_length = 0
    text = text.upper()
    for letter in text:
        if current_length == 0:
            chunks.append([])
        chunks[-1].append(char_to_num[letter])
        current_length += 1
        current_length %= 3
    while len(chunks[-1]) < 3:
        chunks[-1].append(char_to_num[" "])
    return chunks


def second_system_encrypt(matrix, b, chunks):
    encrypted = []
    for chunk in chunks:
        encrypted.append((np.dot(matrix, chunk) + b) % 29)
    return encrypted


def second_desencrypt(matrix_inv, b, chunks):
    desencrypted = []
    for chunk in chunks:
        chunk_array = np.array(chunk)
        x = (chunk_array - b) % 29
        desencrypted.append(np.dot(matrix_inv, x) % 29)
    return desencrypted
