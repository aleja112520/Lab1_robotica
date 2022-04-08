# Lab1_robotica
# Estudiantes: Alejandra Rojas - Juan Diego Plaza
## Ejercicios en el laboratorio:
***
a.  Familiarizarse  con  los  comandos  de  mayor  uso  para  la  consola  de  Linux  (veáse http://www.informit.com/blogs/blog.aspx?uk=The-10-Most-Important-Linux-Commands)

  En el sitio web al que se hace referencia, se nombran 10 comandos que pueden escribirse en el terminal de Linux y por medio de los cuales se quiere hacer más sencilla la interacciòn con la máquina. Los comandos que se nombraron fueron:
  
  - **pwd**:
  Este comando imprime la dirección del directior en el que estás. 

  - **ls**:
  Con este comando se imprime un listado con todos los archivos que existen en un directorio dado. Ej: ls cd/matlab

  - **cd**:
  con este comando  se cambia el directorio en el que se esté trabajando por el direcotiro especificado. Ej: cd /Dowloads/user

  - **touch**:
  Este comando crea un archivo en blando en el directorio actual usando el nombre que se le especifique. Ej: touch archivo

  - **rm**:
  El comando rm borra el archivo con el nombre especificado dentro del directorio actual. Ej rm archivo

  - **mkdir**:
  Este comando crea un directorio en el directorio actual, se debe especificar el nombre del directorio. Ej: mkdir directorio

  - **rmdir**:
  Con este comando se logra borrar el directorio con el nombre especificado dentro del directorio actual. Ej: rmdir directorio

  - **mv** :
  Este comando se usa para cambiar la ubicaciòn de un archivo o directorio que se especifique, tambièn se suele usar este comando para renombrar un archivo o directorio al mismo tiempo que se cambia de ubicaciòn. En el siguiente ejemplo se movera el archivo "user" a un subdirectorio "equipo" que se encuentra en el directorio actual, y ademàs se cambiarà el nombre de user por un nuevo nombre "home". Ej: mv user equipo/home

  - **cp**:
  Este comando se usa de la misma manera que el comando mv, la diferencia entre estos dos comandos radica que con este el archivo original permanecerà en la misma direcciòn, mientras que con la funciòn mv, el archivo original ya no estarà en la posiciòn inicial.

  - **man**:
  Este comando muestra el manual de uso del comando espicificado   Ej: man mv                                                                                                                                                                                                       
***
b)Conexiòn de ROS con Matlab.
- Con Linux operando lanzar 2 terminales. En la primera terminal escribir el comando roscore para iniciar el nodo maestro.
![](https://postimg.cc/kDV4pdwF)
- En la segunda terminal escribir rosrun turtlesim turtlesim_node.


- Lanzar una instancia de Matlab para Linux 
- Crear un script con el siguiente código:
```matlab
%%
rosinit; %Conexión con nodo maestro
%%
velPub = rospublisher(’/turtle1/cmd_vel’,’geometry_msgs/Twist’); %Creación publicador
velMsg = rosmessage(velPub); %Creacion de mensaje
%%
velMsg.Linear.X = 1; %Valor del mensaje
send(velPub,velMsg); %Envio
pause(1)
```
-Ejecutar las tres secciones del script y observar los resultados con la pose de la tortuga.
-Crear un script en Matlab que permita suscribirse al tópico de pose de la simulación de turtle1.  
Tip:Usar la instrucción rossubscriber con los argumentos (’TOPICNAME’, ’MESSAGETY-PE’), luego utilizar la opción lattest messagepara captura el último mensaje obtenido.
-Crear un script en Matlab que permita enviar todos los valores asociados a la pose deturtle1.
Tip:El topicopose únicamente sirve para suscribirse, consultar los servicios de turtlesim para modificar la pose de la tortuga.
-Consultar de qué manera se finaliza el nodo maestro en Matlab

c) Utilizando Python:
  - En el paquete *hello_turtle* de ROS, en la carpeta de scripts, crear un *script* de Python, de nombre *myTeleopKey.py*
  En esta parte se puede recurrir la opción de abrir carpetas y archivos que dispone VSCode en la parte superior izquierda de su interfaz de usuario.
  
  ![This is an image](https://i.postimg.cc/4xfknmYw/Screenshot-from-2022-04-07-20-35-40.png)
  
  De esta manera se abre una nueva ventana en la cual se debe seleccionar la carpeta *catkin*, preparada con el paquete *hello_turtle* y la carpeta de destino *scripts*.
  
  ![This is an image](https://i.postimg.cc/BQcbdPWC/Screenshot-from-2022-04-07-20-41-17.png)
  
  Posterior a ello se hace uso del explorador de archivos de VSCode para recorrer el camino hasta la carpeta *hello_turtle* y finalemente hasta *scripts*, en donde se da click en la opción de crear un nuevo documento, para así crear el archivo *myTeleopKey.py*.
  
  ![This is an image](https://i.postimg.cc/Vkfv1smP/Screenshot-from-2022-04-07-20-45-38.png)
  
  ![This is an image](https://i.postimg.cc/vTnhQL7T/Screenshot-from-2022-04-07-21-03-14.png)
  
  - Escribir un código que permita operar una tortuga del paquete turtlesim con el teclado, que cumpla con las siguientes especificaciones:
    - Se debe mover hacia adelante y hacia atrás con las teclas W y S.
    - Debe girar en sentido horario y antihorario con las teclas D y A.
    - Debe retornar a su posición y orientación centrales con la tecla R.
    - Debe dar un giro de 180° con la tecla ESPACIO.
    
    Para desarrollar este punto se abre el archivo creado en el estamento anterior y se procede a escribir el código correspondiente.
    Este código se inicia importango las librerías y herramientas que se consideran necesarias, como la de *rospy* para establecer conexión con el nodo maestro de ROS, el parámetro Twist para alterar las velocidades lineales y angulares, el  parámetro TeleportAbsolute para modificar la posición de la tortuga y el parámetro TeleportRelative para hacer el giro de 180° mencionado. De la misma manera se importa la constante *pi* y las librerías termios, sys y os para la detección de entradas por teclado.
    
    ```python
    import rospy
    from geometry_msgs.msg import Twist 
    from turtlesim.srv import TeleportAbsolute, TeleportRelative
    from numpy import pi
    import termios, sys, os
    ```
    A partir de aquí se define la función principal *keyControl* que se encarga de asignar a cada tecla presionada una acción respectiva. Para iniciar esta función se define que el nodo es uno del tipo "talker", es decir, que se dedica a publicar información al tópico */turtle1/cmd_vel* usando el tipo de mensaje *Twist*. Luego, en la siguiente línea se inicia el nodo con el nombre "velPub" y se declara que se mantenga anónima su identidad para así evitar mostrar el código que complementa su nombre y que no aporta información relevante para esta práctica. Siguiendo con el proceso se crea la variable *vel*, a la que se le asigna la estructura *Twist*, que presenta el formato del vector de información con las velocidades angulares y lineales de la tortuga, de la misma manera también se añade el objeto *rospy.Rate*, el cual controla la taza de ejecución.
    
```python
def keyControl():
  pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
  rospy.init_node('velPub', anonymous=False)
  vel = Twist()
  rate = rospy.Rate(10) 
```
   Después de ese primer bloque de código, se construye un ciclo while que permite que el código se esté ejecutando hasta que haya una interrupción por teclado del tipo Ctrl + c en la consola de Ubuntu. En este while se construye la respectiva concatenación de condicionales que asignan una acción a ciertas letras detectadas, por ejemplo, en el siguiente bloque de código se muestra la asignación de ordenes para los movimientos lineales con las letras "W" y "S" y los movimientos rotacionales con las letras "A" y "D", y así se muestra cuando se detecta el caracter "w" o "W", con el que se asigna una velocidad linear en la dirección de *x* a la tortuga. La publicación de esta información se hace más adelante para no interferir con el flujo de los condicionales. Cabe aclarar que para esto se utiliza la función *getkey* que retorna datos como bytes (por eso la b antes de las comillas en los condicionales). Esta función será tratada en mayor profundidad después, por ahora lo único importante a saber es que esta le pasa los valores que detecta a la variable *letter* que es usada en cada condicional para verificar cuál fue el caracter utilizado.
   
```python
  while not rospy.is_shutdown():
      letter = getkey()
      if letter == b'D' or letter == b'd':
          vel.angular.z = -0.5
      elif letter == b'A' or letter == b'a':
          vel.angular.z = 0.5
      elif letter == b'W' or letter == b'w':
          vel.linear.x = 0.5
      elif letter == b'S' or letter == b's':
          vel.linear.x = -0.5
```
    
  En el siguiente bloque de código se presenta la acción de restaurar la posición inicial cuando se presiona la letra "R". Para ello se hace uso del servicio *teleport_absolute* que permite teletransportar la tortuta a cualquier punto de la ventana a partir de un sistema coordenado absoluto. Para esto se usa la función *rospy.wait_for_service* que permite saber cuando un servicio está disponible y así poder usar correctamente la función *rospy.ServiceProxy* que permite llamar al servicio en cuestión y crear objetos como el *teleportA* que se muestra acompañando a esta última función. Luego para alterar la posición de la tortuga se le pasan como parámetros al objeto *teleportA* las coordenadas que describen la posición inicial en *x* y *y*. Todo esto desarrollado en un entorno *try* *exception* para gestionar errores en caso de que haya problema conectandose con el servicio.
    
```python
    elif letter == b'R' or letter == b'r':

    rospy.wait_for_service('/turtle1/teleport_absolute')
    try:
        teleportA = rospy.ServiceProxy('/turtle1/teleport_absolute', TeleportAbsolute)
        resp1 = teleportA(5, 5, 0)
        print('Back again in start position')
    except rospy.ServiceException as e:
        print(str(e))
```
Continuando con los condicionales concatenados, ahora viene el caso para el giro de 180°, el cual no se podía realizar con el anterior servicio, ya que este ignoraría la posición actual de la tortuga porque todos sus movimientos son respecto a un marco absoluto. Teniendo esto en cuenta, para el caso cuando se presiona la tecla espaciadora (" ") se usan funciones similares, ya que de manera similar se debe esperar a que el servicio se encuentre disponible y cuando este esté disponible hacerle un llamado para poder transmitir los datos deseados, que en esta ocación se hacen con el opjeto *teleportR*.

```python
     elif letter == b' ':

    rospy.wait_for_service('/turtle1/teleport_relative')
    try:
        teleportR = rospy.ServiceProxy('/turtle1/teleport_relative', TeleportRelative)
        resp2 = teleportR(0, pi)
        print('Turned 180 degrees')
    except rospy.ServiceException as e:
        print(str(e))
```
Por último se hace la publicación de los datos asignados al vector *vel* con la función del objeto *pub*, *publish*, y se le asignan valores nulos tanto a la velocidad lineal en *x* como a la angular en *z*, para que no afecten en los movimientos futuros de la tortuga, ya que si se conservan las velocidades asignadas en un movimiento pasado, el movimiento siguiente las conservaría y no se lograría el resultado esperado.

```python
    pub.publish(vel)
    vel.angular.z = 0
    vel.linear.x = 0
```



  - Incluir el script que se acaba de crear en el apartado de *catkin_install_python* del archivo *CMakeLists.txt*, siguiendo la misma estructura de los otros scripts ya incluidos.
  - Lanzar una terminal, dirigirse al directorio del workspace de *catkin* y escribir el comando *catkin make* para hacer build en el paquete modificado.
  - Con Linux operando lanzar 3 terminales. En la primera terminal escribir el comando *roscore* para iniciar el nodo maestro.
  - En la segunda terminal escribir *rosrun turtlesim turtlesim node*. 
  - En la tercera terminal dirigirse al directorio que contiene el workspace de catkin y escribir source *devel/setup.bash*. Acto seguido escribir rosrun *hello_turtle myTeleopKey.py*. En este punto, la terminal ya debería estar esperando el ingreso de teclas.
