"""
Base component version 1
Contains welcome_instructions and action_screen components, along with unfilled
card action components.
"""


# imports
import easygui


# function to welcome user and show instructions
def welcome_instructions(program_name, instruction_list):
    # display welcome screen
    easygui.msgbox(f"Welcome to {program_name}!", "Welcome")

    # display instructions
    instructions = [f"Instructions for use of {program_name}\n"]
    for inst in instruction_list:
        instructions.append(f"\n* {inst} *")
    easygui.msgbox("".join(instructions), "Instructions")


# function to display action screen
def action_screen(cards):
    # display action screen with choices
    choice = easygui.buttonbox("What would you like to do?",
                               "MONSTER CARDS",
                               ["Add card", "Delete card",
                                "Find card", "Output all", "Exit"])

    # while loop to continue asking for choices
    while choice != "Exit":
        # check the choice and call the appropriate function
        if choice == "Add card":
            add_card(cards)
        elif choice == "Delete card":
            delete_card(cards)
        elif choice == "Find card":
            find_card(cards)
        elif choice == "Output all":
            output_all(cards)

        # display action screen with choices again
        choice = easygui.buttonbox("What would you like to do?",
                                   "MONSTER CARD BASE EDITOR",
                                   ["Add card", "Delete card",
                                    "Find card", "Output all", "Exit"])

    # if exit chosen then display ending
    easygui.msgbox("Thanks for using Monster Cards",
                   "Goodbye!")


# function to add a card
def add_card(database):
    ...


# function to add a card
def delete_card(database):
    ...


# function to add a card
def find_card(database):
    ...


# function to add a card
def output_all(database):
    ...


# Main routine goes here:
# setting up initial card database
card_dict = {
    "Stoneling": {
        "Strength": "7",
        "Speed": "1",
        "Stealth": "25",
        "Cunning": "15"
    },
    "Vexscream": {
        "Strength": "1",
        "Speed": "6",
        "Stealth": "21",
        "Cunning": "19"
    },
    "Dawnmirage": {
        "Strength": "5",
        "Speed": "15",
        "Stealth": "18",
        "Cunning": "22"
    },
    "Blazegolem": {
        "Strength": "15",
        "Speed": "20",
        "Stealth": "23",
        "Cunning": "6"
    },
    "Websnake": {
        "Strength": "7",
        "Speed": "15",
        "Stealth": "10",
        "Cunning": "5"
    },
    "Moldvine": {
        "Strength": "21",
        "Speed": "18",
        "Stealth": "14",
        "Cunning": "5"
    },
    "Vortexwing": {
        "Strength": "19",
        "Speed": "13",
        "Stealth": "19",
        "Cunning": "2"
    },
    "Rotthing": {
        "Strength": "16",
        "Speed": "7",
        "Stealth": "4",
        "Cunning": "12"
    },
    "Froststep": {
        "Strength": "14",
        "Speed": "14",
        "Stealth": "17",
        "Cunning": "4"
    },
    "Wispghoul": {
        "Strength": "17",
        "Speed": "19",
        "Stealth": "3",
        "Cunning": "2"
    },
}

# welcome the user
welcome_instructions("Monster Cards",
                     ["Choose an action after this box",
                      "To add a card: enter a card name, then fill in the "
                      "stats for the card, then confirm your entry.",
                      "To delete a card, enter the card name and confirm your "
                      "choice.",
                      "To find a card, enter the specific card name.",
                      "'Output all' allows you to see which cards are already "
                      "present in the menu.",
                      "Once you have finished, exit the program."])

# start main program with action screen
action_screen(card_dict)
