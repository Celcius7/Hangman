import random
from hangman_art import logo, stages
from hangman_names import word_list
ans_word = random.choice(word_list)
print(logo)
print(ans_word)

demo_ans = []
for letter in ans_word:
    demo_ans.append("_ ")
print(demo_ans)
count = 6
gaming = True
while gaming:
    user_guess = input("Guess a letter : ").lower()
    if user_guess in demo_ans:
        print("You already guessed this letter...")
        continue
    for i in range(len(ans_word)):
        if ans_word[i] == user_guess:
            demo_ans[i] = user_guess
    print(demo_ans)


    if user_guess not in ans_word:
        count -=1
        print(stages[count])
        if count == 0:
            print("You lose")
            gaming = False
            print(f"Word : {ans_word}")

    if "_ " not in demo_ans:
        gaming = False
        print("You guessed all letters correctly...")


