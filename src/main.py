import pygame, os, time
from button import Button
from sound import *

pygame.init()
pygame.font.init()
pygame.mixer.init()


os.chdir("C:\shihan-work\Python Projects\PerfectPitchTrainer\Assets\images")

BACKGROUND = pygame.image.load("piano-background.png")  # Loads background

START_IMG = pygame.image.load("button_start (1).png")
BACK_IMG = pygame.image.load("button_back.png")
EXIT_IMG = pygame.image.load("button_exit.png")

PERFECT_PITCH_IMG = pygame.image.load("button_perfect-pitch.png")
INTERVALS_IMG = pygame.image.load("button_intervals.png")

EASY_IMG = pygame.image.load("button_easy.png")
MEDIUM_IMG = pygame.image.load("button_medium.png")
HARD_IMG = pygame.image.load("button_hard.png")

C_IMG = pygame.image.load("button_c (1).png")
D_IMG = pygame.image.load("button_d (1).png")
E_IMG = pygame.image.load("button_e (1).png")
F_IMG = pygame.image.load("button_f (1).png")
G_IMG = pygame.image.load("button_g (4).png")

A_IMG = pygame.image.load("button_a (2).png")
B_IMG = pygame.image.load("button_b.png")

CSHARP_IMG = pygame.image.load("button_c (2).png")
DSHARP_IMG = pygame.image.load("button_d (2).png")
FSHARP_IMG = pygame.image.load("button_f (2).png")
GSHARP_IMG = pygame.image.load("button_g (5).png")
ASHARP_IMG = pygame.image.load("button_a (3).png")

PLAY_IMG = pygame.image.load("button_play.png")
NEXT_IMG = pygame.image.load("button_next.png")
REVEAL_IMG = pygame.image.load("button_reveal (1).png")
INSTRUMENT_IMG = pygame.image.load("button_instrument (1).png")

os.chdir("C:\shihan-work\Python Projects\PerfectPitchTrainer\Assets\sounds")

Correct = "C:\shihan-work\Python Projects\PerfectPitchTrainer\Assets\sounds\The Price is Right Ding - Gaming Sound Effect (HD).mp3"
Incorrect = "C:\shihan-work\Python Projects\PerfectPitchTrainer\Assets\sounds\Buzzer Wrong Answer - Gaming Sound Effect (HD).mp3"

os.chdir("C:\shihan-work\Python Projects\PerfectPitchTrainer\Assets\sounds\piano")

GREEN = (67, 224, 109)

WIDTH, HEIGHT = 1280, 720  # Sets screen's width and height constants

start_button = Button(
    (WIDTH - START_IMG.get_width()) / 2 - 150,
    HEIGHT * 0.66 - START_IMG.get_height() / 2,
    START_IMG,
    1,
)
back_button = Button(WIDTH * 0.85, HEIGHT * 0.87, BACK_IMG, 1)
exit_button = Button(
    (WIDTH - START_IMG.get_width()) / 2 + 150,
    HEIGHT * 0.66 - EXIT_IMG.get_height() / 2,
    EXIT_IMG,
    1,
)

perfect_pitch_button = Button(
    (WIDTH - PERFECT_PITCH_IMG.get_width()) / 2 - 200,
    HEIGHT * 0.66 - PERFECT_PITCH_IMG.get_height() / 2,
    PERFECT_PITCH_IMG,
    1,
)
intervals_button = Button(
    (WIDTH - PERFECT_PITCH_IMG.get_width()) / 2 + 200,
    HEIGHT * 0.66 - INTERVALS_IMG.get_height() / 2,
    INTERVALS_IMG,
    1,
)

easy_button = Button(
    350 - EASY_IMG.get_width() / 2,
    HEIGHT * 0.66 - EASY_IMG.get_height() / 2,
    EASY_IMG,
    1,
)
medium_button = Button(
    WIDTH / 2 - MEDIUM_IMG.get_width() / 2,
    HEIGHT * 0.66 - MEDIUM_IMG.get_height() / 2,
    MEDIUM_IMG,
    1,
)
hard_button = Button(
    WIDTH - 350 - EASY_IMG.get_width() / 2,
    HEIGHT * 0.66 - HARD_IMG.get_height() / 2,
    HARD_IMG,
    1,
)

