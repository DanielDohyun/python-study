letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25::-1]
# backwards = letters[::-1] returns the same value
print(backwards)

qpo = letters[16:13:-1]
edcba = letters[4::-1]
print(letters[25:17:-1]) # returns last 8 characters in reverse order

# both returns the first index item
# first one give empty value when the string is empty
# 2nd one gives an error when the string is empty
print(letters[:1])
print(letters[0])


