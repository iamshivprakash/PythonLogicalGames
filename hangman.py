import random
word_list = ["apple", "banana", "mango", "tiger"]
chosen_word = random.choice(word_list)
display=[]
lives=6
# print(f"solution is:{chosen_word}")
for _ in range(len(chosen_word)):
    display+="_"
print(display)
end_of_game=False
while not end_of_game:
    guess=input("Guess a letter:\n").lower()
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter==guess:
            display[position]=letter

    print(display)
    if guess not in chosen_word:
        lives-=1
        if lives==0:
            end_of_game=True
            print("you lose")
    if "_" not in display:
        end_of_game = True
        print("you win")