next_button = Button(
    (WIDTH - NEXT_IMG.get_width()) / 2 + 100,
    HEIGHT * 0.4 - NEXT_IMG.get_height() / 2,
    NEXT_IMG,
    1,
)
play_button = Button(
    (WIDTH - PLAY_IMG.get_width()) / 2 - 100,
    HEIGHT * 0.4 - PLAY_IMG.get_height() / 2,
    PLAY_IMG,
    1,
)
reveal_button = Button(
    play_button.x
    - REVEAL_IMG.get_width()
    - (next_button.x - (play_button.x + PLAY_IMG.get_width())),
    HEIGHT * 0.4 - REVEAL_IMG.get_height() / 2,
    REVEAL_IMG,
    1,
)
instrument_button = Button(
    next_button.x
    + NEXT_IMG.get_width()
    + (next_button.x - (play_button.x + PLAY_IMG.get_width())),
    HEIGHT * 0.4 - INSTRUMENT_IMG.get_height() / 2,
    INSTRUMENT_IMG,
    1,
)

c_easy_button = Button(
    (WIDTH / 2 - E_IMG.get_width() * 3.5),
    HEIGHT * 0.8 - C_IMG.get_height() / 2,
    C_IMG,
    1,
)
d_easy_button = Button(
    (WIDTH / 2 - E_IMG.get_width() * 2), HEIGHT * 0.8 - D_IMG.get_height() / 2, D_IMG, 1
)
e_easy_button = Button(
    WIDTH / 2 - E_IMG.get_width() / 2, HEIGHT * 0.8 - E_IMG.get_height() / 2, E_IMG, 1
)
f_easy_button = Button(
    (WIDTH / 2 + E_IMG.get_width()), HEIGHT * 0.8 - F_IMG.get_height() / 2, F_IMG, 1
)
g_easy_button = Button(
    (WIDTH / 2 + E_IMG.get_width() * 2.5),
    HEIGHT * 0.8 - G_IMG.get_height() / 2,
    G_IMG,
    1,
)

c_button = Button(
    (WIDTH / 2 - E_IMG.get_width() * 5), HEIGHT * 0.8 - C_IMG.get_height() / 2, C_IMG, 1
)
d_button = Button(
    (WIDTH / 2 - E_IMG.get_width() * 3.5),
    HEIGHT * 0.8 - D_IMG.get_height() / 2,
    D_IMG,
    1,
)
e_button = Button(
    (WIDTH / 2 - E_IMG.get_width() * 2), HEIGHT * 0.8 - E_IMG.get_height() / 2, E_IMG, 1
)
f_button = Button(
    WIDTH / 2 - E_IMG.get_width() / 2, HEIGHT * 0.8 - F_IMG.get_height() / 2, F_IMG, 1
)
g_button = Button(
    (WIDTH / 2 + E_IMG.get_width()), HEIGHT * 0.8 - G_IMG.get_height() / 2, G_IMG, 1
)
a_button = Button(
    (WIDTH / 2 + E_IMG.get_width() * 2.5),
    HEIGHT * 0.8 - A_IMG.get_height() / 2,
    A_IMG,
    1,
)
b_button = Button(
    (WIDTH / 2 + E_IMG.get_width() * 4), HEIGHT * 0.8 - B_IMG.get_height() / 2, B_IMG, 1
)

