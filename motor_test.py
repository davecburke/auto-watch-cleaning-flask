import RPi.GPIO as GPIO
import time

class Motor:
    def __init__(self, in1, in2, en):
        self.in1 = in1
        self.in2 = in2
        self.en = en
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(in1, GPIO.OUT)
        GPIO.setup(in2, GPIO.OUT)
        GPIO.setup(en, GPIO.OUT)
        self.pi_pwm = GPIO.PWM(en, 1000)
        self.pi_pwm.start(0)
    
    def forward(self, speed):
        print(f'Moving forward at speed {speed}')
        GPIO.output(self.in1, True)
        GPIO.output(self.in2, False)
        self.pi_pwm.ChangeDutyCycle(speed)

    def backward(self, speed):
        print(f'Moving backward at speed {speed}')
        GPIO.output(self.in1, False)
        GPIO.output(self.in2, True)
        self.pi_pwm.ChangeDutyCycle(speed)

    def brake(self):
        print('Braking...')
        GPIO.output(self.in1, False)
        GPIO.output(self.in2, False)
        self.pi_pwm.ChangeDutyCycle(0)

    def clean_up(self):
        print('Cleaning up GPIO...')
        self.pi_pwm.stop()
        GPIO.cleanup()

if __name__ == "__main__":
    # Define motor pins
    in1 = 29
    in2 = 31
    en = 32
    
    motor = Motor(in1, in2, en)

    try:
        while True:
            cmd = input("\nEnter command (forward, backward, brake, exit): ").strip().lower()
            if cmd in ["forward", "backward"]:
                speed = input("Enter speed (0-100): ").strip()
                if speed.isdigit():
                    speed = int(speed)
                    if 0 <= speed <= 100:
                        if cmd == "forward":
                            motor.forward(speed)
                        else:
                            motor.backward(speed)
                    else:
                        print("Speed must be between 0 and 100!")
                else:
                    print("Invalid speed! Please enter a number.")
            elif cmd == "brake":
                motor.brake()
            elif cmd == "exit":
                break
            else:
                print("Invalid command! Use 'forward', 'backward', 'brake', or 'exit'.")
    
    except KeyboardInterrupt:
        print("\nInterrupted by user.")
    
    finally:
        motor.clean_up()
        print("Program terminated.")
