import datetime

class TE16():
    """Blueprint of a TE16 Node"""
    def __init__(self, model, serial, calDate, FWver, MacAddr, IPaddr):
        self.model = model
        self.serial = serial
        self.calDate = calDate
        self.FWver = FWver
        self.MacAddr = MacAddr
        self.IPaddr = IPaddr

    def getSerial(self):
        print(self.serial)

current_time = datetime.datetime.now()
TE160156 = TE16("TE16-0156", "12345", "10/16/22", '1.4', "00:1B:46:0B:92", "192.168.10.36")
TE160156.calDate = current_time
print(TE160156.calDate)


