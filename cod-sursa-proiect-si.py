import RPi.GPIO as GPIO
import time
from datetime import datetime

servo_pin = 14
pass_wrong_times = 0
key_list = [["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"],
            ["*", "0", "#"]]
lines = [2, 3, 4, 17]
columns = [5, 13, 6]
phone_number = "+12029028256"

def setup_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(servo_pin, GPIO.OUT)
    GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(22, GPIO.OUT)
    GPIO.setup(27, GPIO.OUT)
    GPIO.setup(23, GPIO.OUT)

    for pin in [2, 3, 4, 17]:
        GPIO.setup(pin, GPIO.OUT)

    GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def initialize_pwm():
    p = GPIO.PWM(servo_pin, 50)  # 50hz frequency
    p.start(2.5)  # starting duty cycle ( it sets the servo to 0 degrees)
    return p

def send_message():
    now = datetime.now()
    formatted_date = now.strftime('%Y-%m-%d')
    current_time = datetime.now()
    formatted_time = current_time.strftime('%H:%M:%S')
    final_date_and_time = formatted_date + " " + formatted_time
    # Your Twilio client code goes here

def right_password():
    GPIO.output(27, GPIO.HIGH)
    time.sleep(2)

def wrong_password():
    GPIO.output(22, GPIO.HIGH)
    time.sleep(2)

def set_all_lines():
    for line in lines:
        GPIO.output(line, GPIO.HIGH)

def check_all_columns_are_low(line):
    GPIO.output(line, GPIO.HIGH)
    time.sleep(0.01)  # Allow time for the lines to stabilize
    for column in columns:
        if GPIO.input(column) == 1:
            GPIO.output(line, GPIO.LOW)
            return False
    GPIO.output(line, GPIO.LOW)
    return True

def read_line(line, characters):
    GPIO.output(line, GPIO.HIGH)
    time.sleep(0.01)  # Allow time for the lines to stabilize
    for i, column in enumerate(columns):
        if GPIO.input(column) == 1:
            full_pass.append(characters[i])
    GPIO.output(line, GPIO.LOW)

def make_buzzer_sound():
    send_message()
    GPIO.output(23, GPIO.HIGH)
    time.sleep(3)
    GPIO.output(23, GPIO.LOW)

def main():
    global full_pass
    full_pass = ""
    keypadPressed = -1

    GPIO.add_event_detect(columns[0], GPIO.RISING, callback=keypadCallback)
    GPIO.add_event_detect(columns[1], GPIO.RISING, callback=keypadCallback)
    GPIO.add_event_detect(columns[2], GPIO.RISING, callback=keypadCallback)

    p = initialize_pwm()
    setup_gpio()

    while True:
        if GPIO.input(26) == GPIO.HIGH:
            p.ChangeDutyCycle(10)
            right_password()
            GPIO.output(23, GPIO.LOW)
            time.sleep(3)
            GPIO.output(27, GPIO.LOW)
            GPIO.output(23, GPIO.LOW)
            p.ChangeDutyCycle(2.5)

        if keypadPressed != -1:
            set_all_lines()
            if GPIO.input(keypadPressed) == 0:
                keypadPressed = -1
            else:
                time.sleep(0.1)
        else:
            if "#" in full_pass:
                parsed_pass = full_pass[:-1]
                if parsed_pass == "1234":
                    p.ChangeDutyCycle(10)
                    right_password()
                    time.sleep(3)
                    GPIO.output(27, GPIO.LOW)
                    p.ChangeDutyCycle(2.5)
                    full_pass = ""
                    is_open = True
                    pass_wrong_times = 0
                else:
                    wrong_password()
                    pass_wrong_times += 1
                    print(pass_wrong_times)
                    if pass_wrong_times == 3:
                        pass_wrong_times = 0
                        make_buzzer_sound()
                    GPIO.output(22, GPIO.LOW)
                    full_pass = ""
            else:
                for i in range(len(lines)):
                    if check_all_columns_are_low(lines[i]):
                        read_line(lines[i], key_list[i])
                        time.sleep(0.01)

if __name__ == "__main__":
    main()
