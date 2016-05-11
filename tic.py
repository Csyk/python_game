import curses
import time
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

#for i in range (1, 3):
    #screen.addstr(int(dims[0]/i), int(dims[1]/i), "_")
    #screen.refresh()
screen.getch()
curses.endwin()
