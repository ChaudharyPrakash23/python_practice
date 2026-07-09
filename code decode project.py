import random
import string

def random_chars():
    return ''.join(random.choice(string.ascii_letters) for _ in range(3))

choice = input("Enter 'c' to code or 'd' to decode: ").lower()

if choice == "c":
    message = input("Enter the message: ")
    words = message.split()
    coded_words = []

    for word in words:
        if len(word) <= 3:
            new_word = word[1:] + word[0]
            new_word = random_chars() + new_word + random_chars()
        else:
            new_word = word[::-1]

        coded_words.append(new_word)

    print("Coded Message:", " ".join(coded_words))

elif choice == "d":
    message = input("Enter the coded message: ")
    words = message.split()
    decoded_words = []

    for word in words:
        if len(word) < 3:
            new_word = word[::-1]
        else:
            word = word[3:-3]
            new_word = word[-1] + word[:-1]

        decoded_words.append(new_word)

    print("Decoded Message:", " ".join(decoded_words))

else:
    print("Invalid choice!")