csharp_button = Button(
    ((d_button.x + D_IMG.get_width() / 2) - (c_button.x + C_IMG.get_width() / 2)) / 2
    + c_button.x
    + C_IMG.get_width() / 2
    - CSHARP_IMG.get_width() / 2,
    HEIGHT * 0.6,
    CSHARP_IMG,
    1,
)
dsharp_button = Button(
    ((e_button.x + E_IMG.get_width() / 2) - (d_button.x + D_IMG.get_width() / 2)) / 2
    + d_button.x
    + D_IMG.get_width() / 2
    - DSHARP_IMG.get_width() / 2,
    HEIGHT * 0.6,
    DSHARP_IMG,
    1,
)
fsharp_button = Button(
    ((g_button.x + G_IMG.get_width() / 2) - (f_button.x + F_IMG.get_width() / 2)) / 2
    + f_button.x
    + F_IMG.get_width() / 2
    - FSHARP_IMG.get_width() / 2,
    HEIGHT * 0.6,
    FSHARP_IMG,
    1,
)
gsharp_button = Button(
    ((a_button.x + A_IMG.get_width() / 2) - (g_button.x + G_IMG.get_width() / 2)) / 2
    + g_button.x
    + G_IMG.get_width() / 2
    - GSHARP_IMG.get_width() / 2,
    HEIGHT * 0.6,
    GSHARP_IMG,
    1,
)
asharp_button = Button(
    ((b_button.x + B_IMG.get_width() / 2) - (a_button.x + A_IMG.get_width() / 2)) / 2
    + a_button.x
    + A_IMG.get_width() / 2
    - ASHARP_IMG.get_width() / 2,
    HEIGHT * 0.6,
    ASHARP_IMG,
    1,
)


WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # Creates the window object
pygame.display.set_caption(
    "Perfect Pitch Trainer"
)  # Creates a title because why not :)

DEFAULT_FONT = pygame.font.SysFont("comicsans", 60)

loading_text = DEFAULT_FONT.render("Welcome to the Perfect Pitch Trainer!", 1, GREEN)
select_gamemode_text = DEFAULT_FONT.render("Select gamemode", 1, GREEN)
select_difficulty_text = DEFAULT_FONT.render("Choose Difficulty", 1, GREEN)
easy_mode_text = DEFAULT_FONT.render("Easy Mode", 1, GREEN)
medium_mode_text = DEFAULT_FONT.render("Medium Mode", 1, GREEN)
hard_mode_text = DEFAULT_FONT.render("Hard Mode", 1, GREEN)

FPS = 60


def draw_border(surface, x, y, width, height):
    point1 = (x, y)
    point2 = (x, y + height)
    point3 = (x + width, y + height)
    point4 = (x + width, y)
    pygame.draw.line(surface, GREEN, (point1), (point2), 10)
    pygame.draw.line(surface, GREEN, (point2), (point3), 10)
    pygame.draw.line(surface, GREEN, (point3), (point4), 10)
    pygame.draw.line(surface, GREEN, (point4), (point1), 10)


def loading_screen():
    WIN.blit(BACKGROUND, (0, 0))  # places the background onto the screen
    WIN.blit(
        loading_text,
        (
            (WIDTH - loading_text.get_width()) / 2,
            HEIGHT * 0.33 - loading_text.get_height() / 2,
        ),
    )
    if start_button.draw(WIN):
        time.sleep(0.1)
        return "GamemodeSelect"
    elif exit_button.draw(WIN):
        time.sleep(0.1)
        return "Quit"
    else:
        return "Loading"


def select_gamemode_screen():
    WIN.blit(BACKGROUND, (0, 0))  # places the background onto the screen
    WIN.blit(
        select_gamemode_text,
        (
            (WIDTH - select_gamemode_text.get_width()) / 2,
            HEIGHT * 0.33 - select_gamemode_text.get_height() / 2,
        ),
    )

    if perfect_pitch_button.draw(WIN):
        time.sleep(0.1)
        return "EnterPerfectPitch"

    elif intervals_button.draw(WIN):
        time.sleep(0.1)
        return "EnterIntervals"
    elif back_button.draw(WIN):
        time.sleep(0.1)
        return "Loading"
    else:
        return "GamemodeSelect"


def perfect_pitch_difficulty_screen():
    WIN.blit(BACKGROUND, (0, 0))
    WIN.blit(
        select_difficulty_text,
        (
            (WIDTH - select_difficulty_text.get_width()) / 2,
            HEIGHT * 0.33 - select_difficulty_text.get_height() / 2,
        ),
    )

    if easy_button.draw(WIN):
        time.sleep(0.1)
        return "PerfectPitchEasy"
    elif medium_button.draw(WIN):
        time.sleep(0.1)
        return "PerfectPitchMedium"
    elif hard_button.draw(WIN):
        time.sleep(0.1)
        return "PerfectPitchHard"
    elif back_button.draw(WIN):
        time.sleep(0.1)
        return "GamemodeSelect"
    else:
        return "EnterPerfectPitch"


