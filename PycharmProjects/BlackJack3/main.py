import random


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


class Console:
    myHand = "_hand"
    myScore = "_score"
    helpme = "help"
    moreCards = "_hitme"
    noMoreCards = "_enough"
    newGame = "_start"
    stopGame = "_stop"
    leaveGame = "_endgame"

    def blackJack(self):
        print("BLACKJACK, YOU WON!\ndo you wish to try again?")

    def toMuch(self):
        print('Your score over 21, you lost, prepare your cash!\ndo you wish to try again?')

    def dealerWon(self, score, hand, sScore, sHand):
        print('your hand:', hand, '\nand dealers hand:', sHand,
              'dealer score is:', sScore, '\nand your score is:', score, '\nso...\nYou lost...',
              '\ndo you wish to try again?')

    def dealerLost(self, score, hand, sScore, sHand):
        print('your hand:', hand, '\nand dealers hand:', sHand,
              'dealer score is too big\nso...\nYOU WON!',
              '\ndo you wish to try again?')

    def score(self, score):
        print('now your score is:', score)

    def nextIteration(self, score, hand, sScore, sHand):
        getText = input("what you gonna do? \n> ")
        if getText == Console.helpme:
            print(help)
            self.nextIteration(score, hand, sScore, sHand)

        elif getText == Console.moreCards:
            score, hand = Game().newCard(score, hand, 0)
            Game().checkScore(score, hand, sScore, sHand)

        elif getText == Console.noMoreCards:
            Game().dealerGame(score, hand, sScore, sHand)

        elif getText == Console.myHand:
            print(hand)
            self.nextIteration(score, hand, sScore, sHand)

        elif getText == Console.myScore:
            Console().score(score)

        elif getText == Console.stopGame:
            print('I will accept your surrender!')
            return

        else:
            print('wrong command, try again')
            self.nextIteration(score, hand, sScore, sHand)

help = 'help log:\n' + Console.stopGame + ' - end game\n' + Console.moreCards + ' - more cards\n' + \
       Console.noMoreCards + ' - no more cards\n' + Console.myHand + ' - all your cards\n' + \
       Console.myScore + ' - check your score\n' + Console.helpme + ' - commands'


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

    def checkScore(self, score, hand, sScore, sHand):
        if score == 21:
            Console().blackJack()

        elif score > 21:
            Console().toMuch()

        elif score < 21:
            Console().score(score)
            Console().nextIteration(score, hand, sScore, sHand)

    def dealerGame(self, score, hand, sScore, sHand):
        if sScore > 21:
            Console().dealerLost(score, hand, sScore, sHand)

        elif score < sScore or sScore == 21:
            Console().dealerWon(score, hand, sScore, sHand)

        else:
            sScore, sHand = self.newCard(sScore, sHand, 1)
            self.dealerGame(score, hand, sScore, sHand)

    def newGame(self):
        score = 0
        hand = ''
        sScore = 0
        sHand = ''
        print('new game started')

        sScore, sHand = self.newCard(sScore, sHand, 1)
        print('one of dealers card is ', sHand)
        sScore, sHand = self.newCard(sScore, sHand, 1)
        score, hand = self.newCard(score, hand, 0)
        score, hand = self.newCard(score, hand, 0)
        print('now your score is:', score)

        Console().nextIteration(score, hand, sScore, sHand)
        return

print(help)
while True:
    print('\nprint', Console.newGame, 'to start new game, or', Console.leaveGame, 'to leave.')
    phrase = input("> ")
    if phrase == Console.newGame:
        Game().newGame()
    elif phrase == Console.leaveGame:
        print('game ended...')
        break
    else:
        print('wrong command, try again')
