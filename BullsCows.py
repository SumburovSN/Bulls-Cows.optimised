from Phrase import Phrase
from Colors import Colors
from CompPlayer import CompPlayer
from UserPlayer import UserPlayer


class BullsCows:
    def __init__(self, language, user=None):
        self.player1 = CompPlayer(language)
        if user:
            self.player2 = UserPlayer(language)
        else:
            self.player2 = CompPlayer(language)
        self.isGame = True
        self.language = language

    def start(self):
        move = 1
        while self.isGame:
            print(f'{Colors.HEADER}{Phrase.move[self.language]}', move)
            guess1 = self.player1.next_question()
            print(f'{Colors.BLUE}{Phrase.player1guess[self.language]}', guess1)
            response2 = self.player2.get_response(guess1)
            print(f'{Colors.GREEN}{Phrase.player2response[self.language]}', self.format_response(response2))
            self.player1.add_entry_to_game_log(guess1, response2)
            guess2 = self.player2.next_question()
            print(f'{Colors.GREEN}{Phrase.player2guess[self.language]}', guess2)
            response1 = self.player1.get_response(guess2)
            print(f'{Colors.BLUE}{Phrase.player1response[self.language]}', self.format_response(response1))
            print(f'{Colors.HEADER}')
            self.player2.add_entry_to_game_log(guess2, response1)
            if response2 == 40 or response1 == 40:
                self.isGame = False
                self.print_winner(response1, response2)
            if len(self.player1.decisionMaker.decisions_field) == 0 or \
                    len(self.player2.decisionMaker.decisions_field) == 0:
                self.isGame = False
            move += 1

    def format_response(self, response):
        bulls = round(response / 10)
        cows = response - bulls * 10
        return Phrase.bulls[self.language] + str(bulls) + " " + Phrase.cows[self.language] + str(cows)

    def print_winner(self, response1, response2):
        if response1 == 40 and response2 == 40:
            print(Phrase.draw[self.language])
        elif response1 == 40:
            print(Phrase.player2won[self.language])
        elif response2 == 40:
            print(Phrase.player1won[self.language])
        print(self.player1.game_log)
        print(self.player2.game_log)


