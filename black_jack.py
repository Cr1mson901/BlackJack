#Create a deck of cards:Done
#ask the user if they wish to play:Done
#show the player the two cards the they have:Done
#show one of the dealers cards:Done
#add new card to players deck if they hit:Done
#if over 21 bust:Done
#else ask again:Done
#add bank roll mechanic:Done
import random
import os
#Creates a 52 deck of cards, 1 is Ace, 11-13 are face cards
deck = {}
face_cards = {1:'A',11:'J', 12:'Q', 13:'K'}
def build_deck(decks):
    for i in range(1,14):
        deck[i] = decks * 4

#asks if the user would like to play blackjack, accepts any word starting with y
os.system('cls')
#adds new cards according to the count
def new_card(count):
    cards = 0
    hand = []
    while cards < count:
        card = random.randint(1, 13)
        #checks if there are any remaing cards of that value in the deck
        if deck.get(card) != 0:
            deck[card] = deck.get(card) - 1
            cards += 1
            hand.append(card)
    return hand


#converts card to face card for the purpose of printing to user
def swap(hand):
    hand = [face_cards.get(card) if card in face_cards else card for card in hand]
    return hand
            
#adds a card to hand and prints the results
def hit(hand):
    hand.append(new_card(1)[0])

#asks the player if they want to hit
def player_hit(hand):
    if input('Type "h" to hit, or "p" to pass: ') == 'h':
        hit(hand)
        print(swap(hand))
        count = total(hand)
        if count > 21:
            print('You Busted')
            return 0
        elif count == 21:
            return 1
        else:
            return player_hit(hand)
            
    else:
        return 1

#plays one round off black jack
def play(num_decks, bank_roll):   
    game_req = input("Do you want to play a hand of blackjack? Type 'y' or 'n'.\n")
    if game_req[0].lower() !=  'y':
        exit()
    #clears terminal
    os.system('cls')
    if sum(deck.values()) < 30:
        build_deck(num_decks)
    bet = int(input('Your bankroll is {}. How much would you like to bet?'.format(bank_roll)))

    player_cards = new_card(2)
    com_cards = new_card(2)
    print('Your cards: {}'.format(swap(player_cards)))
    print('Computer\'s first card: {}'.format(swap(com_cards)[0]))
    #If player has black jack they win    
    if total(player_cards) == 21:
        print('Winner Winner Chicken Dinner')
        bank_roll += int(bet * 1.5)
        play(num_decks, bank_roll)
        
    if player_hit(player_cards) == 1:
        while total(com_cards) < 16:
            hit(com_cards)
            if total(com_cards) > 21:
                print('Computer\'s final hand: {}'.format(swap(com_cards)))
                print('Dealer busted, you win')
                bank_roll += bet
                play(num_decks, bank_roll)
        #compare and decide winner
        print('Your final hand: {}'.format(swap(player_cards)))
        print('Computer\'s final hand: {}'.format(swap(com_cards)))
        if total(player_cards) > total(com_cards):
            print('You win')
            bank_roll += bet
        elif total(player_cards) < total(com_cards):
            print('Dealer wins')
            bank_roll -= bet
        elif total(player_cards) == total(com_cards):
            print('Its a tie')
    else:
        bank_roll -= bet      
    play(num_decks, bank_roll)
#Sums the hand using 10 for face value and checking if it can use Ace as an 11 without going over
#does not work as intended if a hand has multiple Aces ie [13, 1, 1] would give a less then inteded result. 
#Unsure how to fix for now, maybe if that happens replace 1,1 with just a 2. But I am tired with this project
def total(hand):
    total = 0
    hand.sort(reverse = True)
    for card in hand:
        if card > 10:
            total += 10
        elif card == 1:
            try:
                if total + 11 > 21:
                    raise ValueError
                else:
                    total += 11
            except:
                total += 1
        else:
            total += card
    return total

#Play(Number of Decks, Starting bank roll amount)
play(3, 100)        
    
    
        

       
