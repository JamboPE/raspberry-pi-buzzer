import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from udp_packet import send_packet
from config import Pi_PIN
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(Pi_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

const = False
while True: # Run forever
    if GPIO.input(Pi_PIN) == GPIO.HIGH and const == False:
        print("Button pushed")
        send_packet()
        const = True
    else:
        const = False