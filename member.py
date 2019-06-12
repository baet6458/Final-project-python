class member:
    def __init__(self,bondNumber,name,email,phoneNumber,machine):
        self.bondNumber=bondNumber
        self.name=name
        self.email=email
        self.phoneNumber=phoneNumber
        self.machine=machine
        self.time =0
        self.notificationSent=False;

    def getBondNumber():
        return bondNumber

    def getName():
        return name

    def getMachine():
        return machine

    def getTime():
        return time

    def setMachine(self,machine):
        self.machine=machine

    def setTime(self,time):
        self.time=time

    def sentNotification():
        notificationSent= not notificationSent

    def messageInfo(self):
        return str(self.bondNumber)+','+self.name+',' +self.email+','+str(self.machine)+','+self.phoneNumber
        
    def printInfo(self):
        print(str(self.bondNumber)+' , '+self.name+' , ' +self.email+' , '+str(self.machine)+' ,'+str(self.time))

 
