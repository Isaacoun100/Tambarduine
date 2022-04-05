import pyfirmata
from pyfirmata import SERVO
from threading import Thread
from pyfirmata.util import Iterator
import time

board = pyfirmata.Arduino('COM3')

servoX = board.get_pin('d:10:o')
# servoY = board.get_pin('d:11:o')

IN3X = board.get_pin('d:3:o')
IN4X = board.get_pin('d:2:o')
IN1X = board.get_pin('d:5:o')
IN2X = board.get_pin('d:4:o')

IN3Y = board.get_pin('d:7:o')
IN4Y = board.get_pin('d:6:o')
IN1Y = board.get_pin('d:8:o')
IN2Y = board.get_pin('d:9:o')

IN3o = board.get_pin('d:12:o')
IN4o = board.get_pin('d:13:o')

LED = board.get_pin('d:11:o')

board.digital[10].mode = SERVO
# board.digital[11].mode = SERVO

Rango = int


def Abanico(AoB, Tempo):  # Este método no sirve pues el proyecto funciona solo sobre el eje X
    print("Hola soy abanico de: ", AoB, " y de: ", Tempo)
    # board.pass_time(Tempo)
    # if AoB == "A":
    #     servoX.write(120)
    #     board.pass_time(0.3)
    #     servoX.write(90)
    #     board.pass_time(0.3)
    # if AoB == "B":
    #     servoX.write(60)
    #     board.pass_time(0.3)
    #     servoX.write(90)
    #     board.pass_time(0.3)
    # else:
    #     return "Este método no acepta otra opcion que A o B"


def Percutor(Position, Tempo):
    board.pass_time(Tempo)
    PrenderLED()
    board.pass_time(0.1)
    ApagarLED()
    if Position == "D":
        board.digital[3].write(1)
        board.digital[2].write(0)
        board.pass_time(0.5)
        board.digital[3].write(0)
        board.digital[2].write(1)
        board.pass_time(0.5)
        board.digital[3].write(0)
        board.digital[2].write(0)
        board.pass_time(0.5)
    if Position == "I":
        board.digital[5].write(1)
        board.digital[4].write(0)
        board.pass_time(0.5)
        board.digital[5].write(0)
        board.digital[4].write(1)
        board.pass_time(0.5)
        board.digital[5].write(0)
        board.digital[4].write(0)
        board.pass_time(0.5)
    if Position == "A":
        board.digital[7].write(1)
        board.digital[6].write(0)
        board.pass_time(0.5)
        board.digital[7].write(0)
        board.digital[6].write(1)
        board.pass_time(0.5)
        board.digital[7].write(0)
        board.digital[6].write(0)
        board.pass_time(0.5)
    if Position == "B":
        board.digital[8].write(1)
        board.digital[9].write(0)
        board.pass_time(0.5)
        board.digital[8].write(0)
        board.digital[9].write(1)
        board.pass_time(0.5)
        board.digital[8].write(0)
        board.digital[9].write(0)
        board.pass_time(0.5)
    if Position == "DI":
        board.digital[3].write(0)
        board.digital[2].write(1)
        board.digital[5].write(1)
        board.digital[4].write(0)
        board.pass_time(0.5)
        board.digital[3].write(1)
        board.digital[2].write(0)
        board.digital[5].write(0)
        board.digital[4].write(1)
        board.pass_time(0.5)
        board.digital[3].write(0)
        board.digital[2].write(0)
        board.digital[5].write(0)
        board.digital[4].write(0)
        board.pass_time(0.5)
    if Position == "AB":
        board.digital[7].write(1)
        board.digital[6].write(0)
        board.digital[8].write(1)
        board.digital[9].write(0)
        board.pass_time(0.5)
        board.digital[7].write(0)
        board.digital[6].write(1)
        board.digital[8].write(0)
        board.digital[9].write(1)
        board.pass_time(0.5)
        board.digital[7].write(0)
        board.digital[6].write(0)
        board.digital[8].write(0)
        board.digital[9].write(0)
        board.pass_time(0.5)
    else:
        return "Este método no posee ninguna opción con el valor introducido"


def Golpe(Tempo):
    board.pass_time(Tempo)
    PrenderLED()
    board.pass_time(0.1)
    ApagarLED()
    board.digital[12].write(1)
    board.digital[13].write(0)
    board.pass_time(0.5)
    board.digital[12].write(0)
    board.digital[13].write(1)
    board.pass_time(0.5)
    board.digital[12].write(0)
    board.digital[13].write(0)
    board.pass_time(0.5)
    return


def Vibrato(n, Tempo):
    board.pass_time(Tempo)
    i = 0
    while n != i:
        PrenderLED()
        board.pass_time(0.1)
        ApagarLED()
        servoX.write(90)
        board.pass_time(0.3)
        servoX.write(120)
        board.pass_time(0.3)
        servoX.write(60)
        board.pass_time(0.3)
        i += 1
    servoX.write(90)
    board.pass_time(0.1)
    PrenderLED()
    board.pass_time(0.1)
    ApagarLED()
    return


def resetServoX():
    servoX.write(90)
    board.pass_time(0.3)


def SetServoX(grados):
    servoX.write(grados)
    board.pass_time(0.3)


def Vertical(DoI, Tempo):
    board.pass_time(Tempo)
    PrenderLED()
    board.pass_time(0.1)
    ApagarLED()
    if DoI == "D":
        servoX.write(120)
        board.pass_time(0.3)
        servoX.write(90)
        board.pass_time(0.3)
    if DoI == "I":
        servoX.write(60)
        board.pass_time(0.3)
        servoX.write(90)
        board.pass_time(0.3)
    else:
        return "Este método no acepta otra opcion que I o D"


def BeepLED(Tempo):
    board.digital[11].write(1)
    board.pass_time(Tempo)
    board.digital[11].write(0)
    board.pass_time(Tempo)


def PrenderLED():
    board.digital[11].write(1)


def ApagarLED():
    board.digital[11].write(0)


def Metronomo(AorD, RangoTiempo):
    if AorD == "D":
        while True:
            ApagarLED()
    if AorD == "A":
        while True:
            PrenderLED()
            board.pass_time(RangoTiempo)
            ApagarLED()
            board.pass_time(RangoTiempo)
    if RangoTiempo < 0:
        return "El metronomo debe recibir un argumento de tiempo positivo"
    else:
        if AorD != "A" or AorD != "D":
            return "El metronomo solo puede  recibir A (encendido) o D (apagado) como primer argumento"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    new_thread = Thread(BeepLED, 1)
    new_thread.start()
    Vibrato(10)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
