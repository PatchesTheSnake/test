def on_button_pressed_a():
    global freq, rps
    if test == 1:
        freq += 1
        messageing.connect(freq)
    elif test == 0:
        messageing.send_string("con")
    elif test == -1:
        rps += 1
        if rps == 1:
            basic.show_icon(IconNames.SQUARE)
        if rps == 2:
            basic.show_leds("""
                . . . . .
                            . # # # .
                            . # # # .
                            . # # # .
                            . . . . .
            """)
        if rps == 3:
            basic.show_icon(IconNames.SCISSORS)
input.on_button_pressed(Button.A, on_button_pressed_a)

def win(pl1: number, pl2: number):
    if pl1 > pl2:
        if pl1 == 3 and pl2 == 1:
            return 1
        else:
            return 2
    elif pl1 < pl2:
        if pl2 == 3 and pl1 == 1:
            return 2
        else:
            return 1
    return 3

def on_received_string(receivedString):
    global test, rpsr
    if receivedString == "con":
        if test == 1:
            messageing.send_string("ok")
            # basic.showString("connected")
            
            test = -1
            basic.clear_screen()
            basic.show_icon(IconNames.SQUARE)
    elif receivedString == "ok":
        # basic.showString("connected")
        basic.clear_screen()
        basic.show_icon(IconNames.SQUARE)
        test = -1
    elif receivedString.substr(0, 2) == "12":
        rpsr = parse_float(receivedString.substr(2))
messageing.on_received_string(on_received_string)

def on_button_pressed_ab():
    global test
    # if (rpsr == 1) {
    # basic.showIcon(IconNames.Square)
    # }
    # if (rpsr == 2) {
    # basic.showIcon(IconNames.SmallSquare)
    # }
    # if (rpsr == 3) {
    # basic.showIcon(IconNames.Scissors)
    # }
    if test == 1:
        test = 0
        messageing.connect(freq)
        messageing.send_string("con")
    elif test == -1:
        test = -2
        messageing.send_string("12" + str(rps))
    elif test == -2:
        basic.show_number(win(rps, rpsr))
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global freq, test, rps
    if test == 1:
        freq += -1
        messageing.connect(freq)
    elif test == 0:
        test = 1
    elif test == -1:
        rps += -1
        if rps == 1:
            basic.show_icon(IconNames.SQUARE)
        if rps == 2:
            basic.show_leds("""
                . . . . .
                            . # # # .
                            . # # # .
                            . # # # .
                            . . . . .
            """)
        if rps == 3:
            basic.show_icon(IconNames.SCISSORS)
input.on_button_pressed(Button.B, on_button_pressed_b)

test = 0
rpsr = 0
rps = 1
freq = 0
basic.show_number(0)
radio.send_number(0)
freq = 1
rps = 0
rpsr = 0
test = 1
messageing.connect(freq)