def perfect_pitch_easy(current_note, is_revealed, current_instrument):
    if not is_revealed:
        WIN.blit(BACKGROUND, (0, 0))
        WIN.blit(
            easy_mode_text,
            (
                (WIDTH - easy_mode_text.get_width()) / 2,
                HEIGHT * 0.2 - easy_mode_text.get_height() / 2,
            ),
        )
    if next_button.draw(WIN):
        is_revealed = False
        current_note = pick_random_easy(current_note, current_instrument)
        time.sleep(0.1)

        return "PerfectPitchEasy", current_note, is_revealed
    elif play_button.draw(WIN):
        pygame.mixer.music.load(current_note)
        pygame.mixer.music.play()
        time.sleep(0.1)
        return "PerfectPitchEasy"
    elif back_button.draw(WIN):
        current_note = ""
        is_revealed = False
        time.sleep(0.1)
        return "EnterPerfectPitch", current_note, is_revealed
    elif reveal_button.draw(WIN):
        is_revealed = True
        if current_note[0] == "C":
            draw_border(
                WIN,
                c_easy_button.x,
                c_easy_button.y,
                C_IMG.get_width(),
                C_IMG.get_height(),
            )
        elif current_note[0] == "D":
            draw_border(
                WIN,
                d_easy_button.x,
                d_easy_button.y,
                D_IMG.get_width(),
                D_IMG.get_height(),
            )
        elif current_note[0] == "E":
            draw_border(
                WIN,
                e_easy_button.x,
                e_easy_button.y,
                E_IMG.get_width(),
                E_IMG.get_height(),
            )
        elif current_note[0] == "F":
            draw_border(
                WIN,
                f_easy_button.x,
                f_easy_button.y,
                F_IMG.get_width(),
                F_IMG.get_height(),
            )
        elif current_note[0] == "G":
            draw_border(
                WIN,
                g_easy_button.x,
                g_easy_button.y,
                G_IMG.get_width(),
                G_IMG.get_height(),
            )

        return "PerfectPitchEasy", current_note, is_revealed

    elif instrument_button.draw(WIN):
        pass
    elif c_easy_button.draw(WIN):
        if current_note[0] == "C":
            pygame.mixer.music.load(Correct)
            pygame.mixer.music.play()
            print("Correct")

        else:
            pygame.mixer.music.load(Incorrect)
            pygame.mixer.music.play()
            print("Incorrect")
            print("played")
        time.sleep(0.1)
    elif d_easy_button.draw(WIN):
        if current_note[0] == "D":
            print("Correct")
            pygame.mixer.music.load(Correct)
            pygame.mixer.music.play()

        else:
            print("Incorrect")
            pygame.mixer.music.load(Incorrect)
            pygame.mixer.music.play()
        time.sleep(0.1)
    elif e_easy_button.draw(WIN):
        if current_note[0] == "E":
            pygame.mixer.music.load(Correct)
            pygame.mixer.music.play()
            print("Correct")
        else:
            pygame.mixer.music.load(Incorrect)
            pygame.mixer.music.play()
            print("Incorrect")
        time.sleep(0.1)
    elif f_easy_button.draw(WIN):
        if current_note[0] == "F":
            pygame.mixer.music.load(Correct)
            pygame.mixer.music.play()
            print("Correct")
        else:
            pygame.mixer.music.load(Incorrect)
            pygame.mixer.music.play()
            print("Incorrect")
        time.sleep(0.1)
    elif g_easy_button.draw(WIN):
        if current_note[0] == "G":
            pygame.mixer.music.load(Correct)
            pygame.mixer.music.play()
            print("Correct")
        else:
            pygame.mixer.music.load(Incorrect)
            pygame.mixer.music.play()
            print("Incorrect")
        time.sleep(0.1)
    return "PerfectPitchEasy"


