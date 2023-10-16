
import random

dice_faces = {
    1: [
        "┌───────┐",
        "│       │",
        "│   •   │",
        "│       │",
        "└───────┘"
    ],
    2: [
        "┌───────┐",
        "│       │",
        "│ •  •  │",
        "│       │",
        "└───────┘"
    ],
    3: [
        "┌───────┐",
        "│ •     │",
        "│   •   │",
        "│     • │",
        "└───────┘"
    ],
    4: [
        "┌───────┐",
        "│ •   • │",
        "│       │",
        "│ •   • │",
        "└───────┘"
    ],
    5: [
        "┌───────┐",
        "│ •   • │",
        "│   •   │",
        "│ •   • │",
        "└───────┘"
    ],
    6: [
        "┌───────┐",
        "│ •   • │",
        "│ •   • │",
        "│ •   • │",
        "└───────┘"
    ]
}

while True:
    roll_dice = random.randint(1, 6)
    roll_dice2 = random.randint(1, 6)

    print("dice rolled: {} and {}".format(roll_dice, roll_dice2))
    for line in dice_faces[roll_dice]:
        print(line)
    print("\n")
    for line in dice_faces[roll_dice2]:
        print(line)

    roll = input("roll the dice (yes/no):").lower()
    if roll != "yes" and roll != "y":
        break

print("Thank you for gambling")

import random

dice_faces = {
    1: [
        "┌───────┐",
        "│       │",
        "│   •   │",
        "│       │",
        "└───────┘"
    ],
    2: [
        "┌───────┐",
        "│       │",
        "│ •  •  │",
        "│       │",
        "└───────┘"
    ],
    3: [
        "┌───────┐",
        "│ •     │",
        "│   •   │",
        "│     • │",
        "└───────┘"
    ],
    4: [
        "┌───────┐",
        "│ •   • │",
        "│       │",
        "│ •   • │",
        "└───────┘"
    ],
    5: [
        "┌───────┐",
        "│ •   • │",
        "│   •   │",
        "│ •   • │",
        "└───────┘"
    ],
    6: [
        "┌───────┐",
        "│ •   • │",
        "│ •   • │",
        "│ •   • │",
        "└───────┘"
    ]
}

while True:
    roll_dice = random.randint(1, 6)
    roll_dice2 = random.randint(1, 6)

    print("dice rolled: {} and {}".format(roll_dice, roll_dice2))
    for line in dice_faces[roll_dice]:
        print(line)
    print("\n")
    for line in dice_faces[roll_dice2]:
        print(line)

    roll = input("roll the dice (yes/no):").lower()
    if roll != "yes" and roll != "y":
        break

print("Thank you for gambling")

