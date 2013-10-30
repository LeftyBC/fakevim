import curses
import curses.wrapper
import curses.textpad

def initborder(window):
    window.attrset(curses.color_pair(1))
    window.border()
    window.attrset(curses.color_pair(0))

def cursesapp(s):

    # initialize a blank window with a border
    height,width = s.getmaxyx()
    curses.use_default_colors()

    # default color pair for text
    # change on the fly with F9/F10
    text_color_pair = 3

    # color pair 1 is the pair that will be used for the border+background
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_WHITE)
    curses.init_pair(5, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_GREEN, curses.COLOR_WHITE)
    curses.init_pair(7, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(8, curses.COLOR_YELLOW, curses.COLOR_WHITE)
    s.keypad(1)

    # change this number to change the default background pair
    s.bkgd(' ',curses.color_pair(1))

    initborder(s)

    x=1
    y=1
    s.move(y,x)


    # setup
    while True:
        height,width = s.getmaxyx()
        c = s.getch()
        if c == 10: # CR
            y += 1
            x =  1
            s.move(y,x)
        elif c == 263: # backspace
            s.addch(y,x-1,32)
            x -= 1
        elif c == 12:
           s.refresh()
        elif c == 259: # up arrow
            y -= 1
        elif c == 258: # down arrow
            y += 1
        elif c == 260: # left arrow
            x -= 1
        elif c == 261: # right arrow
            x += 1
        elif c == 273: # F9
            text_color_pair = (text_color_pair - 1) % 8
        elif c == 274: # F10
            text_color_pair = (text_color_pair + 1) % 8

        elif 255 > c  and 32 <= c :
            # printable ascii char, emit it with the current color
            s.attrset(curses.color_pair(text_color_pair))
            s.addstr(y,x,
                curses.keyname(c)
            )
            s.attrset(curses.color_pair(0))
            x += 1

        if x < 1:
            x = 1;
        if x >= width:
            x = 1;
            y += 1;
        if y >= height:
            y = height - 1

        initborder(s)
        s.addstr(0,1,"Pos: (%d,%d) Key: [%s] (%d) Color: %d" % (y,x,curses.keyname(c),c,text_color_pair))
        s.move(y,x)
        s.attrset(curses.color_pair(0))
        s.refresh()



curses.wrapper(cursesapp)