def perfect_pitch_medium(current_note, is_revealed):
    if not is_revealed:
        WIN.blit(BACKGROUND, (0, 0))
        WIN.blit(
            medium_mode_text,
            (
                (WIDTH - medium_mode_text.get_width()) / 2,
                HEIGHT * 0.2 - medium_mode_text.get_height() / 2,
            ),
        )
    if next_button.draw(WIN):
        is_revealed = False
        current_note = pick_random_medium(current_note)
        time.sleep(0.1)

        return "PerfectPitchMedium", current_note, is_revealed
    elif play_button.draw(WIN):
        pygame.mixer.music.load(current_note)
        pygame.mixer.music.play()
        time.sleep(0.1)
        return "PerfectPitchMedium"
    elif back_button.draw(WIN):
        current_note = ""
        is_revealed = False

        time.sleep(0.1)
        return "EnterPerfectPitch", current_note, is_revealed
    elif reveal_button.draw(WIN):
        is_revealed = True
        if current_note[0] == "C":
            draw_border(
                WIN, c_button.x, c_button.y, C_IMG.get_width(), C_IMG.get_height()
            )
        elif current_note[0] == "D":
            draw_border(
                WIN, d_button.x, d_button.y, D_IMG.get_width(), D_IMG.get_height()
            )
        elif current_note[0] == "E":
            draw_border(
                WIN, e_button.x, e_button.y, E_IMG.get_width(), E_IMG.get_height()
            )
        elif current_note[0] == "F":
            draw_border(
                WIN, f_button.x, f_button.y, F_IMG.get_width(), F_IMG.get_height()
            )
        elif current_note[0] == "G":
            draw_border(
                WIN, g_button.x, g_button.y, G_IMG.get_width(), G_IMG.get_height()
            )
        elif current_note[0] == "A":
            draw_border(
                WIN, a_button.x, a_button.y, A_IMG.get_width(), A_IMG.get_height()
            )
        elif current_note[0] == "B":
            draw_border(
                WIN, b_button.x, b_button.y, B_IMG.get_width(), B_IMG.get_height()
            )

        return "PerfectPitchMedium", current_note, is_revealed

    elif c_button.draw(WIN):
        if current_note[0] == "C":
            pygame.mixer.music.load(Correct)
            pygame.mixer.music.play()
            print("Correct")

        else:
            pygame.mixer.music.load(Incorrect)
            pygame.mixer.music.play()
            print("Incorrect")
            print("played")
        time.sleep(0.1)
    elif d_button.draw(WIN):
        if current_note[0] == "D":
            print("Correct")
            pygame.mixer.music.load(Correct)
            pygame.mixer.music.play()

        else:
            print("Incorrect")
            pygame.mixer.music.load(Incorrect)
            pygame.mixer.music.play()
        time.sleep(0.1)
    elif e_button.draw(WIN):
        if current_note[0] == "E":
            pygame.mixer.music.load(Correct)
            pygame.mixer.music.play()
            print("Correct")
        else:
            pygame.mixer.music.load(Incorrect)
            pygame.mixer.music.play()
            print("Incorrect")
        time.sleep(0.1)
    elif f_button.draw(WIN):
        if current_note[0] == "F":
            pygame.mixer.music.load(Correct)
            pygame.mixer.music.play()
            print("Correct")
        else:
            pygame.mixer.music.load(Incorrect)
            pygame.mixer.music.play()
            print("Incorrect")
        time.sleep(0.1)
    elif g_button.draw(WIN):
        if current_note[0] == "G":
            pygame.mixer.music.load(Correct)
            pygame.mixer.music.play()
            print("Correct")
        else:
            pygame.mixer.music.load(Incorrect)
            pygame.mixer.music.play()
            print("Incorrect")
        time.sleep(0.1)
    elif a_button.draw(WIN):
        if current_note[0] == "A":
            pygame.mixer.music.load(Correct)
            pygame.mixer.music.play()
            print("Correct")
        else:
            pygame.mixer.music.load(Incorrect)
            pygame.mixer.music.play()
            print("Incorrect")
        time.sleep(0.1)
    elif b_button.draw(WIN):
        if current_note[0] == "B":
            pygame.mixer.music.load(Correct)
            pygame.mixer.music.play()
            print("Correct")
        else:
            pygame.mixer.music.load(Incorrect)
            pygame.mixer.music.play()
            print("Incorrect")
        time.sleep(0.1)
    return "PerfectPitchMedium"


