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
<img src="https://i.postimg.cc/RCdHqSH8/Captura-de-pantalla-de-2022-04-07-16-27-20.png" alt="drawing" width="600"/>

- En la segunda terminal escribir rosrun turtlesim turtlesim_node.
<img src="https://i.postimg.cc/x1F27MRh/Captura-de-pantalla-de-2022-04-07-16-30-22.png" alt="drawing" width="600"/>
- Lanzar una instancia de Matlab para Linux 
<img src="https://i.postimg.cc/CLcTBkW5/Captura-de-pantalla-de-2022-04-07-17-21-20.png" alt="drawing" width="600"/>
- Crear un script con el siguiente código:

```
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

<img src="https://i.postimg.cc/Twx55v9T/Captura-de-pantalla-de-2022-04-07-17-23-38.png" alt="drawing" width="600"/>

-Ejecutar las tres secciones del script y observar los resultados con la pose de la tortuga.


-Crear un script en Matlab que permita suscribirse al tópico de pose de la simulación de turtle1.  

Tip:Usar la instrucción rossubscriber con los argumentos (’TOPICNAME’, ’MESSAGETY-PE’), luego utilizar la opción lattest messagepara captura el último mensaje obtenido.

<img src="https://i.postimg.cc/y8Wbtw06/Captura-de-pantalla-de-2022-04-07-17-25-38.png" alt="drawing" width="600"/>

-Crear un script en Matlab que permita enviar todos los valores asociados a la pose de turtle1.

Tip:El topicopose únicamente sirve para suscribirse, consultar los servicios de turtlesim para modificar la pose de la tortuga.
<img src="https://i.postimg.cc/50Ln5JLy/Captura-lab1-robot.png" alt="drawing" width="600"/>

Primero se crea un objeto tipo cliente con nombre "/turtle1/teleport_absolute", luego se crea un mensaje cuyo dato de entrada es el objeto creado anteriormente. En las líneas posteriores se modifican los parámetros X=3 Y=5 y Theta=1.5 del mensaje, finalmente se envía el mensaje con la función call y se le pone de entrada el mensaje y objeto tipo cliente creado. 

-Consultar de qué manera se finaliza el nodo maestro en Matlab
<img src="https://i.postimg.cc/YSGTGJSD/Captura-de-pantalla-de-2022-04-07-17-27-09.png" alt="drawing" width="600"/>

c) Utilizando Python:
  - En el paquete *hello_turtle* de ROS, en la carpeta de scripts, crear un *script* de Python, de nombre *myTeleopKey.py*
  En esta parte se puede recurrir la opción de abrir carpetas y archivos que dispone VSCode en la parte superior izquierda de su interfaz de usuario.
  ![This is an image](https://i.postimg.cc/4xfknmYw/Screenshot-from-2022-04-07-20-35-40.png)
  
  De esta manera se abre una nueva ventana en la cual se debe seleccionar la carpeta *catkin*, preparada con el paquete *hello_turtle* y la carpeta de destino *scripts*.
  ![This is an image](https://i.postimg.cc/2jgnzZKR/Screenshot-from-2022-04-07-20-45-38.png)
  
  - Escribir un código que permita operar una tortuga del paquete turtlesim con el teclado, que cumpla con las siguientes especificaciones:
    - Se debe mover hacia adelante y hacia atr ́as con las teclas W y S.
    - Debe girar en sentido horario y antihorario con las teclas D y A.
    - Debe retornar a su posici ́on y orientaci ́on centrales con la tecla R.
    - Debe dar un giro de 180° con la tecla ESPACIO.
  - Incluir el script que se acaba de crear en el apartado de *catkin_install_python* del archivo *CMakeLists.txt*, siguiendo la misma estructura de los otros scripts ya incluidos.
  - Lanzar una terminal, dirigirse al directorio del workspace de *catkin* y escribir el comando *catkin make* para hacer build en el paquete modificado.
  - Con Linux operando lanzar 3 terminales. En la primera terminal escribir el comando *roscore* para iniciar el nodo maestro.
  - En la segunda terminal escribir *rosrun turtlesim turtlesim node*. 
  - En la tercera terminal dirigirse al directorio que contiene el workspace de catkin y escribir source *devel/setup.bash*. Acto seguido escribir rosrun *hello_turtle myTeleopKey.py*. En este punto, la terminal ya deber ́ıa estar esperando el ingreso de teclas.
