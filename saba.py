print()


print("****************************")

S = [
    " ***** ",
    "*      ",
    " ***** ",
    "      *",
    " ***** "
]

A = [
    "   *   ",
    "  * *  ",
    " *   * ",
    "*******",
    "*     *"
]

B = [
    "****** ",
    "*     *",
    "****** ",
    "*     *",
    "****** "
]

# Combine the patterns for each letter
letters = [S, A, B, A]

# Print each line of the word
for i in range(5):
    for letter in letters:
        print(letter[i], end="  ")
    print()
