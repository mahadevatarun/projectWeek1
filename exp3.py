# Rail-Fence Cipher Implementation

def rail_fence_encrypt(message, rails):
    fence = [['\n' for _ in range(len(message))] for _ in range(rails)]
    direction_down = False
    row, col = 0, 0

    for char in message:
        if row == 0 or row == rails - 1:
            direction_down = not direction_down
        fence[row][col] = char
        col += 1
        row += 1 if direction_down else -1

    encrypted_message = ''.join([''.join(row) for row in fence]).replace('\n', '')
    return encrypted_message

def rail_fence_decrypt(cipher, rails):
    fence = [['\n' for _ in range(len(cipher))] for _ in range(rails)]
    direction_down = None
    row, col = 0, 0

    for i in range(len(cipher)):
        if row == 0:
            direction_down = True
        if row == rails - 1:
            direction_down = False
        fence[row][col] = '*'
        col += 1
        row += 1 if direction_down else -1

    index = 0
    for i in range(rails):
        for j in range(len(cipher)):
            if (fence[i][j] == '*' and index < len(cipher)):
                fence[i][j] = cipher[index]
                index += 1

    decrypted_message = []
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            direction_down = True
        if row == rails - 1:
            direction_down = False
        if fence[row][col] != '*':
            decrypted_message.append(fence[row][col])
            col += 1
        row += 1 if direction_down else -1

    return ''.join(decrypted_message)

# Sample Input
N = 6
Message = "S21location56"

# Encryption
encrypted = rail_fence_encrypt(Message, N)
print("Encrypted:", encrypted)

# Decryption
decrypted = rail_fence_decrypt(encrypted, N)
print("Decrypted:", decrypted)
