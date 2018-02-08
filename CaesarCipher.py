
def rotateLetter(letter, rot):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    length = len(alphabet)-1
    letter = letter.lower()
    if letter in alphabet:
        orig_index = alphabet.index(letter)
    elif letter == ' ':
        return " "
    else:
        return 'Error - letter not in alphabet'
    new_index = orig_index + rot
    if new_index > length:
        new_index = (new_index%length) - 1
    return alphabet[new_index]


# print rotateLetter('A', 1)

def CaesarEncrypt(message, rotation):
    output = []
    [output.append(rotateLetter(letter, rotation)) for letter in message]
    return "".join(output)

print CaesarEncrypt("meatball meatball ravioli", 26)