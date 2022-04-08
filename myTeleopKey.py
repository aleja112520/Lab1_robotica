import rospy
from geometry_msgs.msg import Twist 
from turtlesim.srv import TeleportAbsolute, TeleportRelative
from numpy import pi
import termios, sys, os


def keyControl():
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10) #Declara el nodo como talker
    rospy.init_node('velPub', anonymous=False) #Inicia el nodo con el nombre "velPub"
    vel = Twist()   #Hace que la variable vel tome el formato de Twist, para que así pueda contener
                    #información acerca de las velocidades lineales y angulares de la tortuga
    rate = rospy.Rate(10) #Define la frecuencia de ejecución

    while not rospy.is_shutdown(): #Ciclo while que se ejecuta hasta que haya alguna interrupción

        letter = getkey() #Almacenamiento del carácter detectado por la función getkey

        if letter == b'D' or letter == b'd':
            vel.angular.z = -0.5    #Giro en sentido de las manecillas del reloj
        elif letter == b'A' or letter == b'a':
            vel.angular.z = 0.5     #Giro en contra de las manecillas del reloj
        elif letter == b'W' or letter == b'w':
            vel.linear.x = 0.5      #Movimiento hacia adelante
        elif letter == b'S' or letter == b's':
            vel.linear.x = -0.5     #Movimiento hacia atrás
            
        elif letter == b'R' or letter == b'r':

            rospy.wait_for_service('/turtle1/teleport_absolute') #Consulta de disponibilidad del servicio
            try:
                teleportA = rospy.ServiceProxy('/turtle1/teleport_absolute', TeleportAbsolute) #Llamada al servicio
                resp1 = teleportA(5.5, 5.5, 0) #Transmisión de información al servicio
                print('Back again in start position')
            except rospy.ServiceException as e:
                print(str(e))
        
        elif letter == b' ':
            
            rospy.wait_for_service('/turtle1/teleport_relative') #Consulta de disponibilidad del servicio
            try:
                teleportR = rospy.ServiceProxy('/turtle1/teleport_relative', TeleportRelative) #Llamada al servicio
                resp2 = teleportR(0, pi) #Transmisión de información al servicio
                print('Turned 180 degrees')
            except rospy.ServiceException as e:
                print(str(e))

        pub.publish(vel) #Publicación de los datos de las velocidades angulares y lineales
        vel.angular.z = 0 #Reseteo de las velocidades modificadas
        vel.linear.x = 0
        rate.sleep() #Se encarga de mantener la frecuencia establecida anteriormente por rospy.Rate()

TERMIOS = termios


def getkey():
    fd = sys.stdin.fileno() 
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] = new[3] & ~TERMIOS.ICANON & ~TERMIOS.ECHO
    new[6][TERMIOS.VMIN] = 1 
    new[6][TERMIOS.VTIME] = 0 
    termios.tcsetattr(fd, TERMIOS.TCSANOW, new) 
    c = None
    try:
        c = os.read(fd, 1)
    
    finally:
        termios.tcsetattr(fd, TERMIOS.TCSAFLUSH, old)
    return c


if __name__ == '__main__':
    try:
        keyControl()
    except rospy.ROSInterruptException:
        pass