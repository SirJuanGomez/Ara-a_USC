from test_modules.servo import Servo

S = Servo()

list_m_d = [14, 11, 2]
list_m_i = [17, 20, 30]
list_p_d = [13, 10, 1]
list_p_i = [18, 21, 31]

# Posiciones específicas para cada grupo
pos_m_d = 170
pos_m_i = 10
pos_p_d = 90
pos_p_i = 90

while True:
    # Mueve los servos del grupo m_d
    for servo_id in list_m_d:
        S.mover(servo_id, pos_m_d)

    # Mueve los servos del grupo m_i
    for servo_id in list_m_i:
        S.mover(servo_id, pos_m_i)

    # Mueve los servos del grupo p_d
    for servo_id in list_p_d:
        S.mover(servo_id, pos_p_d)

    # Mueve los servos del grupo p_i
    for servo_id in list_p_i:
        S.mover(servo_id, pos_p_i)

    print("Todos los servos fueron movidos a sus posiciones respectivas.")
    break  # Elimina esto si quieres que siga corriendo en bucle
