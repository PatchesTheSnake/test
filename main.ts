input.onButtonPressed(Button.A, function () {
    if (test == 1) {
        freq += 1
        messageing.connect(freq)
    } else if (test == 0) {
        messageing.sendString("con")
    } else if (test == -1) {
        rps += 1
    }
})
function win (pl1: number, pl2: number) {
    if (pl1 < pl2) {
        if (pl1 == 3 && pl2 == 1) {
            return 1
        } else {
            return 2
        }
    } else if (pl1 > pl2) {
        if (pl2 == 3 && pl1 == 1) {
            return 2
        } else {
            return 1
        }
    }
    return 3
}
messageing.onReceivedString(function (receivedString) {
    if (receivedString == "con") {
        if (test == 1) {
            messageing.sendString("ok")
            basic.showString("connected")
            test = -1
        }
    } else if (receivedString == "ok") {
        basic.showString("connected")
        test = -1
    } else if (receivedString.substr(0, 2) == "12") {
        rpsr = parseFloat(receivedString.substr(2))
    }
})
input.onButtonPressed(Button.AB, function () {
    // if (rpsr == 1) {
    // basic.showIcon(IconNames.Square)
    // }
    // if (rpsr == 2) {
    // basic.showIcon(IconNames.SmallSquare)
    // }
    // if (rpsr == 3) {
    // basic.showIcon(IconNames.Scissors)
    // }
    if (test == 1) {
        test = 0
        messageing.connect(freq)
        messageing.sendString("con")
    } else if (test == -1) {
        test = -2
        messageing.sendString("12" + rps)
    } else if (test == -2) {
        basic.showNumber(win(rps, rpsr))
    }
})
input.onButtonPressed(Button.B, function () {
    if (test == 1) {
        freq += -1
        messageing.connect(freq)
    } else if (test == 0) {
        test = 1
    } else if (test == -1) {
        rps += -1
    }
})
let test = 0
let rpsr = 0
let rps = 0
let freq = 0
basic.showNumber(0)
radio.sendNumber(0)
freq = 1
rps = 0
rpsr = 0
test = 1
messageing.connect(freq)
