import numpy as np
from encrypt_utils import num_to_char
from first_encrypt_system import desencrypt, encrypt, most_common_letter
from numpy.linalg import inv
from second_encrypt_system import (
    second_desencrypt,
    second_system_encrypt,
    three_letters_chunks,
)

trabalenguas = "Pablito clavo un clavito * que clavito clavo Pablito * Pablito clavo un clavito en la calva de un calvito * Que calvito tan maldito el clavito que clavo Pablito"
print(f"Nuestro texto es: \n{trabalenguas}\n\nY su letra más común es:")
most_common = most_common_letter(trabalenguas)
print(
    f"{most_common[0][0]} con {most_common[1][0]} apariciones en los indices {most_common[1][1]}"
)
print()

print("Encriptandolo con el primer sistema obtenemos:")
encrypted = encrypt(4, 5, trabalenguas)
print(encrypted)
print()

print("Y la letra más común es:")
most_common = most_common_letter(encrypted)
print(
    f"{most_common[0][0]} con {most_common[1][0]} apariciones en los índices {most_common[1][1]}"
)
print()

print("Al desencriptarlo obtenemos:")
print("".join(desencrypt(4, 5, encrypted)))
print()

matrix = np.array([[1, 0, 0], [2, 1, 0], [3, 4, 1]])
b = np.array([3, 8, 2])


print("Al encriptar con nuestro segundo sistema obtenemos:")
encrypted_second_system = []
encrypted_chunks = second_system_encrypt(matrix, b, three_letters_chunks(trabalenguas))
for chunk in encrypted_chunks:
    encrypted_second_system.extend(chunk)
encrypted = "".join([num_to_char[int(n)] for n in encrypted_second_system])

print(encrypted)
print()

print("Y la letra más común es:")
most_common = most_common_letter(encrypted)
print(
    f"{most_common[0]} con {most_common[1][0]} apariciones en los índices {most_common[1][1]}"
)
print()

print("Y al desencriptarlo: ")
desencrypted_chunks = second_desencrypt(inv(matrix), b, encrypted_chunks)
desencrypted_second_system = []
for chunk in desencrypted_chunks:
    desencrypted_second_system.extend(chunk)
print("".join([num_to_char[int(value)] for value in desencrypted_second_system]))
