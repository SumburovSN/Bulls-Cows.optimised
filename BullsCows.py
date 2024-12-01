from CompPlayer import CompPlayer


class BullsCows:
    def __init__(self):
        self.player1 = CompPlayer()
        self.player2 = CompPlayer()
        self.isGame = True
        self.turn = 1

    def start(self):
        # number = ''
        move = 1
        while self.isGame:
            guess = self.player1.next_question()
            response = self.player2.get_response(guess)
            self.player1.add_entry_to_game_log(guess, response)
            if response == 40:
                self.isGame = False
            if len(self.player1.decisionMaker.decisions_field) == 0:
                self.isGame = False
            print('move', move, guess, response)
            move += 1


            # if self.turn == 1:
            #     if number:
            #         self.player1.get_response(number)
            #     self.player1.next_question()
            #     self.turn = 2
            # else:
            #     self.player2.next_move()
            #     self.turn = 1
