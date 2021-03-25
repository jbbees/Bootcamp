# Create a variable named cheer and give it a word to cheer (i.e. Python or FinTech)

cheer = "Yah!"

# Below strings can be used to add fun
cheer_symbol = "*\O/*"
cheer_symbol_2 = "ヘ( ^o^)ノ＼(^_^ )"

# Loop through string and print each letter with a cheer

for letter in "GO TEAM SOME COMPANY!":
    if letter == ' ':
        continue                                       # use a continue to omit spaces in the string.
    print(letter + ' ' + cheer)

# Print excitement to screen
print("\nWhat does that spell?!")
print(cheer + "!\nWoohoo! Go " + cheer + "!")
print(cheer_symbol * 3)
print(cheer_symbol_2)
