import RPi.GPIO as GPIO
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
        self.pi_pwm.ChangeDutyCycle(speed)

    def backward(self, speed):
        print('backward')
        GPIO.output(self.in1, False)
        GPIO.output(self.in2, True)
        self.pi_pwm.ChangeDutyCycle(speed)

    def brake(self):
        print('brake')
        GPIO.output(self.in1, False)
        GPIO.output(self.in2, False)

    def clean_up(self):
        print('clean up')
        GPIO.cleanup()    