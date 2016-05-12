import curses
import curses.textpad
import time
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint
z = 0

mylist = [' '] * 10

def test():
    global z
    if z == 0:
        z += 1
        return "X"
    else:
        z -= 1
        return "O"

def rewrite(i):
    global mylist
    global write
    global c
    if mylist[i] == " ":
        write = True
        mylist[i] = c
    else:
        write = False
c = test() #lehet hiba van
def getPlayerMove(c):

    if c == ord('7'):
        i = 7
        rewrite(i)
        if write == True:
            screen.addstr(int(dims[0]/6),int(dims[1]/6), test())
    elif c == ord('8'):
        i = 8
        rewrite(i)
        if write == True:
            screen.addstr(int(dims[0]/6),int(dims[1]/2),test())
    elif c == ord('9'):
        i = 9
        rewrite(i)
        if write == True:
            screen.addstr(int(dims[0]/6),int(dims[1]/6*5),test())
    elif c == ord('4'):
        i = 4
        rewrite(i)
        if write == True:
            screen.addstr(int(dims[0]/6*3),int(dims[1]/6),test())
    elif c == ord('5'):
        i = 5
        rewrite(i)
        if write == True:
            screen.addstr(int(dims[0]/6*3),int(dims[1]/2),test())
    elif c == ord('6'):
        i = 6
        rewrite(i)
        if write == True:
            screen.addstr(int(dims[0]/6*3),int(dims[1]/6*5),test())
    elif c == ord('1'):
        i = 1
        rewrite(i)
        if write == True:
            screen.addstr(int(dims[0]/6*5),int(dims[1]/6),test())
    elif c == ord('2'):
        i = 2
        rewrite(i)
        if write == True:
            screen.addstr(int(dims[0]/6*5),int(dims[1]/2),test())
    elif c == ord('3'):
        i = 3
        rewrite(i)
        if write == True:
            screen.addstr(int(dims[0]/6*5),int(dims[1]/6*5),test())
    return()

screen = curses.initscr()
#bo = curses.initscr()
dims = screen.getmaxyx()
screen = curses.newwin(int(dims[0]), int(dims[1]),0 ,0)
screen.box()
for i in range (0, int(dims[0])):
    screen.addstr(i, int(dims[1]/3), '|')
    screen.addstr(i, int(dims[1]/3*2), '|')
for i in range (0, int(dims[1])):
    screen.addstr(int(dims[0]/3), i, '_')
    screen.addstr(int(dims[0]/3*2), i, '_')
    #screen.addstr(i, int(dims[1]), '|')
    #screen = curses.newwin(int(dims[0]/3),int(dims[1]/3),int(dims[0]-dims[0]/3) ,int(dims[1]-dims[1]/3))

curses.noecho()
curses.cbreak()
screen.keypad(True)
curses.curs_set(0)

# print ("Use the number keys to place the symbols or press 'q' to quit.")


while True:
    c = screen.getch()
    if c != ord('q'):
        getPlayerMove(c)
    else:
        break  # Exit the while loop:



# mvaddstr() moves to a given y,x coordinate first before displaying the string.
    #form: y, x, str or ch	Move to position y,x within the window, and display str or ch

curses.nocbreak()
screen.keypad(False)
curses.echo()
curses.endwin()
