from test_modules.servo import Servo

S = Servo()

def iniciar():
    for i in range(32):
        S.set_servo_angle(i, 90)

iniciar()

while True:
    try:
        entrada = input("Introduce el número del servo (0-31) y el ángulo (0-180), separados por un espacio: ")
        partes = entrada.strip().split()

        if len(partes) != 2:
            print("Debes introducir dos valores: servo y ángulo.")
            continue

        servo_id = int(partes[0])
        angulo = int(partes[1])

        if 0 <= servo_id < 32 and 0 <= angulo <= 180:
            S.set_servo_angle(servo_id, angulo)
        else:
            print("Servo debe estar entre 0 y 31, y ángulo entre 0 y 180.")
    except ValueError:
        print("Entrada no válida. Asegúrate de introducir números enteros.")
