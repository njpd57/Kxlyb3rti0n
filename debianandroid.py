import os
print('')
print('*************************************************')
print('Linux en Android por Nicolas para el mundo -2018-')
print('********************Python-3*********************')
print('')
print ("Saludos,para instalar y ejecutar LXDE Sigue estos pasos C:")
print('')
print('Que deseas hacer??')
print('')
print('-A = Instalar Componentes')
print('-B = Instalar LXDE')
print('-C = Ejecutar LXDE')
print('-D = Actualizar Debian')
print('-E = Instrucciones')
print('')
a=input("Selecciona una opcion: ")
if a=="A":
 os.system('apt-get install xterm pulseaudio synaptic')
 print('Listo!!')
if a=="B":
 os.system('apt-get install lxde')
 print('Listo, ya puedes ejecutar LXDE En XSERVER')
if a=="C":
 os.system('export DISPLAY=0 PULSE_SERVER=:127.0.0.1:4712')
 os.system('startlxde')
 print('Ahora inicia Xserver XDSL')
if a=="D":
 os.system('apt-get update && apt-get upgrade')
 print('Listo!!')
if a=="E":
 print('Saludos,es necesario tener instaladas las aplicaciones GNURoot Debian')
 print('y Xserver XSDL, ejecutar este script desde GNURoot Debian')
 print('Actualizar Debian,instalar los componentes luego instalar LXDE')
 print('Por ultimo Iniciar LXDE, luego abrir la aplicacion Xserver')
 print('y esta todo LISTO!!!')
else:
 print('Opcion invalida')

print('*************')
print('*KXLYB3RTI0N*')
print('*************')
