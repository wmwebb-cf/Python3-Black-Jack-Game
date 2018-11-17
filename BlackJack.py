'''
Black Jack Game
'''

'''
---> This code block will be needed if associating each card with a different
asset in the game.

h_num = list(range(2, 10))
h_face = [10, 10, 10, 10]
h_ace = [1, 11]
hearts = h_num + h_face + h_ace

d_num = list(range(2, 10))
d_face = [10, 10, 10, 10]
d_ace = [1, 11]
diamonds = d_num + d_face + d_ace

c_num = list(range(2, 10))
c_face = [10, 10, 10, 10]
c_ace = [1, 11]
clubs = c_num + c_face + c_ace


s_num = list(range(2, 10))
s_face = [10, 10, 10, 10]
s_ace = [1, 11]
spades = s_num + s_face + s_ace
'''


import random
'''
Creates the four different suits (Heart, Diamonds, Clubs, and Spades for a deck
of cards.
'''
##h_num = list(range(2, 10))
##h_face = [10, 10, 10, 10]
##h_ace = [1, 11]
##hearts = h_num + h_face + h_ace
##diamonds = h_num + h_face + h_ace
##clubs = h_num + h_face + h_ace
##spades = h_num + h_face + h_ace
##
##deck = hearts + diamonds + clubs + spades
###print(deck)

def game_play():
    '''
    Creates the four different suits (Heart, Diamonds, Clubs, and Spades for a deck
    of cards.
    '''
    h_num = list(range(2, 10))
    h_face = [10, 10, 10, 10]
    h_ace = [1, 11]
    hearts = h_num + h_face + h_ace
    diamonds = h_num + h_face + h_ace
    clubs = h_num + h_face + h_ace
    spades = h_num + h_face + h_ace

    deck = hearts + diamonds + clubs + spades
    #print(deck)

    '''
    Introduces the player to the dealer.
    -> Takes input from the user
    -> Selects a dealer's name by random from a list of names
    '''

    # deal the hands
    dealer_names = ['Roscoe', 'Mr. Vickers', 'Big Tuna', 'Rat King']
    player = input(f'Player, what is your name: ').capitalize()
    house = random.choice(dealer_names)

    '''
    Deals a hand to the dealer and a player
    -> Selects two numbers from the deck at random
    -> The two numbers are added to the hand
    -> Determines if the initial hand is a winner or bust
    '''

    h_one = random.choice(deck)
    h_two = random.choice(deck)
    p_one = random.choice(deck)
    p_two = random.choice(deck)
    h_hand = [h_one, h_two]
    p_hand = [p_one, p_two]
    
    

##'''
##Introduces the player to the dealer.
##-> Takes input from the user
##-> Selects a dealer's name by random from a list of names
##'''
##
### deal the hands
##dealer_names = ['Roscoe', 'Mr. Vickers', 'Big Tuna', 'Rat King']
##player = input(f'Player, what is your name: ').capitalize()
##house = random.choice(dealer_names)
##
##'''
##Deals a hand to the dealer and a player
##-> Selects two numbers from the deck at random
##-> The two numbers are added to the hand
##-> Determines if the initial hand is a winner or bust
##'''
##
##h_one = random.choice(deck)
##h_two = random.choice(deck)
##p_one = random.choice(deck)
##p_two = random.choice(deck)
##h_hand = [h_one, h_two]
##p_hand = [p_one, p_two]

    def clear():
        h_hand.clear()
        p_hand.clear()
        # print(h_hand, p_hand)

    def deal():
        print()
        print()
        print(f'{house} represents The House vs {player}')
        print()
        print()
        print(f'LET\'S PLAY BLACKJACK!!! {player} here are your cards...')
        print(f'{player}: {p_hand}')

        h = sum(h_hand)
        p = sum(p_hand)
        if p > 21 and h < 21:
            return f'{player} bust, {house} WINS'
        elif h > 21 and p < 21:
            return f'House bust, {player} Wins'
        elif p == 21 and h != 21:
            return f'Twenty-One, {player} WINS!'
        elif h == 21 and p != 21:
            return f'Twenty-One, {house} WINS!'
        

    '''

    '''
    def bust():
        if sum(p_hand) > 21:
            return f'{house} WINS, {player} BUSTS'
            replay()
            return
        elif sum(h_hand) > 21:
            return f'{player} WINS, {house} BUSTS'
            replay()
            return
        return

    '''
    Dealer chooses if they want to get another card
    -> If they want a card, they will asked if they want another card
    -> If they don't want a card their turn will end
    '''

    def hit_house():
        x = input(f'{house}, would you like another card, yes or no: ')
        if x == 'yes':
            h_hand.append(random.choice(deck))
            print(f'{player}: {p_hand}, {house}: {h_hand}')
            if bust() != None:
                print(bust())
                replay()
            hit_house()
        elif x == 'no':
            return
        else:
            hit_house()
            
    '''
    Player chooses if they want to get another card
    -> If they want a card, they will asked if they want another card
    -> If they don't want a card their turn will end
    '''

    def hit_player():
        y = input(f'{player}, would you like another card, yes or no: ')
        if y == 'yes':
            p_hand.append(random.choice(deck))
            print(f'{player}: {p_hand}')
            if bust() != None:
                print(bust())
                replay()
            hit_player()
        elif y == 'no':
            return
        else:
            hit_player()


    '''
    Determines the winner
    -> Use sum() to turn hand into an integer
    -> Also determines if one of the player Busts 
    '''
    def winner():
        if sum(h_hand) > 21:
            print(f'{player} WINS!')
        elif sum(p_hand) > 21:
            print(f'{house} WINS!')
        elif 21 >= sum(h_hand) and sum(h_hand) > sum(p_hand):
            print(f'{house}, WINS')
        elif sum(h_hand) < sum(p_hand) and sum(p_hand) <= 21:
            print(f'{player}, WINS')
        else:
            print(f'{house} and {player} TIES!')
        
    '''
    Asks to player if they would like to play another game
    '''

    def replay():
        play_again = input(f'Would you like to play again? yes or no: ')
        if play_again == 'yes':
            clear()
            game_play()
        elif play_again == 'no':
            print(f'Thanks for playing')
            quit()
        else:
            print(f'Choose yes or no.')
            replay()
        return
            
    '''
    The game_play() function uses all the functions to create a game for the player
    '''
    deal()
    hit_house()
    hit_player()
    winner()
    replay()

game_play()






