from pynput.mouse import Button, Controller
import time
mouse = Controller()

Xposition = mouse.position[0]
Yposition = mouse.position[1]
step = 10


while True:
    print("sapientiae timor domini")
    print("click ctrl+c here to stop the mouse program")
    mouse.click(Button.left, 1)
    mouse.position = (Xposition + step,Yposition + step)
    time.sleep(10)
    mouse.position = (Xposition - step,Yposition - step)
    time.sleep(10)
    
    
