import random


def create_blank_sentence(sentence):
    words = sentence.split()
    blank_index = random.randint(0, len(words) - 1)
    blank_word = words[blank_index]
    words[blank_index] = "___"
    blank_sentence = " ".join(words)
    return blank_sentence, blank_word


def play_game():
    sentences = [
        "Du hast schon so viel mitgemacht",
        "Du lebst am Tag und lebst bei Nacht",
        "Hast oft geweint , denn es war nie leicht",
        "Doch selbst geteilt , warst du noch eins",
        "Du bist so dreckig , wunderschön, einzigartig, anzusehen",
        "Nur bei dir fühl ich mich zuhause",
        "Du bist mein Berlin",
        "Du bist mein Berlin",
        "Bist so verrückt und das mit Leidenschaft",

        "Machst alles , was sonst keiner macht , Berlin"
        "Du wurdest oft kaputt gemacht",
        "Doch jeder findest bei dir sein Platz",
        "Am Ende bist du vielleicht ein Neuanfang",
        "Steckst voller Chancen ein leben lang",
        "Du bist so dreckig , wunderschön , einzigartig , anzusehen",
        "Nur bei dir fühl ich mich zuhause",
        "Du bist mein Berlin",
        "Du bist mein Berlin",
        "Bist so verrückt und das mit Leidenschaft",
        "Machst alles, was sonst keiner macht, Berlin",
        "Das ist mein Berlin",
        "Voller Hoffnung voll mit Euphorie",
        "Zwischen Chaos und Chemie",
        "Manchmal so hässlich und dann so schön",
        "Du bist mein Berlin",
        "Du bist mein Berlin, Berlin, Berlin",
        "Du bist mein Berlin",
        "Du bist mein Berlin",
        "Bist so verrückt und das mit Leidenschaft",
        "Machst alles , was sonst keiner macht , Berlin",
        "Das ist mein Berlin"
    ]

    print("Welcome to the Fill in the Blanks Game!\n")

    score = 0
    for sentence in sentences:

        blank_sentence, correct_answer = create_blank_sentence(sentence)
        print("Fill in the blank:")
        print(blank_sentence)

        user_input = input("\nEnter your guess: ")

        if user_input.lower() == correct_answer.lower():
            print("\nCorrect!\n")
            score = score+1
            print("Score= " + str(score))
        else:
            print(f"\nIncorrect. The correct answer is: {correct_answer}\n")
            score = score+0
            print(str("Score= ") + str(score))

    print("Congratulations! You completed the game.")
    print("You scored", score, "out of", len(sentences))


if __name__ == "__main__":
    play_game()