def perfect_pitch_hard(current_note, is_revealed):
    if not is_revealed:
        WIN.blit(BACKGROUND, (0, 0))
        WIN.blit(
            hard_mode_text,
            (
                (WIDTH - hard_mode_text.get_width()) / 2,
                HEIGHT * 0.2 - hard_mode_text.get_height() / 2,
            ),
        )
    if next_button.draw(WIN):
        is_revealed = False
        current_note = pick_random_hard(current_note)
        time.sleep(0.1)

        return "PerfectPitchHard", current_note, is_revealed
    elif play_button.draw(WIN):
        print(current_note)

        pygame.mixer.music.load(current_note)
        pygame.mixer.music.play()
        time.sleep(0.1)
        return "PerfectPitchHard"
    elif back_button.draw(WIN):
        current_note = ""
        is_revealed = False

        time.sleep(0.1)
        return "EnterPerfectPitch", current_note, is_revealed
    elif reveal_button.draw(WIN):
        is_revealed = True

        if current_note[0] == "C":
            if len(current_note) == 7:
                draw_border(
                    WIN,
                    csharp_button.x,
                    csharp_button.y,
                    CSHARP_IMG.get_width(),
                    CSHARP_IMG.get_height(),
                )
            else:
                draw_border(
                    WIN, c_button.x, c_button.y, C_IMG.get_width(), C_IMG.get_height()
                )
        elif current_note[0] == "D":
            if len(current_note) == 7:
                draw_border(
                    WIN,
                    dsharp_button.x,
                    dsharp_button.y,
                    DSHARP_IMG.get_width(),
                    DSHARP_IMG.get_height(),
                )
            else:
                draw_border(
                    WIN, d_button.x, d_button.y, D_IMG.get_width(), D_IMG.get_height()
                )
        elif current_note[0] == "E":
            draw_border(
                WIN,
                e_easy_button.x,
                e_easy_button.y,
                E_IMG.get_width(),
                E_IMG.get_height(),
            )
        elif current_note[0] == "F":
            if len(current_note) == 7:
                draw_border(
                    WIN,
                    fsharp_button.x,
                    fsharp_button.y,
                    FSHARP_IMG.get_width(),
                    FSHARP_IMG.get_height(),
                )
            else:
                draw_border(
                    WIN, f_button.x, f_button.y, F_IMG.get_width(), F_IMG.get_height()
                )
        elif current_note[0] == "G":
            if len(current_note) == 7:
                draw_border(
                    WIN,
                    gsharp_button.x,
                    gsharp_button.y,
                    GSHARP_IMG.get_width(),
                    GSHARP_IMG.get_height(),
                )
            else:
                draw_border(
                    WIN, g_button.x, g_button.y, G_IMG.get_width(), G_IMG.get_height()
                )

        elif current_note[0] == "A":
            if len(current_note) == 7:
                draw_border(
                    WIN,
                    asharp_button.x,
                    asharp_button.y,
                    ASHARP_IMG.get_width(),
                    ASHARP_IMG.get_height(),
                )
            else:
                draw_border(
                    WIN, a_button.x, a_button.y, A_IMG.get_width(), A_IMG.get_height()
                )
        elif current_note[0] == "B":
            draw_border(
                WIN,
                d_easy_button.x,
                d_easy_button.y,
                D_IMG.get_width(),
                D_IMG.get_height(),
            )

        return "PerfectPitchHard", current_note, is_revealed
    elif csharp_button.draw(WIN):
        if len(current_note) == 7:
            if current_note[:2] == "C#":
                pygame.mixer.music.load(Correct)
                pygame.mixer.music.play()
                print("Correct")
            else:
                pygame.mixer.music.load(Incorrect)
                pygame.mixer.music.play()
                print("Incorrect")
        else:
            pygame.mixer.music.load(Incorrect)
            pygame.mixer.music.play()
            print("Incorrect")
        time.sleep(0.1)
    elif dsharp_button.draw(WIN):
        if len(current_note) == 7:
            if current_note[:2] == "D#":
                pygame.mixer.music.load(Correct)
                pygame.mixer.music.play()
                print("Correct")
            else:
                pygame.mixer.music.load(Incorrect)
                pygame.mixer.music.play()
                print("Incorrect")
        else:
            pygame.mixer.music.load(Incorrect)
            pygame.mixer.music.play()
            print("Incorrect")
        time.sleep(0.1)
    elif fsharp_button.draw(WIN):
        if len(current_note) == 7:
            if current_note[:2] == "F#":
                pygame.mixer.music.load(Correct)
                pygame.mixer.music.play()
                print("Correct")
            else:
                pygame.mixer.music.load(Incorrect)
                pygame.mixer.music.play()
                print("Incorrect")
        else:
            pygame.mixer.music.load(Incorrect)
            pygame.mixer.music.play()
            print("Incorrect")
        time.sleep(0.1)
    elif gsharp_button.draw(WIN):
        if len(current_note) == 7:
            if current_note[:2] == "G#":
                pygame.mixer.music.load(Correct)
                pygame.mixer.music.play()
                print("Correct")
            else:
                pygame.mixer.music.load(Incorrect)
                pygame.mixer.music.play()
                print("Incorrect")
        else:
            pygame.mixer.music.load(Incorrect)
            pygame.mixer.music.play()
            print("Incorrect")
        time.sleep(0.1)
    elif asharp_button.draw(WIN):
        if len(current_note) == 7:
            if current_note[:2] == "A#":
                pygame.mixer.music.load(Correct)
                pygame.mixer.music.play()
                print("Correct")
            else:
                pygame.mixer.music.load(Incorrect)
                pygame.mixer.music.play()
                print("Incorrect")
        else:
            pygame.mixer.music.load(Incorrect)
            pygame.mixer.music.play()
            print("Incorrect")
        time.sleep(0.1)
    elif c_button.draw(WIN):
        if len(current_note) == 6:
            if current_note[0] == "C":
                pygame.mixer.music.load(Correct)
                pygame.mixer.music.play()
                print("Correct")
            else:
                pygame.mixer.music.load(Incorrect)
                pygame.mixer.music.play()
                print("Incorrect")
        else:
            pygame.mixer.music.load(Incorrect)
            pygame.mixer.music.play()
            print("Incorrect")
        time.sleep(0.1)
    elif d_button.draw(WIN):
        if len(current_note) == 6:
            if current_note[0] == "D":
                pygame.mixer.music.load(Correct)
                pygame.mixer.music.play()
                print("Correct")
            else:
                pygame.mixer.music.load(Incorrect)
                pygame.mixer.music.play()
                print("Incorrect")
        else:
            print("Incorrect")
            pygame.mixer.music.load(Incorrect)
            pygame.mixer.music.play()
        time.sleep(0.1)
    elif e_button.draw(WIN):
        if len(current_note) == 6:
            if current_note[0] == "E":
                pygame.mixer.music.load(Correct)
                pygame.mixer.music.play()
                print("Correct")
            else:
                pygame.mixer.music.load(Incorrect)
                pygame.mixer.music.play()
                print("Incorrect")
        else:
            pygame.mixer.music.load(Incorrect)
            pygame.mixer.music.play()
            print("Incorrect")
        time.sleep(0.1)
    elif f_button.draw(WIN):
        if len(current_note) == 6:
            if current_note[0] == "F":
                pygame.mixer.music.load(Correct)
                pygame.mixer.music.play()
                print("Correct")
            else:
                pygame.mixer.music.load(Incorrect)
                pygame.mixer.music.play()
                print("Incorrect")
        else:
            pygame.mixer.music.load(Incorrect)
            pygame.mixer.music.play()
            print("Incorrect")
        time.sleep(0.1)
    elif g_button.draw(WIN):
        if len(current_note) == 6:
            if current_note[0] == "G":
                pygame.mixer.music.load(Correct)
                pygame.mixer.music.play()
                print("Correct")
            else:
                pygame.mixer.music.load(Incorrect)
                pygame.mixer.music.play()
                print("Incorrect")
        else:
            pygame.mixer.music.load(Incorrect)
            pygame.mixer.music.play()
            print("Incorrect")
        time.sleep(0.1)
    elif a_button.draw(WIN):
        if len(current_note) == 6:
            if current_note[0] == "A":
                pygame.mixer.music.load(Correct)
                pygame.mixer.music.play()
                print("Correct")
            else:
                pygame.mixer.music.load(Incorrect)
                pygame.mixer.music.play()
                print("Incorrect")
        else:
            pygame.mixer.music.load(Incorrect)
            pygame.mixer.music.play()
            print("Incorrect")
        time.sleep(0.1)
    elif b_button.draw(WIN):
        if len(current_note) == 6:
            if current_note[0] == "B":
                pygame.mixer.music.load(Correct)
                pygame.mixer.music.play()
                print("Correct")
            else:
                pygame.mixer.music.load(Incorrect)
                pygame.mixer.music.play()
                print("Incorrect")
        else:
            pygame.mixer.music.load(Incorrect)
            pygame.mixer.music.play()
            print("Incorrect")
        time.sleep(0.1)

    return "PerfectPitchHard"


