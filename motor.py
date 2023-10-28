import RPi.GPIO as GPIO
import time
class Motor():
    def __init__(self, in1, in2, en):
        self.in1 = in1;
        self.in2 = in2;
        self.en = en;
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(in1, GPIO.OUT)
        GPIO.setup(in2, GPIO.OUT)
        GPIO.setup(en, GPIO.OUT)
        self.pi_pwm = GPIO.PWM(en,1000)
        self.pi_pwm.start(0)
    
    def forward(self, speed):
        print('forward')
        GPIO.output(self.in1, True)
        GPIO.output(self.in2, False)
        for x in range(0, int(speed), 1):
            self.pi_pwm.ChangeDutyCycle(x)
            time.sleep(1/speed)

    def backward(self, speed):
        print('backward')
        GPIO.output(self.in1, False)
        GPIO.output(self.in2, True)
        for x in range(0, int(speed), 1):
            self.pi_pwm.ChangeDutyCycle(x)
            time.sleep(1/speed)

    def brake(self, speed):
        print('brake')
        for x in range(int(speed), 0, -1):
            self.pi_pwm.ChangeDutyCycle(x)
            time.sleep(1/speed)
        GPIO.output(self.in1, False)
        GPIO.output(self.in2, False)

    def clean_up(self):
        print('clean up')
        self.pi_pwm.stop()
        GPIO.cleanup()    