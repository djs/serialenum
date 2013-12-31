from glob import glob
import os
import os.path
from serial import Serial
import sys


def enumerate():
    ports = []

    if sys.platform == 'win32':
        # Iterate through registry because WMI does not show virtual serial ports
        import _winreg

        try:
            key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, r'HARDWARE\DEVICEMAP\SERIALCOMM')
        except WindowsError:
            return []
        i = 0
        while True:
            try:
                ports.append(_winreg.EnumValue(key, i)[1])
                i = i + 1
            except WindowsError:
                break
    elif sys.platform == 'linux2':
        if os.path.exists('/dev/serial/by-id'):
            entries = os.listdir('/dev/serial/by-id')
            dirs = [os.readlink(os.path.join('/dev/serial/by-id', x))
                    for x in entries]
            ports.extend([os.path.normpath(os.path.join('/dev/serial/by-id', x))
                         for x in dirs])

        for dev in glob('/dev/ttyS*'):
            try:
                port = Serial(dev)
            except:
                pass
            else:
                ports.append(dev)

    else:
        return []

    return ports

def script():
    for port in enumerate():
        print port

if __name__ == "__main__":
    script()
