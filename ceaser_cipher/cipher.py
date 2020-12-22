import string
import operator
import nltk
nltk.download('words')

english_words = nltk.corpus.words.words()
english_words = [word.lower() for word in english_words]
letters = list(string.ascii_lowercase)

def encrypt(string, key):
    encrypted = ""
    string = string.lower()

    for character in string:
        if character in letters:
            character_index = letters.index(character) + key
            cipher_letter = letters[character_index % len(letters)]
            encrypted += cipher_letter
        else:
            encrypted += character

    return encrypted
    
def decrypt(encrypted, key):
     return encrypt(encrypted, -1*key)

def is_english(encrypted):
    counting_english_words = 0

    for word in encrypted:
        if word in english_words:
           counting_english_words += 1
    
    return (counting_english_words)



def break_cipher(encrypted):
    counts_dict = {}

    for key in range (len(letters)):
        counts_dict[f"{key}"] = is_english(decrypt(encrypted, key).split(" "))

    max_words_key = max(counts_dict.items(), key=operator.itemgetter(1))[0]
    return decrypt(encrypted, int(max_words_key))


if __name__ == "__main__":
    print (encrypt("abc", 1)) 
    print (encrypt("abc", 10)) 
    print (encrypt("abc", 27)) 
    print (decrypt("bcd", 1))
    print (decrypt("klm", 10))
    print (decrypt("bcd", 27))
    encrypted = encrypt("It was the best of times, it was the worst of times", 10)
    print (encrypted)
    print (break_cipher(encrypted))


    



