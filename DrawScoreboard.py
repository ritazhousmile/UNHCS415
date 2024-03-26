# huan zhou
# PhraseGame Assignment 1
# 03/25/2024


def draw_scoreboard(total_guesses, incorrect_guesses):
    # Calculate the number of empty boxes
    empty_boxes = total_guesses - incorrect_guesses
    scoreboard = "+-----" * total_guesses + "+\n"
    scoreboard += "|\\\\ //" * incorrect_guesses + "|     " * empty_boxes + "|\n"
    scoreboard += "| \V/ " * incorrect_guesses + "|     " * empty_boxes + "|\n"
    scoreboard += "| /.\ " * incorrect_guesses + "|     " * empty_boxes + "|\n"
    scoreboard += "|// \\\\" * incorrect_guesses + "|     " * empty_boxes + "|\n"
    scoreboard += "+-----" * total_guesses + "+\n"

    return scoreboard


if __name__ == '__main__':
    number_of_guesses = int(input("Enter number of guesses allowed between 1 and 11 "))
    incorrect_ones = int(input("Enter number of incorrect guesses "))
    print(draw_scoreboard(number_of_guesses, incorrect_ones))
