#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'https://github.com/qkzk'
__date__ = '2020/06/20'
__title__ = 'Python String Coloring'
__doc__ = '''
{0}
{1}
{2}

This simple script gives you simpler syntax to print colored text on POSIX
compliant terminals.

Usage :

1. copy it somewhere, remember the path
2. import it from another script :




    Just replace the path with the address of your script

3. use it !


    To print a white colored text
    >>> color.print_color("BONJOUR", "WHITE")

    To print an inverted red text :
    >>> color.print_color("Hello World !", "RED", inverted=True)

    To format a string, without printing it, just :
    >>> color.format_color("print me if you want ;)", color="RED")

source:

https://stackoverflow.com/questions/67631/how-to-import-a-module-given-the-full-path

'''.format(__title__, __author__, __date__)


################################################################################
################################################################################
#################### CONSTANTS  ################################################
################################################################################
################################################################################

colors = {

    "WHITE": '\033[37m',
    "PURPLE": '\033[95m',
    "CYAN": '\033[96m',
    "DARKCYAN": '\033[36m',
    "BLUE": '\033[94m',
    "GREEN": '\033[92m',
    "YELLOW": '\033[93m',
    "RED": '\033[91m',
    "BOLD": '\033[1m',
    "UNDERLINE": '\033[4m',
    "END": '\033[0m',
    "INVERTED": '\033[7m',

}

colors_tag = {
    "END": colors["END"] + colors["END"],
}

for name, color_tag in colors.items():
    colors_tag[name] = colors[name] + colors["BOLD"]


################################################################################
################################################################################
#################### UTILS  ####################################################
################################################################################
################################################################################


def format_color(string, color=None, inverted=False):
    '''
    Format a string with a color
    Used for printing in POSIX terminals.

    if no color is given or if the color doesn't math the preset,
    returns the string
    '''
    if not type(string) == str:
        string = repr(string)
        return string
    if not color or type(color) != str:
        return string
    else:
        color = color.upper()
        if inverted:
            string = colors["INVERTED"] + string
        if color in colors:
            string = colors_tag[color] + string +\
                colors_tag["END"] + colors["END"]
        if inverted:
            string += colors["END"]
    return string


def print_color(string, color=None, inverted=False, end=None):
    '''
    Print a colored formated string
    '''
    if end is None:
        print(format_color(string, color=color, inverted=inverted))
    else:
        print(format_color(string, color=color, inverted=inverted), end=end)


def examples():

    ############################################################################
    ############################################################################
    #################### EXAMPLES  #############################################
    ############################################################################
    ############################################################################
    print("\033[0;37;40m Normal text\n")
    print("\033[2;37;40m Underlined text\033[0;37;40m \n")
    print("\033[1;37;40m Bright Colour\033[0;37;40m \n")
    print("\033[3;37;40m Negative Colour\033[0;37;40m \n")
    print("\033[5;37;40m Negative Colour\033[0;37;40m\n")

    print("\033[1;37;40m \033[2;37:40m TextColour BlackBackground          TextColour GreyBackground                WhiteText ColouredBackground\033[0;37;40m\n")
    print("\033[1;30;40m Dark Gray      \033[0m 1;30;40m            \033[0;30;47m Black      \033[0m 0;30;47m               \033[0;37;41m Black      \033[0m 0;37;41m")
    print("\033[1;31;40m Bright Red     \033[0m 1;31;40m            \033[0;31;47m Red        \033[0m 0;31;47m               \033[0;37;42m Black      \033[0m 0;37;42m")
    print("\033[1;32;40m Bright Green   \033[0m 1;32;40m            \033[0;32;47m Green      \033[0m 0;32;47m               \033[0;37;43m Black      \033[0m 0;37;43m")
    print("\033[1;33;40m Yellow         \033[0m 1;33;40m            \033[0;33;47m Brown      \033[0m 0;33;47m               \033[0;37;44m Black      \033[0m 0;37;44m")
    print("\033[1;34;40m Bright Blue    \033[0m 1;34;40m            \033[0;34;47m Blue       \033[0m 0;34;47m               \033[0;37;45m Black      \033[0m 0;37;45m")
    print("\033[1;35;40m Bright Magenta \033[0m 1;35;40m            \033[0;35;47m Magenta    \033[0m 0;35;47m               \033[0;37;46m Black      \033[0m 0;37;46m")
    print("\033[1;36;40m Bright Cyan    \033[0m 1;36;40m            \033[0;36;47m Cyan       \033[0m 0;36;47m               \033[0;37;47m Black      \033[0m 0;37;47m")
    print("\033[1;37;40m White          \033[0m 1;37;40m            \033[0;37;40m Light Grey \033[0m 0;37;40m               \033[0;37;48m Black      \033[0m 0;37;48m")

    print_color("gras, blanc", "white")
    print("normal, gris")

    print(colors["END"] + "normal, on essaie encore")
    print_color("gras, rouge", "red")


if __name__ == '__main__':
    examples()
