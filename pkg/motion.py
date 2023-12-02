import os
import time

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_christmas_tree(tree, dice_position, dice_value):
    for i, line in enumerate(tree):
        if i == 2:  # Add the dice line
            print(line[:dice_position] + str(dice_value) + line[dice_position + 1:])
        else:
            print(line)

def move_dice(tree_width, dice_position, speed):
    dice_position += speed
    if dice_position > tree_width - 1:
        dice_position = 0
    return dice_position

def main():
    christmas_tree = [
        "         🌟         ",
        "       🎄 \\\        ",
        "       /   \\\🎁     ",
        "     🔔 🎅  \\\      ",
        "     /======🎄\\    ",
        "        |||         "
    ]

    tree_width = len(christmas_tree[0])
    dice_position = 0
    speed = 1

    for _ in range(8):  # Adjust the number of iterations for the desired duration
        clear_terminal()

        # Move the dice and draw the tree
        dice_position = move_dice(tree_width, dice_position, speed)
        draw_christmas_tree(christmas_tree, dice_position, _ % 6 + 1)
        print('주사위 굴리는 중...')

        time.sleep(0.2)

if __name__ == "__main__":
    main()

