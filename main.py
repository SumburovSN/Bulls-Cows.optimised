from BullsCows import BullsCows
from Phrase import Phrase

if __name__ == '__main__':
    choice = input("Choose the language for the game (1-Русский, 2-Français, 3-Deutsch, ""Other symbols-English): ")
    language = Phrase.check_language_choice(choice)
    if input(Phrase.promptToGameMode[language]) == "1":
        game = BullsCows(language, 1)
    else:
        game = BullsCows(language)
    game.start()
