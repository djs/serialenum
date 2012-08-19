import sys
import glob


def enumerate():
    ports = []

    if sys.platform == 'win32':
        # Iterate through registry because WMI does not show virtual serial ports
        import _winreg

        key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, r'HARDWARE\DEVICEMAP\SERIALCOMM')
        i = 0
        while True:
            try:
                ports.append(_winreg.EnumValue(key, i)[1])
                i = i + 1
            except WindowsError:
                break
    elif sys.platform == 'linux2':
        ports = glob.glob('/dev/ttyUSB*')
        ports = ports + glob.glob('/dev/ttyS*')

    return ports
