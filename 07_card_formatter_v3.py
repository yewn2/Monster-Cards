"""
Card formatter version 3
Second trial code of this component
This trial involves using a short checker to check the length of the 'Monster Card: ****' line in
order to correctly implement the right amount of characters.
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
    # checks the length of the first line and changes the amount of '~' characters appropriately
    around = len(emoji_card[:(emoji_card.find("\n"))]) * "~"
    print(around)
    print(emoji_card)
    print(around)
