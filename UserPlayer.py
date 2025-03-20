from DecisionMaker import DecisionMaker
from Phrase import Phrase


class UserPlayer:
    def __init__(self, language):
        self.language = language
        self.game_log = []
        self.decisionMaker = DecisionMaker(language)
        self.input_secret_code()

    def input_secret_code(self):
        print(Phrase.autoSecretCode[self.language], self.decisionMaker.secret_code)
        guess = input(Phrase.promptToSecretCode[self.language])
        if self.is_correct(guess):
            self.decisionMaker.secret_code = guess
            print(Phrase.secretCode[self.language], self.decisionMaker.secret_code)
        else:
            print(Phrase.secretCode[self.language], self.decisionMaker.secret_code)

    def next_question(self):
        print(Phrase.calculateHint[self.language])
        hint = self.get_hint()
        print(Phrase.hint[self.language], hint)
        while True:
            guess = input(Phrase.promptForGuess[self.language])
            if self.is_correct(guess) and not self.is_number_in_game_log(guess):
                return guess
            else:
                print(Phrase.incorrectInput[self.language])

    def get_response(self, guess):
        return DecisionMaker.get_bulls_cows(self.decisionMaker.secret_code, guess)

    def add_entry_to_game_log(self, guess, response):
        self.game_log.append([guess, response])

    def is_correct(self, guess):
        if guess in self.decisionMaker.full:
            return True
        else:
            return False

    def is_number_in_game_log(self, number):
        for entry in self.game_log:
            if number in entry:
                return True
        return False

    def verify(self, code):
        for number, answer in self.game_log:
            if DecisionMaker.get_bulls_cows(code, number) != answer:
                print(Phrase.errorInAnswer[self.language], number, answer)
                return
        print(Phrase.errorInCode[self.language])

    def get_hint(self):
        # сначала дает случайное число
        if len(self.game_log) == 0:
            hint = self.decisionMaker.pick()
        else:
            # мало ли, а вдруг
            # что-то пошло не так, надо разбираться
            if len(self.decisionMaker.decisions_field) == 0:
                print(Phrase.errorInCode[self.language])
                print(self.game_log)
                # code = input(Phrase.somethingWrong[self.language])
                # self.verify(code)
                hint = ''
            elif len(self.decisionMaker.decisions_field) == 1:
                hint = self.decisionMaker.decisions_field[0]
            else:
                hint = self.decisionMaker.get_next_guess(self.game_log[-1][0], self.game_log[-1][1])
        return hint
