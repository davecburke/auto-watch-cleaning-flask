import RPi.GPIO as GPIO
class Heater():
    def __init__(self, in1, in2, en, element):
        print(in1)
        print(in2)
        print(en)
        self.in1 = in1;
        self.in2 = in2;
        self.en = en;
        self.element = element
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(in1, GPIO.OUT)
        GPIO.setup(in2, GPIO.OUT)
        GPIO.setup(en, GPIO.OUT)
        GPIO.setup(element, GPIO.OUT)
        # self.pi_pwm = GPIO.PWM(en,1000)
        # self.pi_pwm.start(0)
    
    def on(self):
        print('heater on')
        print(self.in1)
        print(self.en)
        GPIO.output(self.in1, True)
        GPIO.output(self.in2, False)
        GPIO.output(self.en, True)
        GPIO.output(self.element, True)

    def off(self):
        print('heater off')
        GPIO.output(self.in1, False)
        GPIO.output(self.in2, False)
        GPIO.output(self.en, False)
        GPIO.output(self.element, False)