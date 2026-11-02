VOWELS = 'aeiou'

# Declare word and get user input
word = input("Enter a word for us to count vowels: ")

# Declare total, outside of the loop
total = 0 

# for each letter in our word
for character in word:
    # print the letter
    print(character)

    # if the character is in our string of characters to check
    if character.lower() in VOWELS:
        # then add 1
        total += 1

#log out result
print(f"There are {total} vowels in {word}")