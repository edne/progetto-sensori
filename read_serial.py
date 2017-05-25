from serial import Serial

# Su Windows sostituire /dev/ttyACM3 con COM-qualcosa
# TODO: leggere da un file di configurazione
with Serial("/dev/ttyACM3", 9600) as port:
    while True:
        data = port.read(1)
        value = ord(data)
        print(value)
