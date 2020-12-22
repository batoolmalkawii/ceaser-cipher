PR: https://github.com/batoolmalkawii/ceaser-cipher/pull/1

# Ceaser Cipher

In this project, we worked on a well-know cryptographic class - the Caesar Cipher.


### Feature Tasks and Requirements
* `encrypt`: takes in a plain text phrase and a numeric shift. The phrase will then be shifted that many letters, shifts that exceed 26 should wrap around.
* `decrypt`: takes in encrypted text and numeric shift which will restore the encrypted text back to its original form as long as correct key is supplied.
* `break_cipher`: Break the cipher so that an encrypted message can be transformed into its original state WITHOUT access to the key.
* `is_english`: Returns the number of english words in a sentence.

### User Acceptance Tests:

Test cases:

    1. encrypt a string with a given shift
    2. decrypt a previously encrypted string with the same shift
    3. encryption should handle upper and lower case letters
    4. encryption should allow non-alpha characters but ignore them, including white space
    5. decrypt encrypted version of It was the best of times, it was the worst of times. WITHOUT knowing the shift used.
