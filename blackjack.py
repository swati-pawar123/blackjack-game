
import random

#Declare Variables

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

playing = True

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of  " + self.suit


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = " "
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
            return "the deck has : " + deck_comp


    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value = self.value + values[card.rank]
        if card. rank == "Ace":
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:
    def __init__(self,total=100):
        self.total = total
        self.bet = 0


    def win_bet(self):
         self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


#Function defination

#Write function for taking bets
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet?  "))
        except ValueError:
            print("Sorry please provide integer")
        else:
            if chips.bet > chips.total:
                print("Sorry you do not have enough chips!", chips.total)
            else:
                break

#Write function for taking hits
def hit(deck, hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

#Write function to prompt the player to hit or stand
def hit_or_stand(deck, hand):
    global playing
    while True:
        x = input("Hit or Stand? Enter h or s")
        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print("player stands, dealers turn")
            playing = False
        else:
            print("Sorry! Please enter h or s only")
            continue
        break

#write function for win or lose
def player_wins(player,dealer,chips):
    print("player wins!")
    chips.win_bet()

def player_busts(player,dealer, chips):
    print("player bust!")
    chips.lose_bet()

def dealer_wins(player,dealer, chips):
    print("Dealer wins!")
    chips.win_bet()


def dealer_busts(player, dealer,chips):
    print("Dealer bust!, player wins!")
    chips.lose_bet()

def push(player, dealer):
    print("Dealer and player Tie!, PUSH")

#Write a function to display card
def show_some(player, dealer):
    print("Dealer Hand: ")
    print("one card hidden!")
    print(' ', dealer.cards[1])
    print('\n')
    print("players hand: ")
    for card in player.cards:
        print(card)


def show_all(player, dealer):
    print("Dealer Hand:  ")
    for card in dealer.cards:
        print(card)
    print('\n')
    print("Player Hand: ")
    for card in player.cards:
       print(card)


while True:
    print("Welcome to black jack")
    #create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

#set up the players chips
    player_chips = Chips()

#prompt the player for there bet
    take_bet(player_chips)

#show cards(but keep 1dealer card hidden)
    show_some(player_hand, dealer_hand)

    while playing: #recall this variable from our hit_or_stand function
        #prompt for player to hit or stand
        hit_or_stand(deck, player_hand)

        #show cards(one hidden for dealer)
        show_some(player_hand, dealer_hand)

        #if player hand exceeds 21 run player busts()& break out of loop

        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break

        #if player has not busted play dealer hand until dealer reaches 17

        if player_hand.value <= 21:
            while dealer_hand.value < player_hand.value:
                hit(deck, dealer_hand)

        # show all cards
        show_all(player_hand, dealer_hand)

        #run different winning sceneris
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)

#Inform player of thier total chips
    print("\n player total chips are", player_chips.total)

#Ask to play again
    new_game = int(input("Would you like to play another hand? Enter y or n: "))
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thanks for playing")
        break