def intervals_easy():
    WIN.blit(BACKGROUND, (0, 0))
    WIN.blit(
        easy_mode_text,
        (
            (WIDTH - easy_mode_text.get_width()) / 2,
            HEIGHT * 0.2 - easy_mode_text.get_height() / 2,
        ),
    )


def intervals_medium():
    WIN.blit(BACKGROUND, (0, 0))
    WIN.blit(
        medium_mode_text,
        (
            (WIDTH - medium_mode_text.get_width()) / 2,
            HEIGHT * 0.2 - medium_mode_text.get_height() / 2,
        ),
    )


def intervals_hard():
    WIN.blit(BACKGROUND, (0, 0))
    WIN.blit(
        hard_mode_text,
        (
            (WIDTH - hard_mode_text.get_width()) / 2,
            HEIGHT * 0.2 - hard_mode_text.get_height() / 2,
        ),
    )


def intervals_difficulty_screen():
    WIN.blit(BACKGROUND, (0, 0))
    WIN.blit(
        select_difficulty_text,
        (
            (WIDTH - select_difficulty_text.get_width()) / 2,
            HEIGHT * 0.33 - select_difficulty_text.get_height() / 2,
        ),
    )
    if easy_button.draw(WIN):
        time.sleep(0.1)
        return "IntervalsEasy"
    elif medium_button.draw(WIN):
        time.sleep(0.1)
        return "IntervalsMedium"
    elif hard_button.draw(WIN):
        time.sleep(0.1)
        return "IntervalsHard"
    elif back_button.draw(WIN):
        time.sleep(0.1)
        return "GamemodeSelect"
    else:
        return "EnterIntervals"


