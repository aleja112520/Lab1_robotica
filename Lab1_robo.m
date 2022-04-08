rosinit %Conexión con el nodo maestro
%%  
velPub = rospublisher('/turtle1/cmd_vel','geometry_msgs/Twist'); %Crear Publicador
velMsg = rosmessage(velPub); %Creación del mensaje
%%
velMsg.Linear.X=-1; %Asignar mensaje
velMsg.Angular.Z=1;
send(velPub,velMsg); %Enviar mensaje
pause(1)
%%
suscrip = rossubscriber('/turtle1/pose','turtlesim/Pose');
%%
suscrip.LatestMessage  
%%
Posecli = rossvcclient('/turtle1/teleport_absolute');
poseMsg= rosmessage(Posecli);
%%
poseMsg.X = 5;
poseMsg.Y= 3;
poseMsg.Theta = 1.5;
call(Posecli,poseMsg);
pause(1)
%%
Poserosshutdown
