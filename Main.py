import random

deck_array = ["A", "A", "A", "A", "2", "2", "2", "2", "3", "3", "3", "3", "4",
              "4", "4", "4", "5", "5", "5", "5", "6", "6", "6", "6", "7", "7",
              "7", "7", "8", "8", "8", "8", "9", "9", "9", "9", "10", "10",
              "10", "10", "J", "J", "J", "J", "Q", "Q", "Q", "Q", "K", "K", "K", "K"]
player_hand = []
computer_hand = []
player_total = 0
computer_total = 0


def shuffledeck(array):
    deck = array
    for i in range(len(deck)):
        while i > 0:
            i *= -1
            randomnumber = random.randint(0, 51)
            temp = deck[i]
            deck[i] = deck[randomnumber]
            deck[randomnumber] = temp
    print(deck)
    return deck


def drawcard(array):
    draw = array[-1]
    return draw


def get_total(input_hand):
    print(input_hand)
    sum = 0
    for i in range(len(input_hand)):
        if str(input_hand[i]) == "A":
            value = 1
        elif str(input_hand[i]) == "J":
            value = 11
        elif str(input_hand[i]) == "Q":
            value = 12
        elif str(input_hand[i]) == "K":
            value = 13
        else:
            value = int(input_hand[i])
        sum += value
    print("The total of the hand is at " + str(sum))
    return sum


def is_bust(input_hand):
    sum = get_total(input_hand)
    busted = False
    if sum > 21:
        print("The hand is a bust")
        busted = True
    return busted


def dealcards(inputdeck, p_hand, c_hand):
    p_hand.append(inputdeck[-1])
    del inputdeck[-1]
    c_hand.append(inputdeck[-1])
    del inputdeck[-1]
    p_hand.append(inputdeck[-1])
    del inputdeck[-1]
    c_hand.append(inputdeck[-1])
    del inputdeck[-1]
    return inputdeck


def main():
    shuffledeck(deck_array)
    dealcards(deck_array, player_hand, computer_hand)
    if is_bust(player_hand) == False:
        print("let's play")
    else:
        print("game over, player busted")
        # play the game
    # if the user decides to hit


main()


# Create a deck of 52 cards
    # shuffle the deck
    # deal cards
    # display total for the player
    # Give the player their options
    # Player chooses an option
        # Hit or Stay
        # if Hit
            # Draw card
            # Recalculate the total
            # check for bust
            # player chooses an option...
        # if stay
            # Turn goes to Computer for auto playing their side
            # lookup dealer rules for when the dealer is and isn't forced to hit
    # determine the winner if neither player busts
    # if a player busts, the other wins automatically
    # add in the option to gamble?
