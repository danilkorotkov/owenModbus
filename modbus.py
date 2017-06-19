import minimalmodbus
minimalmodbus.CLOSE_PORT_AFTER_EACH_CALL = True
#print minimalmodbus._getDiagnosticString()
import serial
import serial.rs485

instrument = minimalmodbus.Instrument('/dev/ttyUSB0',slaveaddress=16) # port name, slave address (in decimal)
instrument.debug = True
#instrument.close_port_after_each_call=0
instrument.mode = 'rtu' # rtu or ascii mode
instrument.serial.baudrate = 57600 # Baud
#instrument.serial.rs485.RS485()
#instrument.serial.rs485_mode = serial.rs485.RS485Settings(delay_before_rx=0.00)
temperature=0
#instrument.serial.rs485_mode = serial.rs485.RS485Settings()
print instrument
#print instrument.get_all_pattern_variables(0)
#instrument.serial.setRTS(1)
print instrument.serial.rts
try:
    temperature = instrument.read_register(1, functioncode=3, signed=True, numberOfDecimals=1) # Registernumber, number of decimals
except IOError:
    pass
print instrument.serial.rts
print ('t= ', temperature)