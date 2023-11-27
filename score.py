from pathlib import Path


def add_score(difficultly):
    POINTS_OF_WINNING = int((difficultly * 3) + 5)
    # The function will read the current score in the scores file,
    # if it fails it will create a new one and will save the current score.
    try:
        score_file = open(Path("Scores.txt"), "r")
        score_file = int(score_file.readlines()[0])
        score = open(Path("Scores.txt"), "w")
        score.write(f"{int(POINTS_OF_WINNING)+score_file}")
    except FileNotFoundError:
        score = open(Path("Scores.txt"), "x")
        score.write(POINTS_OF_WINNING)