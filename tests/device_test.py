import usb
busses = usb.busses()
for bus in busses:
    devices = bus.devices
    for dev in devices:
        handle = dev.open()
        print("Device:", dev.filename)
        print("  VID: 0x{:04x}".format(dev.idVendor))
        print("  PID: 0x{:04x}".format(dev.idProduct))
        print("  Manufacturer: 0x{:x}".format(dev.iManufacturer), end='')