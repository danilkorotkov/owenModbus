import minimalmodbus, time
minimalmodbus.CLOSE_PORT_AFTER_EACH_CALL = True
#print minimalmodbus._getDiagnosticString()
import serial
import serial.rs485

def signme(me):
    if me < 0x8000:
        return float(me)
    else:
        me = me - 0x10000
        return float(me)

instrument = minimalmodbus.Instrument('/dev/ttyUSB0',slaveaddress=16, mode='rtu') # port name, slave address (in decimal)
instrument.debug = True
instrument.serial.baudrate = 57600
temperature=0
error=0
print instrument

counter = 0
while True:
    try:
        temperature = instrument.read_register(1, functioncode=3, signed=True, numberOfDecimals=1) # Registernumber, number of decimals
        t2 = instrument.read_registers(1+6*5, numberOfRegisters = 2)
        t3 = instrument.read_registers(1 + 6 * 2, numberOfRegisters=2)
    except IOError:
        error += 1
    print 'error', error
    counter += 1
    print 'counter', counter
    print 't= ', temperature
    print 't2= ', signme(t2[0])/10, t2[1]
    print 't3= ', signme(t3[0])/10, t3[1]
    time.sleep(1)

