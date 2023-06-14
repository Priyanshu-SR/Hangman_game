from wonderwords import RandomWord


def get_hangman_stage(j):
    max = 6
    stages = ["""
        ------
        |    |
        |    O
        |
        |
        |
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |    |
        |    |
        |
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |    |
        |    |
        |   /
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |    |
        |    |
        |   / \\
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |  --|
        |    |
        |   / \\
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |  --|--
        |    |
        |   / \\
        |
    ------------
    """]
    return stages[max - j]


r = RandomWord()
word = r.word()
print(word)
print("Hey! Let's play Hangman...\n\nYou've got 6 tries to guess the word.")
print(f"\nIt's a {len(word)} letters word.\n")
list0 = []
for i in word:
    list0.append("_")
print(list0)
j = 6
count = 0
while (j > 0):
    guessed_letter = input("\nGuess a letter : ")
    guessed_letter = guessed_letter.lower()
    if guessed_letter in list0:
        print(f"You've already guessed {guessed_letter}")
    else:
        if len(guessed_letter) == 1:
            if guessed_letter in word:
                print(f"\n{guessed_letter} is present in the word.\n")
                for i in range(len(word)):
                    if word[i] == guessed_letter:
                        list0[i] = guessed_letter
                        count += 1
                print(list0)
                if count == len(word):
                    break
            else:
                print(f"\n{guessed_letter} is not present in the word.\n")
                pic = get_hangman_stage(j)
                print(pic)
                j -= 1
        else:
            print(
                f"{guessed_letter} is not correct format of input. Please enter a letter.")
if count == len(word):
    print(f"\nYou guessed the {word}... YOU WIN!!!")
else:
    print(f"\nYou couldn't guess the {word}... YOU LOOSE!!!")
