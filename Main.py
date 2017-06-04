import random

deck_array = ["A", "A", "A", "A", "2", "2", "2", "2", "3", "3", "3", "3", "4",
              "4", "4", "4", "5", "5", "5", "5", "6", "6", "6", "6", "7", "7",
              "7", "7", "8", "8", "8", "8", "9", "9", "9", "9", "10", "10",
              "10", "10", "J", "J", "J", "J", "Q", "Q", "Q", "Q", "K", "K", "K", "K"]
player_hand = []
computer_hand = []
player_total = 0
computer_total = 0


def shuffle_deck(array):
    deck = array
    for i in range(len(deck)):
        while i > 0:
            i *= -1
            random_number = random.randint(0, 51)
            temp = deck[i]
            deck[i] = deck[random_number]
            deck[random_number] = temp
    return deck


def draw_card(array):
    draw = array[-1]
    del array[-1]
    return draw


def get_total(input_hand):
    total = 0
    for i in range(len(input_hand)):
        if str(input_hand[i]) == "A":
            value = 1
        elif str(input_hand[i]) == "J" or str(input_hand[i]) == "Q" or str(input_hand[i]) == "K":
            value = 10
        else:
            value = int(input_hand[i])
        total += value
    return total


def is_bust(input_hand):
    total = get_total(input_hand)
    if total > 21:
        print(input_hand)
        print("The hand is a bust")
        busted = True
        # End Round Here
    else:
        busted = False
    return busted


def deal_cards(input_deck, p_hand, c_hand):
    p_hand.append(input_deck[-1])
    del input_deck[-1]
    c_hand.append(input_deck[-1])
    del input_deck[-1]
    p_hand.append(input_deck[-1])
    del input_deck[-1]
    c_hand.append(input_deck[-1])
    del input_deck[-1]
    if is_bust(p_hand):
        return "game over"
    return input_deck


def play_dealer_hand(d_hand, deck):
    total = get_total(d_hand)
    print("The dealer's hand is: " + str(d_hand))
    print("The total of his hand is " + str(total))
    is_bust(d_hand)
    if total < 17:
        d_hand.append(draw_card(deck))
        total = get_total(d_hand)
        print("The dealer drew a " + str(d_hand[-1]))
        print("The dealer's hand is: " + str(d_hand))
        is_bust(d_hand)
        print("The total of his hand is " + str(total))
        if total < 17:
            d_hand.append(draw_card(deck))
            total = get_total(d_hand)
            print("The dealer drew a " + str(d_hand[-1]))
            print("The dealer's hand is: " + str(d_hand))
            is_bust(d_hand)
            print("The total of his hand is " + str(total))
            if total < 17:
                total = get_total(d_hand)
                print("The dealer drew a " + str(d_hand[-1]))
                print("The dealer's hand is: " + str(d_hand))
                is_bust(d_hand)
                print("The total of his hand is " + str(total))


def hand_options(array, hand, comp_hand):
    total = get_total(hand)
    print("Your hand is: " + str(hand))
    print("The total of your hand is at " + str(total))
    print("You can press 'h' to Hit and get another card")
    print("Or you can press 's' to Stay and turn it over to the dealer")
    choice = input("What would you like to do?")
    if choice == "h":
        hand.append(draw_card(array))
    else:
        print("You chose to stay where you are with a total of: " + str(total))
        print("Time for the dealer to go...")
        play_dealer_hand(comp_hand, array)
    return str(choice)


def main():
    shuffle_deck(deck_array)
    deal_cards(deck_array, player_hand, computer_hand)
    if is_bust(player_hand):
        return "game over"
    choice = hand_options(deck_array, player_hand, computer_hand)
    if is_bust(player_hand):
        return "game over"
    if choice == "h":
        choice = hand_options(deck_array, player_hand, computer_hand)
        if is_bust(player_hand):
            return "game over"
        if choice == "h":
            if is_bust(player_hand):
                return "game over"
    # Check the scores and figure out the winner
    p_total = get_total(player_hand)
    c_total = get_total(computer_hand)
    if p_total > c_total:
        print("You won!")
        print("Your hand total was " + str(p_total))
        print("The computer total was " + str(c_total))
    if c_total > p_total:
        print("You lost!")
        print("Your hand total was " + str(p_total))
        print("The computer total was " + str(c_total))

main()


# if a player busts, the other wins automatically
# add in the option to gamble?
