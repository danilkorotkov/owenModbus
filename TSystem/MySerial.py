# -*- coding: utf8 -*-
import serial, serial.rs485
import time

#класс последовательного порта с логированием данных
class ComPort(serial.rs485.RS485):
    def __init__(self, port=None, baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=None, xonxoff=0, \
                 rtscts=0, writeTimeout=0.02, dsrdtr=None):
        serial.rs485.RS485.__init__(self, port, baudrate, bytesize, parity, stopbits, timeout, xonxoff, rtscts, \
                                   writeTimeout, dsrdtr)                        
        self.LoggingIsOn=False;
                
    def log(self, buffer, obj_name=None, action=None):
        if self.LoggingIsOn:            
            log_file = open('ComLog.txt','a')
            tm = time.ctime(time.time())
            timeStr='Time: {}\n'.format(tm)
            #ObjectStr='Object: {}\n'.format(obj_name)        
            ObjectStr=''
            str2log=''
            if len(buffer)>0:
                for char in buffer:
                    str2log=str2log+'{0:#x}({0}) '.format(ord(char))
                dataStr='Data {}: {}\n\n'.format(action,str2log)
            else:
                dataStr='Data when {} is empty\n\n'.format(action)        
            log_file.write('{} {} {}'.format(timeStr,ObjectStr,dataStr))
            log_file.close()
        
    def write(self, buffer, obj_name=None):
        if self.isOpen():
            #serial.rs485.RS485.flush()
            serial.rs485.RS485.write(self,buffer)
            #serial.rs485.RS485.flush()
            self.log(buffer, obj_name, 'writing')
            return (True,'')
        else:
            self.log(buffer,obj_name,'writing::error:port_not_open')                
            raise Exception('ComPort::writing:port is not open!')                
        
    def read(self, size, obj_name=None):
        if self.isOpen():
            buffer = serial.rs485.RS485.read(self,size)
            self.log(buffer, obj_name, 'reading')
            return (True,buffer)
        else:
            self.log(buffer, obj_name, 'reading::error:port_not_open')                        
            raise Exception('ComPort::reading:port is not open!')
    
    def test(self):
        raise Exception('Test not implemented!')
   