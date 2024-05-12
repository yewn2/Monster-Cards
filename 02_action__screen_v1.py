"""
Component 2 (Action choices) v1
Displays an action choice screen with appropriate choices
Copied from previous project: Burger Menu Combos
"""


# imports
import easygui


# display action screen with choices
choice = easygui.buttonbox("What would you like to do?",
                           "MONSTER CARDS",
                           ["Add card", "Delete card",
                            "Find card", "Output all", "Exit"])

# while loop to continue asking for choices
while choice != "Exit":
    # display action screen with choices
    choice = easygui.buttonbox("What would you like to do?",
                               "BURGER MENU COMBO EDITOR",
                               ["Add card", "Delete card",
                                "Find card", "Output all", "Exit"])

# if exit chosen then display ending
easygui.msgbox("Thanks for using Monster Cards",
               "Goodbye!")
