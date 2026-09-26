import machine
import utime

# --- UART Setup for HC-05/HC-06 (UART 0) ---
uart = machine.UART(0, baudrate=9600, tx=machine.Pin(0), rx=machine.Pin(1))

# --- Motor Pins Setup ---
in1 = machine.Pin(6, machine.Pin.OUT)
in2 = machine.Pin(7, machine.Pin.OUT)
in3 = machine.Pin(8, machine.Pin.OUT)
in4 = machine.Pin(9, machine.Pin.OUT)

def stop():
    in1.value(0)
    in2.value(0)
    in3.value(0)
    in4.value(0)

def forward():
    in1.value(1)
    in2.value(0)
    in3.value(1)
    in4.value(0)

def backward():
    in1.value(0)
    in2.value(1)
    in3.value(0)
    in4.value(1)

def turn_left():
    in1.value(0)
    in2.value(1)
    in3.value(1)
    in4.value(0)

def turn_right():
    in1.value(1)
    in2.value(0)
    in3.value(0)
    in4.value(1)
stop()
print("Bluetooth Robot Ready.")

while True:
    if uart.any():
        command = uart.read().decode('utf-8').strip().upper()
        print("Received command:", command)

        # Process movement commands
        if command == 'W':
            forward()
            print("forward")
        elif command == 'S':
            backward()
            print("back")
        elif command == 'A':
            turn_left()
            print("left")
        elif command == 'D':
            turn_right()
            print("right")
        elif command == 'X':
            stop()
            print("stop")

    utime.sleep_ms(20)