#!/bin/python3

# Initial prototype of a curses-based Nmap menu

import curses
from curses import wrapper

stdscr = curses.initscr()

curses.noecho()
curses.cbreak()
stdscr.keypad(True)

def main(stdscr):
    # Clear screen
    stdscr.clear()

    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)

    stdscr.addstr("#############\n")
    stdscr.addstr("# ")
    stdscr.addstr("Nmap Menu ", curses.color_pair(1))
    stdscr.addstr("#\n")
    stdscr.addstr("#############\n")
    stdscr.addstr("\n\n")

    stdscr.addstr("Target ")
    stdscr.addstr("[E]", curses.color_pair(1))
    stdscr.addstr("ntry\n")
    stdscr.addstr("[H]", curses.color_pair(1))
    stdscr.addstr("ost Discovery method(s)\n")
    stdscr.addstr("[S]", curses.color_pair(1))
    stdscr.addstr("can technique(s)\n")
    stdscr.addstr("[P]", curses.color_pair(1))
    stdscr.addstr("ort option(s)\n")
    stdscr.addstr("Ser")
    stdscr.addstr("[V]", curses.color_pair(1))
    stdscr.addstr("ice/Version option(s)\n")
    stdscr.addstr("[C]", curses.color_pair(1))
    stdscr.addstr("ript option(s)\n")
    stdscr.addstr("[O]", curses.color_pair(1))
    stdscr.addstr("perating System option(s)\n")
    stdscr.addstr("[T]", curses.color_pair(1))
    stdscr.addstr("iming option(s)\n")
    stdscr.addstr("Firewall/I")
    stdscr.addstr("[D]", curses.color_pair(1))
    stdscr.addstr("S Evasion option(s)\n")
    stdscr.addstr("\n")
    stdscr.addstr("E")
    stdscr.addstr("[X]", curses.color_pair(1))
    stdscr.addstr("it")

    stdscr.refresh()

    selection = ""
    while selection != "x":
        selection = stdscr.getkey()

wrapper(main)

curses.nocbreak()
stdscr.keypad(False)
curses.echo()

curses.endwin()
