import random

help = '"_stop" - end game\n"_hitme" - more cards\n' \
       '"_enough" - no more cards\n"_hand" - all your cards\n' \
       '"_help" - view commands'
class Card:
    def __init__(self,  name='', suit='', weight=0):
        self.name = name
        self.suit = suit
        self.weight = weight

    def __gt__(self, other):
        return self.weight > other.weight and other.weight < self.weight

    def __lt__(self, other):
        return self.weight < other.weight and other.weight > self.weight

    def __eq__(self, other):
        return self.weight == other.weight and other.weight == self.weight


class Game:
    def fitScore(self, n, score):
        if n > 8:
            score += 10
        else:
            score += n + 2
        return score

    def filHand(self, card, hand):
        if hand == '':
            hand += card
        else:
            hand += ' and ' + card
        return hand

    def newCard(self, score, hand, hide):
        suit = ['hearts', 'clubs', 'spades', 'diamonds']
        cards = ['two', 'three', 'four', 'five',
                 'six', 'seven', 'eight', 'nine', 'ten',
                 'jack', 'queen', 'king', 'ace']
        n = random.randint(0, 12)
        card = cards[n] + ' of ' + suit[random.randint(0, 3)]
        if hide == 0:
            print('you got new card:', card)

        score = self.fitScore(n, score)
        hand = self.filHand(card, hand)
        return score, hand

    def nextIteration(self, score, hand, sScore, sHand):
        phrase = input("what you gonna do? \n> ")
        if phrase == '_help':
            print(help)
            self.nextIteration(score, hand, sScore, sHand)

        elif phrase == '_hitme':
            score, hand = self.newCard(score, hand, 0)
            sScore, sHand = self.newCard(sScore, sHand, 1)
            print('now your score is:', score)
            self.nextIteration(score, hand, sScore, sHand)

        elif phrase == '_enough':
            print('your hand:', hand,'and dealers hand:', sHand, 'so...')
            if score > sScore:
                print('YOU WON!')
            else:
                print('You lost...')
            print("do you wish to try again?")

        elif phrase == '_hand':
            print(hand)
            self.nextIteration(score, hand, sScore, sHand)

    def newGame(self):
        score = 0
        hand = ''
        sScore = 0
        sHand = ''
        print('new game started')
        score, hand = self.newCard(score, hand, 0)
        score, hand = self.newCard(score, hand, 0)
        print('now your score is:', score)

        sScore, sHand = self.newCard(sScore, sHand, 1)
        print('one of dealers card is ', sHand)
        sScore, sHand = self.newCard(sScore, sHand, 1)

        self.nextIteration(score, hand, sScore, sHand)
        return


while True:
    print(help, '\nprint "_start" to start new game, or "_endgame" to leave.')
    phrase = input("> ")
    if phrase == '_start':
        Game().newGame()
    elif phrase == '_endgame':
        print('game ended...')
        break
