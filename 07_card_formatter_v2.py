"""
Card formatter version 2
More code added, such as emojis around the characteristics of the monster card.
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
    print("~" * 25)
    print(emoji_card)
    print("~" * 25)
