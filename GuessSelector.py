class GuessSelector:
    possible_answers_set = [0, 1, 2, 3, 4, 10, 11, 12, 13, 20, 21, 22, 30, 40]

    def __init__(self, full):
        self.full = full

    @staticmethod
    def get_bulls_cows(secret_code, guess):
        """
        the function gets answer for "Bulls&Cows" game by comparison 2 given codes
        :param secret_code: the string consisted of 4 different numeric symbols to be recognised
        :param guess: the string consisted of 4 different numeric symbols as an attempt to recognise the secret_code
        :return result: the number of template, e.g. 12 - 1 bull and 2 cows
        """
        bulls = 0
        cows = 0
        # check every 4 symbols of the attempt against the riddle
        for i in range(4):
            for k in range(4):
                if guess[i] == secret_code[k]:
                    if i == k:
                        # if symbol is in the same position it contributes to bulls
                        bulls += 1
                    else:
                        # if symbol is in the different position it contributes to cows
                        cows += 1
        # the response of template 12 (0, 22, etc.)
        return bulls * 10 + cows

    @staticmethod
    def narrow_decisions_field(decisions_field, guess, response):
        new_decisions_field = []
        for number in decisions_field:
            if GuessSelector.get_bulls_cows(number, guess) != response:
                new_decisions_field.append(number)
        return new_decisions_field

    # distribution = {40: 1, 30: 20, ...}
    @staticmethod
    def get_distribution(decisions_field, guess):
        distribution = {answer: [] for answer in GuessSelector.possible_answers_set}
        for number in decisions_field:
            distribution[GuessSelector.get_bulls_cows(number, guess)].append(number)
        return distribution

    @staticmethod
    def get_baskets_amounts(decisions_field, guess):
        basket = {outcome: 0 for outcome in GuessSelector.possible_answers_set}
        for number in decisions_field:
            basket[GuessSelector.get_bulls_cows(guess, number)] += 1
        baskets = []
        for value in basket.values():
            if value != 0:
                baskets.append(value)
        baskets.sort(reverse=True)
        return baskets

    @staticmethod
    def get_all_baskets_amounts(decisions_field, guess_field):
        baskets = {}
        for el in guess_field:
            print('\r' + el, end='')
            baskets[el] = GuessSelector.get_baskets_amounts(decisions_field, el)
        print('\n')
        after_sort = dict(sorted(baskets.items(), key=lambda item: item[1]))
        return after_sort

    @staticmethod
    def get_shallowest_baskets(baskets):
        shallowest = []
        optimal = list(baskets.values())[0]
        for k, v in baskets.items():
            if v == optimal:
                shallowest.append(k)
        return shallowest

    def get_next_guess(self, decisions_field, guess, response):
        GuessSelector.narrow_decisions_field(decisions_field, guess, response)
        guess_field = self.full
        baskets = GuessSelector.get_all_baskets_amounts(decisions_field, guess_field)
        GuessSelector.get_shallowest_baskets()


