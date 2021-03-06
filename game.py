# game.py
# import the draw module

#import draw
#from draw import *
from draw import draw_game

# import se dá dát i do IFu

# game.py
# import the draw module
if visual_mode:
    # in visual mode, we draw using graphics
    import draw_visual as draw
else:
    # in textual mode, we print out text
    import draw_textual as draw

def main():
    result = play_game()
    # this can either be visual or textual depending on visual_mode
    draw.draw_game(result)


def play_game():
    ...


def main():
    result = play_game()
    draw.draw_game(result)

# this means that if this script is executed, then
# main() will be executed
if __name__ == '__main__':
    main()
