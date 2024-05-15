"""
Add card version 2
Trialling Add card with a list format.
Basically the same code from version 1 but with lists
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

# ask user for card name
new_monster = easygui.enterbox("Enter a name for your new monster card:",
                               "New Monster")

# name confirmation
confirm_monster = easygui.buttonbox(f"The name you want to have for your new "
                                    f"card is {new_monster}.",
                                    "Monster Name Confirmation",
                                    ["Yes", "No"])

while confirm_monster != "Yes":
    # ask user for card name again
    new_monster = easygui.enterbox("Enter a name for your new monster card:",
                                   "New Monster")
    # name confirmation again
    confirm_monster = easygui.buttonbox(
        f"The name you want to have for your new "
        f"card is {new_monster}.",
        "Monster Name Confirmation",
        ["Yes", "No"])

# add card name to card database; set stat categories by default  to 0
card_lst.append([])
monster_index = card_lst.index([])
card_lst[monster_index].insert(monster_index, new_monster)
card_lst[monster_index].insert(1, ["Strength", "0"])
card_lst[monster_index].insert(2, ["Speed", "0"])
card_lst[monster_index].insert(3, ["Stealth", "0"])
card_lst[monster_index].insert(4, ["Cunning", "0"])

# entering stats for new card
monster_stats = easygui.buttonbox(f"Your new monster {new_monster}'s "
                                  f"current stats are:\n"
                                  f"\tStrength: "
                                  f"{card_lst[monster_index][1][1]}\n"
                                  f"\tSpeed: "
                                  f"{card_lst[monster_index][2][1]}\n"
                                  f"\tStealth: "
                                  f"{card_lst[monster_index][3][1]}\n"
                                  f"\tCunning: "
                                  f"{card_lst[monster_index][4][1]}\n"
                                  f"Please choose which of the current "
                                  f"categories you would like to change.",
                                  "Current Monster Statistics",
                                  ["Strength", "Speed", "Stealth",
                                   "Cunning", "I don't want "
                                              "to change anything"])

while monster_stats != "I don't want to change anything":
    stat_index = 0
    if monster_stats == "Strength":
        stat_index = 1
    elif monster_stats == "Speed":
        stat_index = 2
    elif monster_stats == "Stealth":
        stat_index = 3
    else:
        stat_index = 4
    card_lst[monster_index][stat_index][1] = str(easygui.integerbox("Enter a new value for the "
                                                                    f"{monster_stats} category: \n"
                                                                    f"(must be a whole number "
                                                                    f"between 0 and 25)",
                                                                    "New Stat", 0,
                                                                    0, 25))

    # making sure the statistic value is an integer
    if card_lst[monster_index][stat_index][1] == "None":
        card_lst[monster_index][stat_index][1] = "0"

    monster_stats = easygui.buttonbox(f"Your new monster {new_monster}'s "
                                      f"current stats are:\n"
                                      f"\tStrength: "
                                      f"{card_lst[monster_index][1][1]}\n"
                                      f"\tSpeed: "
                                      f"{card_lst[monster_index][2][1]}\n"
                                      f"\tStealth: "
                                      f"{card_lst[monster_index][3][1]}\n"
                                      f"\tCunning: "
                                      f"{card_lst[monster_index][4][1]}\n"
                                      f"Please choose which of the current "
                                      f"categories you would like to change.",
                                      "Current Monster Statistics",
                                      ["Strength", "Speed", "Stealth",
                                       "Cunning", "I don't want "
                                                  "to change anything"])

print(card_lst)
