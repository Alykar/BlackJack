import random

help = '"_stop" - end game\n"_hitme" - more cards\n' \
       '"_enough" - no more cards\n"_hand" - all your cards\n' \
       '"_help" - view commands'


def fitScore(n, score):
    if n > 9:
        score += 10
    else:
        score += n + 1
    return score


def filHand(card, hand):
    if hand == '':
        hand += card
    else:
        hand += ' and ' + card
    return hand


def newCard(score, hand, hide):
    suit = ['hearts', 'clubs', 'spades', 'diamonds']
    cards = ['one', 'two', 'three', 'four', 'five',
             'six', 'seven', 'eight', 'nine', 'ten',
             'jack', 'queen', 'king', 'ace']
    n = random.randint(1, 13)
    card = cards[n] + ' of ' + suit[random.randint(0, 3)]
    if hide == 0:
        print('you got new card:', card)

    score = fitScore(n, score)
    hand = filHand(card, hand)
    return score, hand


def nextIteration(score, hand, sScore, sHand):
    phrase = input("what you gonna do? \n> ")
    if phrase == '_help':
        print(help)
        nextIteration(score, hand, sScore, sHand)
        return

    elif phrase == '_hitme':
        score, hand = newCard(score, hand, 0)
        sScore, sHand = newCard(sScore, sHand, 1)
        print('now your score is:', score)
        nextIteration(score, hand, sScore, sHand)
        return

    elif phrase == '_enough':
        print('your hand:', hand,'and dealers hand:', sHand, 'so...')
        if score > sScore:
            print('YOU WON!')
        else:
            print('You lost...')
        print("do you wish to try again?")
        return

    elif phrase == '_hand':
        print(hand)
        nextIteration(score, hand, sScore, sHand)
        return

def newGame():
    score = 0
    hand = ''
    sScore = 0
    sHand = ''
    print('new game started')
    score, hand = newCard(score, hand, 0)
    score, hand = newCard(score, hand, 0)
    print('now your score is:', score)

    sScore, sHand = newCard(sScore, sHand, 1)
    print('one of dealers card is ', sHand)
    sScore, sHand = newCard(sScore, sHand, 1)

    nextIteration(score, hand, sScore, sHand)
    return


while True:
    print(help, '\nprint "_start" to start new game, or "_endgame" to leave.')
    phrase = input("> ")
    if phrase == '_start':
        newGame()
    elif phrase == '_endgame':
        break