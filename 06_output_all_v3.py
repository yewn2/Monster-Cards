"""
Output all version 2
Component 7 implemented into code
"""


def card_formatter(card):
    # finds the different stats and adds emojis to the card
    index = card.find("Strength")
    emoji_card = card[:index] + "💪" + card[index:]
    index = emoji_card.find("Speed")
    emoji_card = emoji_card[:index] + "🏃" + emoji_card[index:]
    index = emoji_card.find("Stealth")
    emoji_card = emoji_card[:index] + "🥷" + emoji_card[index:]
    index = card.find("Cunning")
    emoji_card = emoji_card[:(index + 3)] + "🧠" + emoji_card[(index + 3):]
    print("~" * 100)
    print(emoji_card)
    print("~" * 100)


def output_all(database):
    # loop to output all the cards in the database, one by one
    for card_ID, card_stats in database.items():
        stats_lst = []
        for stat, value in card_stats.items():
            stats_lst.append(f"{stat} : {value}")
        complete_stats = "\n\t".join(stats_lst)
        card_formatter(f"Monster card: {card_ID}\n\t"
                       f"{complete_stats}")


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

# main program
output_all(card_dict)
