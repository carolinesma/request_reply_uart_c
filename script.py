import serial

while True: #Loop para a conexão com o Arduino
    try:  #Tenta se conectar, se conseguir, o loop se encerra
        ser = serial.Serial('/dev/ttyUSB0', 9600, 8, 'N', 1)    
        break
    except:
        pass
        print('Não foi possível conectar')
while ser.is_open: #Loop enquanto a conexão está aberta
    msg = ser.read(1) #Recebe Syn
    mgs = int.from_bytes(msg, 'little')
    
    if (msg == 10): #Envia Ack-Syn
      print('Solicitando reoconhecimento de conexão do Arduino...')
      ser.write(chr(20).encode())
      msg = ser.read(1)
      mgs = int.from_bytes(msg, 'little')

    if (msg == 30): #Recebe Ack
      print("Arduino reconheceu a conexão.")
      ser.flush() #Limpa a comunicação
      print("Finalizando conexão e script...")
      ser.close()     
        
