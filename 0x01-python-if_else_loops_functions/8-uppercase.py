def uppercase(str):
    for char in str:
        letter = ord(char)
        if letter in range(97,  122):
            print("{:c}" .format(letter - 32))
        elif letter in range(65, 90):
            print("{:c}" .format(letter + 32))
        else:
            print("{:c}" .format(letter))
