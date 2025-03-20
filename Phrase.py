class Phrase:
    promptToGameMode = [
        "Choose game mode (1 - Comp vs User, other symbols - Comp vs Comp): ",
        "Выберите режим игры (1 — Компьютер против Пользователя, другие символы — Компьютер против Компьютера): ",
        "Sélectionner le mode de jeu(1 - Ordinateur contre Utilisateur, autres symboles - Ordinateur contre Ordinateur): ",
        "Spielmodus auswählen(1 – Computer vs. Benutzer, andere Symbole – Computer vs.Computer): ",
                 ]
    move = [
        "MOVE",
        "ХОД",
        "COUP",
        "ZUG"
    ]
    bulls = [
        "Bulls: ",
        "Быков: ",
        "Taureaux: ",
        "Bullen: "
    ]
    cows = [
        "Cows: ",
        "Коров: ",
        "Vaches: ",
        "Kühe:"
    ]
    player1guess = [
        "Player 1 guess:",
        "Догадка Игрока 1:",
        "Le joueur 1 devine:",
        "Vermutung von Spieler 1:"
    ]
    player2guess = [
        "Player 2 guess:",
        "Догадка Игрока 2:",
        "Le joueur 2 devine:",
        "Vermutung von Spieler 2:"
    ]
    player1response = [
        "Player 1 response:",
        "Ответ Игрока 1:",
        "Réponse du joueur 1:",
        "Antwort von Spieler 1:"
    ]
    player2response = [
        "Player 2 response:",
        "Ответ Игрока 2:",
        "Réponse du joueur 2:",
        "Antwort von Spieler 2:"
    ]
    player1won = [
        "Player 1 won",
        "Выиграл Игрок 1",
        "Le joueur 1 a gagné",
        "Spieler 1 hat gewonnen"
    ]
    player2won = [
        "Player 2 won",
        "Выиграл Игрок 2",
        "Le joueur 2 a gagné",
        "Spieler 2 hat gewonnen"
    ]
    draw = [
        "Draw",
        "Ничья",
        "Match nul",
        "Unentschieden"
    ]
    autoSecretCode = [
        "Your automatically generated guess number is",
        "Ваше загаданное число, сгенерированное автоматически, равно",
        "Votre numéro de supposition généré automatiquement est",
        "Ihre automatisch generierte Ratezahl lautet"
    ]
    promptToSecretCode = [
        "If you want to make a different wish, enter it here: ",
        "Если Вы хотите загадать другое, введите здесь: ",
        "Si vous souhaitez faire un souhait différent, indiquez-le ici :",
        "Wenn Du einen anderen Wunsch äußern möchtest, gib ihn hier ein:",
    ]
    secretCode = [
        "Your guessed number is",
        "Ваше загаданное число равно",
        "Votre numéro deviné est",
        "Ihre erratene Zahl ist"
    ]
    calculateHint = [
        "Calculating a hint...",
        "Вычисляю подсказку...",
        "Calculer un indice...",
        "Einen Hinweis berechnen..."
    ]
    hint = [
        "Clue:",
        "Подсказка:",
        "Indice:",
        "Hinweis:"
    ]
    promptForGuess = [
        "Enter your guess: ",
        "Введите Вашу догадку: ",
        "Entrez votre estimation: ",
        "Geben Sie Ihren Schätzwert ein: "
    ]
    analyzing = [
        "Analyzing...",
        "Анализирую...",
        "En train d'analyser...",
        "Analysieren..."
    ]
    incorrectInput = [
        "Incorrect input, try again",
        "Неверный ввод, попробуйте еще раз",
        "Entrée incorrecte, réessayez",
        "Falsche Eingabe, versuchen Sie es erneut"
    ]
    somethingWrong = [
        "Something wrong. Please, input your guess number for verification: ",
        "Что-то не так. Пожалуйста, введите загаданное число для проверки: ",
        "Quelque chose ne va pas. Veuillez entrer le numéro masqué pour vérifier: ",
        "Irgendwas stimmt nicht. Bitte geben Sie zur Überprüfung die versteckte Nummer ein: "
    ]
    errorInAnswer = [
        "Error in answer:",
        "Ошибка в ответе:",
        "Erreur dans la réponse:",
        "Fehler in der Antwort:"
    ]
    errorInCode = [
        "The error in code for further correction...",
        "Ошибка в коде для дальнейшего исправления...",
        "L'erreur dans le code pour une correction supplémentaire...",
        "Der Fehler im Code zur weiteren Korrektur..."
    ]

    def __init__(self, language_choice):
        self.language_choice = language_choice

    @staticmethod
    def check_language_choice(language):
        if language == "1":
            return 1
        elif language == "2":
            return 2
        elif language == "3":
            return 3
        else:
            return 0
