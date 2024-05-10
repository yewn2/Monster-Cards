"""
Welcome screen and instructions version 2
Takes welcome_instructions v1 and places it into a function for easier use
Instructions and program name variables added for easier function use in future
Copied from previous project: Burger Menu Combos
"""

# imports
import easygui


def welcome_instructions(program_name, instruction_list):
    # display welcome screen
    easygui.msgbox(f"Welcome to {program_name}!", "Welcome")

    # display instructions
    instructions = [f"Instructions for use of {program_name}\n"]
    for inst in instruction_list:
        instructions.append(f"\n* {inst} *")
    easygui.msgbox("".join(instructions), "Instructions")


# Main routine goes here:
welcome_instructions("Monster Cards",
                     ["Choose an action after this box",
                      "To add a card: enter a card ID, then fill in the stats "
                      "for the card, then confirm "
                      "your entry.",
                      "To delete a card, enter the card ID and confirm your "
                      "choice.",
                      "To find a card, enter the specific card ID.",
                      "'Output all' allows you to see which cards are already "
                      "present in the menu.",
                      "Once you have finished, exit the program."])
