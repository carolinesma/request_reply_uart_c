import serial

while True: #Loop para a conexão com o Arduino
    try:  #Tenta se conectar, se conseguir, o loop se encerra
        ser = serial.Serial('/dev/ttyUSB0', 9600)    
        break
    except:
        pass
        print('Não foi possível conectar')
while ser.is_open: #Loop enquanto a conexão está aberta
    print('Enviando mensagem para o arduino...')
    ser.write(chr(10).encode())

    print('Aguardando confirmação...')
    msg = ser.read(3).decode("ascii","ignore")

    if chr(20) in msg:
      print("Arduino confirmou a conexão.")
      ser.write(chr(30).encode())
      ser.flush() #Limpa a comunicação
      print("Finalizando conexão e script...")
      ser.close()
