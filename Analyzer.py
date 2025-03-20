import pickle
import random
from GuessSelector import GuessSelector as selector


class Analyzer:
    @staticmethod
    def save_optimizer_map(optimizer_map: dict, level: int):
        with open("resources/" + str(level) + ".dic", "wb") as file:
            pickle.dump(optimizer_map, file)

    @staticmethod
    def load_optimizer_map(level: int):
        with open("resources/" + str(level) + ".dic", "rb") as file:
            optimizer_map = pickle.load(file)
            return optimizer_map

    @staticmethod
    def save_initial_distribution(initial_distribution: dict):
        with open("resources/" + 'initial_distribution' + ".dic", "wb") as file:
            pickle.dump(initial_distribution, file)

    @staticmethod
    def load_initial_distribution():
        with open("resources/" + 'initial_distribution' + ".dic", "rb") as file:
            initial_distribution = pickle.load(file)
            return initial_distribution

    @staticmethod
    def build_first_level_optimization(first_guess):
        full_set = []
        selector.get_full(full_set, '0123456789')
        print(len(full_set))

        initial_distribution = selector.get_distribution(full_set, first_guess)

        # собираем информацию для ускорения выбора попытки (guess) путем уменьшения поля для выбора (guess_field), которое
        # изначально составляют все элементы (full_set). Исключаем 40 - 4 быка - само число.
        # формат optimizer_map: {outcome: [locale set(), amounts in basket]}, например {4: [(3, 13), 56]}
        first_optimizer_map = {}
        for response in selector.possible_answers_set[0:13]:
            optimal_baskets = selector.get_shallowest_baskets(
                selector.get_all_baskets_amounts(initial_distribution[response], full_set))
            locale = set()
            for numeric in optimal_baskets:
                locale.add(selector.get_bulls_cows(first_guess, numeric))
            first_optimizer_map.update({response: [locale, len(optimal_baskets)]})

        # print(first_optimizer_map)
        Analyzer.save_optimizer_map(first_optimizer_map, 1)
        Analyzer.save_initial_distribution(initial_distribution)

    # under development
    @staticmethod
    def build_second_level_optimization():
        initial_distribution = Analyzer.load_initial_distribution()

        # а теперь поработаем с выходом после 1 вопроса с ответом 2 быка 2 коровы, где 936 элементов в поле решений
        second_guess = random.choice(initial_distribution[11])
        print('second_guess:', second_guess)
        second_distribution = selector.get_distribution(initial_distribution[22], second_guess)

        for label in second_distribution:
            print(label, len(second_distribution[label]))
        full_set = []
        selector.get_full(full_set, '0123456789')
        second_optimizer_map = {}
        included = 0
        for response in selector.possible_answers_set[0:13]:
            optimal_baskets = selector.get_shallowest_baskets(
                selector.get_all_baskets_amounts(second_distribution[response], full_set))
            locale = set()
            for numeric in optimal_baskets:
                locale.add(selector.get_bulls_cows(second_guess, numeric))
                # print(numeric in initial_distribution[1])
                included += 1
            second_optimizer_map.update({response: [locale, len(optimal_baskets)]})

        print('included', included)
        # print(second_optimizer_map)
        Analyzer.save_optimizer_map(second_optimizer_map, 22)

    @staticmethod
    def get_example_initial_distribution(guess):
        full_set = []
        selector.get_full(full_set, '0123456789')

        initial_baskets = selector.get_distribution(full_set, guess)
        initial_distribution = []

        for outcome in initial_baskets:
            initial_distribution.append([outcome, len(initial_baskets[outcome])])
        initial_distribution.sort(key=lambda el: el[1], reverse=True)
        print(initial_distribution)


# guess is any from full_set, e.g. 1234
guess_example = '1234'
Analyzer.get_example_initial_distribution(guess_example)

# distribution for the optimization after first response
Analyzer.build_first_level_optimization('8031')
first_level = Analyzer.load_optimizer_map(1)
print(first_level)
for outcome in first_level:
    print(f"For outcome {outcome} optimal guesses are located in locale with outcome {first_level[outcome][0]} "
          f"and the amount of all optimal guesses is {first_level[outcome][1]}")


# def factorial(n):
    #     if n == 1:
    #         return 1
    #     else:
    #         return n * factorial(n - 1)
    #
    #
    # print(int(factorial(10) / factorial(10 - 4)))  # 5040

# under development
# Analyzer.build_second_level_optimization()

# second_level = Analyzer.load_optimizer_map(2)
# print(second_level)
