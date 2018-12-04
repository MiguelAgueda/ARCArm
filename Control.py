from Movements import Movements
import Adafruit_PCA9685 as Ada
from curses import wrapper


mv = Movements()


# ASCII Codes for arrow keys
up = 259
down = 258
left = 260
right = 261


def main(stdscr):
    stdscr.clear()
    stdscr.refresh()
    return stdscr.getch()


def key_press():
    key = wrapper(main)
    # print("Key: " + str(key))

    if key == ord('w'):
        mv.up(1)
    if key == ord('s'):
        mv.down(1)
    if key == ord('a'):
        mv.up(0)
    if key == ord('d'):
        mv.down(0)
    if key == up:
        mv.down(2)  # Must reverse direction so movement is intuitive
    if key == down:
        mv.up(2)  # Must reverse direction so movement is intuitive
    if key == left:
        mv.up(3)
    if key == right:
        mv.down(3)
    if key == ord('h'):
        mv.home()


choice = input("To access robotic arm movement, press ENTER.\nTo exit, enter any character.\n\n> ")

if choice == '':
    mv.home()
    while True:
        try:
            key_press()
        except KeyboardInterrupt:
            print("Exiting Program")
            quit()
else:
    quit()
