import time

def test_Servo():
    from servo import Servo
    servo = Servo()
    try:
        for i in range(50):
            servo.set_servo_angle(15,90+i)
            servo.set_servo_angle(12,90+i)
            servo.set_servo_angle(9,90+i)
            servo.set_servo_angle(16,90+i)
            servo.set_servo_angle(19,90+i)
            servo.set_servo_angle(22,90+i)
            time.sleep(0.005)
        for i in range(60):
            servo.set_servo_angle(14,90+i)
            servo.set_servo_angle(11,90+i)
            servo.set_servo_angle(8,90+i)
            servo.set_servo_angle(17,90-i)
            servo.set_servo_angle(20,90-i)
            servo.set_servo_angle(23,90-i)
            time.sleep(0.005)
        for i in range(120):
            servo.set_servo_angle(13,i)
            servo.set_servo_angle(10,i)
            servo.set_servo_angle(31,i)
            servo.set_servo_angle(18,180-i)
            servo.set_servo_angle(21,180-i)
            servo.set_servo_angle(27,180-i)
            time.sleep(0.005)
        print ("\nEnd of program")      
        servo.relax()
    except KeyboardInterrupt:
        servo.relax()
        print ("\nEnd of program")


if __name__ == '__main__':
    print ('Program is starting ... ')
    test_Servo()      
        
        
        