from random import random, choice

from Phrase import Phrase


class DecisionMaker:
    def __init__(self, language):
        self.source_set = '0123456789'
        self.possible_answers_set = [0, 1, 2, 3, 4, 10, 11, 12, 13, 20, 21, 22, 30, 40]
        self.full = []
        self.get_full(self.source_set)
        self.decisions_field = self.full
        self.secret_code = self.pick()
        self.language = language

    def pick(self):
        """
        function picks up a random 4-digit string to guess by user
        :return puzzle: 4-digit string to guess by user
        """
        numeric = self.source_set
        puzzle = ''
        while len(puzzle) != 4:
            var = numeric[int(random() * len(numeric))]
            puzzle += var
            numeric = numeric.replace(var, '')
        return puzzle

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

    def get_full(self, source_set, subset=''):
        """
        A recursive function that creates a list of possible permutations from a given set of characters.
        :param source_set: a set of given characters
        :param subset: a set of specified length of characters
        """
        if len(subset) == 4:
            self.full.append(subset)
        else:
            for symbol in source_set:
                self.get_full(source_set.replace(symbol, ''), subset + symbol)

    def narrow_decisions_field(self, guess, response):
        new_decision_field = []
        for number in self.decisions_field:
            if DecisionMaker.get_bulls_cows(number, guess) == response:
                new_decision_field.append(number)
        self.decisions_field = new_decision_field

    # distribution = {40: 1, 30: 20, ...}
    def get_distribution(self, guess):
        distribution = {answer: [] for answer in self.possible_answers_set}
        for number in self.decisions_field:
            distribution[DecisionMaker.get_bulls_cows(number, guess)].append(number)
        return distribution

    # baskets = {0:360, 1:1440, 2:1260, ...}
    def get_baskets_amounts(self, guess):
        basket = {outcome: 0 for outcome in self.possible_answers_set}
        for number in self.decisions_field:
            basket[DecisionMaker.get_bulls_cows(guess, number)] += 1
        baskets = []
        for value in basket.values():
            if value != 0:
                baskets.append(value)
        baskets.sort(reverse=True)
        return baskets

    # after_sort = {'0123':[360, 120, 20, ...], ...}
    def get_all_baskets_amounts(self, guess_field):
        baskets = {}
        i = 1
        for number in guess_field:
            print(f"\r {Phrase.analyzing[self.language]} {i/(len(guess_field)): .1%}", end='')
            baskets[number] = self.get_baskets_amounts(number)
            i += 1
        print('\r ')
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

    # use the function in optimization whey guess_field < full
    # def get_optimal_list(self, guess, response, guess_field):
    def get_optimal_list(self, guess_field):
        baskets = self.get_all_baskets_amounts(guess_field)
        optimal_list = DecisionMaker.get_shallowest_baskets(baskets)
        return optimal_list

    def get_next_guess(self, guess, response):
        optimization = False
        if len(self.decisions_field) == len(self.full):
            optimization = True
        if optimization:
            return self.get_second_guess_optimising(guess, response)
        else:
            self.narrow_decisions_field(guess, response)
            optimal_list = self.get_optimal_list(self.full)
            return choice(optimal_list)

    def get_second_guess_optimising(self, guess, response):
        distribution = self.get_distribution(guess)
        if response == 0:
            next_guess = choice(distribution[0])
        elif response == 1:
            next_guess = choice(distribution[1])
        elif response == 2:
            optimal_list = self.get_optimal_list(distribution[3])
            next_guess = choice(optimal_list)
        elif response == 3:
            optimal_list = self.get_optimal_list(distribution[2])
            next_guess = choice(optimal_list)
        elif response == 4:
            optimal_list = self.get_optimal_list(distribution[3] + distribution[13])
            next_guess = choice(optimal_list)
        elif response == 10 or response == 11 or response == 12 or response == 30:
            next_guess = choice(distribution[20])
        elif response == 13:
            optimal_list = self.get_optimal_list(distribution[3] + distribution[12] + distribution[21])
            next_guess = choice(optimal_list)
        elif response == 20 or response == 21:
            next_guess = choice(distribution[11])
        elif response == 22:
            next_guess = choice(distribution[11] + distribution[12])
        else:
            next_guess = choice(distribution[11] + distribution[12])
        self.narrow_decisions_field(guess, response)
        return next_guess
