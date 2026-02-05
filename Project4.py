questions = [
    ["What is the only metal that is liquid at room temperature?", "Hg", "Na", "K", "Ni", 1],
    ["Which is the smallest continent in the world?","Asia","Australlia","Africa","Europe", 2],
    ["What color is the sun?","Red","Blue", "Yellow", "White", 3],
    ["How many poles does the magnet have?", "5", "4", "3", "2", 4],
    ["Which planet is known as the red planet?", "Mars", "Earth", "Venus", "Saturn", 1],
    ["What is the word opposite to 'Hot'?", "up", "cool", "down", "beside", 2],
    ["What do you call a person who flies an airplane?", "doctor", "police", "pilot", "watchman", 3],
    ["What shape has 3 sides?", "square", "rectangle", "circle", "triagle", 4],
    ["Which animal call the king of jungle?", "lion", "tiger", "elephant", "deer", 1],
    ["How many color has our flag have", "1", "4", "3", "2", 2]
]

for question in questions:
    print(question[0])
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")

    a = int(input("Enter your answer: 1 for a, 2 for b, 3 for c, 4 for d\n"))
    if(question[5] == a):
        print("Your answer is...")
        print("Correct!₍₍⚞(˶˃ ᵕ ˂˶)⚟⁾⁾")
    else:
        print(f"Incorrect, the correct answer was {question[5]}")
        print("Better luck next time!")
        break
    