def draw_window(screen, current_note, is_revealed, current_instrument):

    if screen == "Loading":
        result = loading_screen()
    elif screen == "GamemodeSelect":
        result = select_gamemode_screen()
    elif screen == "Quit":
        result = "Quit"
    elif screen == "EnterPerfectPitch":
        result = perfect_pitch_difficulty_screen()
    elif screen == "EnterIntervals":
        result = intervals_difficulty_screen()
    elif screen == "PerfectPitchEasy":
        result = perfect_pitch_easy(current_note, is_revealed, current_instrument)
    elif screen == "PerfectPitchMedium":
        result = perfect_pitch_medium(current_note, is_revealed)
    elif screen == "PerfectPitchHard":
        result = perfect_pitch_hard(current_note, is_revealed)
    elif screen == "IntervalsEasy":
        result = perfect_pitch_easy()
    elif screen == "IntervalsMedium":
        result = perfect_pitch_medium()
    elif screen == "IntervalsHard":
        result = perfect_pitch_hard()
    else:
        result = "Done"
    pygame.display.update()

    if type(result) == str:
        result = list(result.split())
        result.append(current_note)
        result.append(is_revealed)

    else:
        result = list(result)

    return result


def main():
    run = True
    clock = pygame.time.Clock()
    screen = "Loading"
    current_note = "C4.mp3"
    current_instrument = "Piano"
    is_revealed = False
    while run:
        clock.tick(FPS)  # Limits the game to 60fps

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        result = draw_window(screen, current_note, is_revealed, current_instrument)

        # print(result)
        screen = result[0]
        current_note = result[1]
        is_revealed = result[2]

        if screen == "Quit":
            pygame.quit()
    pygame.quit()


if __name__ == "__main__":  # Incase we need to import it (probably not)
    main()
