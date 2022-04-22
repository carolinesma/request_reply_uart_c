import serial

while True: #Loop para a conexão com o Arduino
    try:  #Tenta se conectar, se conseguir, o loop se encerra
        ser = serial.Serial('/dev/ttyUSB0', 9600)    
        break
    except:
        pass
        print('Não foi possível conectar')
while ser.is_open: #Loop enquanto a conexão está aberta
    msg = ser.read(3).decode("ascii","ignore") #Recebe Syn
    if chr(10) in msg: #Envia Ack-Syn
      print('Solicitando reoconhecimento de conexão do Arduino...')
      ser.write(chr(20).encode())
      msg = ser.read(3).decode("ascii","ignore")

    if chr(30) in msg: #Recebe Ack
      print("Arduino reconheceu a conexão.")
      ser.flush() #Limpa a comunicação
      print("Finalizando conexão e script...")
      ser.close()close()
