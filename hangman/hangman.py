import random

COLORS = {
    "o": "\033[33m",
    "g": "\033[92m",
    "y": "\033[93m",
    "rst": "\033[00m",
}


def print_color(m: str, c: str) -> None:
    print(f"{COLORS[c]}{m}{COLORS['rst']}")


class Hangman:
    def __init__(self, f: str) -> None:
        self.word_list = self.read_word_list(f)
        self.word = self.get_word(self.word_list)
        self.found = ["_"] * len(self.word)
        self.already_guessed = set()
        self.correct = 0
        self.guesses = 0
        self.game_loop()

    def read_word_list(self, filename: str) -> list:
        f = open(filename, "r")
        words = []
        for w in f:
            words.append(w.rstrip())
        return words

    def get_word(self, words: list) -> str:
        return random.choice(words)

    def make_guess(self) -> None:
        guess = input("\nMake a guess: ").lower()
        found = False

        if not guess[0].isalnum():
            print("\nInvalid input, try again")
            return

        if guess[0] in self.already_guessed:
            print_color(f"\n{guess[0]} was already guessed, try again", "y")
            return

        for i in range(len(self.word)):
            if self.word[i] == guess[0]:
                found = True
                self.found[i] = guess[0]
                self.correct += 1
                if guess[0] not in self.already_guessed:
                    print_color(f"\n{guess[0]} is a match!", "g")
                    self.already_guessed.add(guess[0])
                    print(self.get_picture(self.guesses))

        if self.correct == len(self.word):
            print_color("You win!", "g")
            print_color(f"The word was: {self.word}", "g")
            exit()

        if not found:
            print_color(f"\n{guess[0]} is not a match :(", "o")
            self.guesses += 1
            self.already_guessed.add(guess[0])
            print(self.get_picture(self.guesses))
            if self.guesses == 7:
                print_color("Game Over", "o")
                print_color(f"The word was: {self.word}", "o")
                exit()
        self.print_game_state()

    def game_loop(self):
        while True:
            self.make_guess()

    def print_game_state(self):
        for i in self.found:
            print(f"{i}", end=" ")
        print("")

    def get_picture(self, state):
        states = {
            0: """
            -------
            |     |
            |
            |
            |
            |
            |
            """,
            1: """
            -------
            |     |
            |     @
            |
            |
            |
            |
            """,
            2: """
            -------
            |     |
            |     @
            |     !
            |
            |
            |
            """,
            3: """
            -------
            |     |
            |     @
            |     !
            |     !
            |
            |
            """,
            4: """
            -------
            |     |
            |     @
            |    /!
            |     !
            |
            |
            """,
            5: """
            -------
            |     |
            |     @
            |    /!\\
            |     !
            |
            |
            """,
            6: """
            -------
            |     |
            |     @
            |    /!\\
            |     !
            |    /
            |
            """,
            7: """
            -------
            |     |
            |     @
            |    /!\\
            |     !
            |    / \\
            |
            """,
        }
        return states[state]


if __name__ == "__main__":
    dead_dude = Hangman("words.txt")
