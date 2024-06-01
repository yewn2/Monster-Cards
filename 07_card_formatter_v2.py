"""
Card formatter version 2
More code added, such as emojis around the characteristics of the monster card.
This is the first trial of this component, and I have used a multiplier to add the formatting
around the card.
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
    emoji_lst = list(emoji_card[:(emoji_card.find("Strength"))])
    print(emoji_lst)
    print("~" * 25)
    print(emoji_card)
    print("~" * 25)
