input.onButtonPressed(Button.A, function () {
    basic.clearScreen()
    basic.showIcon(IconNames.Happy)
})
input.onButtonPressed(Button.B, function () {
    basic.clearScreen()
    basic.showIcon(IconNames.Sad)
})
input.onLogoEvent(TouchButtonEvent.Touched, function () {
    basic.clearScreen()
    basic.showIcon(IconNames.Confused)
})
for (let index = 0; index < 4; index++) {
    basic.clearScreen()
    basic.pause(500)
    basic.showIcon(IconNames.Heart)
}
