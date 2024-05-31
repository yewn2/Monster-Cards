"""
Delete card version 2
This version is trialled with a list instead of a dictionary for the card database.
"""

# imports
import easygui

# setting up initial card database
card_lst = [
    ["Stoneling", ["Strength", "7"], ["Speed", "1"], ["Stealth", "25"], ["Cunning", "15"]],
    ["Vexscream", ["Strength", "1"], ["Speed", "6"], ["Stealth", "21"], ["Cunning", "19"]],
    ["Dawnmirage", ["Strength", "5"], ["Speed", "15"], ["Stealth", "18"], ["Cunning", "22"]],
    ["Blazegolem", ["Strength", "15"], ["Speed", "20"], ["Stealth", "23"], ["Cunning", "6"]],
    ["Websnake", ["Strength", "7"], ["Speed", "15"], ["Stealth", "10"], ["Cunning", "5"]],
    ["Moldvine", ["Strength", "21"], ["Speed", "18"], ["Stealth", "18"], ["Cunning", "5"]],
    ["Vortexwing", ["Strength", "19"], ["Speed", "13"], ["Stealth", "19"], ["Cunning", "2"]],
    ["Rotthing", ["Strength", "16"], ["Speed", "7"], ["Stealth", "4"], ["Cunning", "12"]],
    ["Froststep", ["Strength", "14"], ["Speed", "14"], ["Stealth", "17"], ["Cunning", "4"]],
    ["Wispghoul", ["Strength", "17"], ["Speed", "19"], ["Stealth", "3"], ["Cunning", "2"]],
]
print(card_lst)

# loop to continue asking for card ID and searching database for card
find_card = True

while find_card:
    # ask user for card ID to find
    monster_ID = easygui.enterbox("Enter the name of the card you wish to delete:",
                                  "Monster Name")

    # search card database for card ID
    complete_stats = ""
    card_index = 0
    for card_ID in card_lst:
        if monster_ID == card_ID[0]:
            find_card = False
            card_index = card_lst.index(card_ID)
            stats_lst = []
            for stat in card_lst[card_index][1::]:
                stats_lst.append([stat[0], stat[1]])
            for stat in stats_lst:
                complete_stats = complete_stats + f"{stat[0]} : {stat[1]}\n"
            delete_confirmation = easygui.buttonbox(f"Delete card?\n{monster_ID}\n"
                                                    f"{complete_stats}", "Card to delete",
                                                    ["Yes", "No"])
            # delete card if confirmed, otherwise start again
            if delete_confirmation == "Yes":
                card_lst.pop(card_index)
                easygui.msgbox(f"Monster Card '{monster_ID}' deleted.", "All Done!")
                break
            else:
                find_card = True

    if find_card:
        easygui.msgbox(f"Sorry, the card {monster_ID} could not be deleted.", "Failure")
        again = easygui.buttonbox("Would you like to enter another card name to delete?",
                                  "Try again?", ["Yes", "No"])
        if again == "No":
            find_card = False

print("-" * 100)
print(card_lst)
