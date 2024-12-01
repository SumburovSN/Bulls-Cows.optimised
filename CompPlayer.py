from DecisionMaker import DecisionMaker


class CompPlayer:
    def __init__(self):
        self.game_log = []
        self.decisionMaker = DecisionMaker()
        # self.decisions_field = full
        # self.isGame = True

    def next_question(self):
        # сначала дает случайное число
        if len(self.game_log) == 0:
            guess = self.decisionMaker.pick()
        else:
            # что-то пошло не так, надо разбираться
            if len(self.decisionMaker.decisions_field) == 0:
                code = input("Something wrong. Please, input your secret code for verification: ")
                self.verify(code)
                guess = ''
            elif len(self.decisionMaker.decisions_field) == 1:
                guess = self.decisionMaker.decisions_field[0]
                print('Your number is', self.decisionMaker.decisions_field[0])
            else:
                guess = self.decisionMaker.get_next_guess(self.game_log[-1][0], self.game_log[-1][1])
        return guess

    def get_response(self, guess):
        return DecisionMaker.get_bulls_cows(self.decisionMaker.secret_code, guess)

    def add_entry_to_game_log(self, guess, response):
        self.game_log.append([guess, response])

    def verify(self, code):
        for number, answer in self.game_log:
            if DecisionMaker.get_bulls_cows(code, number) != answer:
                print('Error in answer for ', number, answer)
                return
        print('The error in code for further correction...')


