#! python3
""""
#RPS006
Design a simulation of logic gates with python
Maroko Gideon (c) 2017
marokogideon@gmail.com
www.gmaroko.me
PS: No serious License

======================NOTES============================
Binary gates ==> Those with two input terminals named Pin A and Pin B.
Unary gates ==> Those with a single input terminal, named pinA
=======================================================
"""
class LogicGate:
    """
    Declares the name of the gate and returns the output from that gate
    """

    def __init__(self,name):
        self.name = name
        self.output = None

    def getName(self):
        return self.name

    def getOutput(self):
        self.output = self.gateLogic()
        return self.output


class BinaryGate(LogicGate):
    """
    Identifies the gates with two inputs and checks for input signals at these pins
    """
    def __init__(self,name):
        LogicGate.__init__(self,name)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(input("Signal input at pin A for gate "+self.getName()+": "))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return int(input("Signal input at pin B for gate "+self.getName()+"-->"))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self,signalSource):
        if self.pinA == None:
            self.pinA = signalSource
        else:
            if self.pinB == None:
                self.pinB = signalSource
            else:
                pass
                #Cannot connect: gate does not have an open terminal


class AndGate(BinaryGate):

    def __init__(self,name):
        BinaryGate.__init__(self,name)

    def gateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):

    def __init__(self,name):
        BinaryGate.__init__(self,name)

    def gateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a ==1 or b==1:
            return 1
        else:
            return 0

class UnaryGate(LogicGate):

    def __init__(self,name):
        LogicGate.__init__(self,name)

        self.pin = None

    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate "+self.getName()+"-->"))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")


class NotGate(UnaryGate):

    def __init__(self,name):
        UnaryGate.__init__(self,name)

    def gateLogic(self):
        if self.getPin():
            return 0
        else:
            return 1

class NandGate(BinaryGate):
    def __init__(self):
        BinaryGate.__init__(self, name)
    def gatelogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 0
        else:
            return 1

class NorGate(BinaryGate):
    def __int__(self):
        BinaryGate.__init__(self, name)

    def gateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 or b == 1:
            return 0
        else:
            return 1

class XorGate(BinaryGate):
    def  __int__(self):
        BinaryGate.__init__(self, name)

    def gateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b !=a or b == 1 and a !=b:
            return 1
        else:
            return 0

class Connect:
    """
    Models a circuit network by connecting various gates like it was a cable
    """

    def __init__(self, fromgate, togate):
        self.fromgate = fromgate
        self.togate = togate

        togate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate


def sampleDesign():
   g1 = AndGate("G1")
   g2 = AndGate("G2")
   g3 = OrGate("G3")
   g4 = NotGate("G4")
   Connect(g1,g3)
   Connect(g2,g3)
   Connect(g3,g4)
   print('Connecting AND(G1) gate to OR(G3) gate pin A', end='\n')
   print('Connecting AND(G2) gate to OR(G3) gate pin B', end='\n')
   print('Connecting OR(G3) gate to NOT(G4) gate, Measuring the output of the NOT gate!', end='\n')
   print('Signal measured at output of G4(NOT):', g4.getOutput())

"""
##Automatically models a logic circuit and measure the output values

def designCircuit():
    numGates = int(input('Number of gates: '))
    gates = [] #stores just the number of gates
    for num in range(numGates):
        gateName = str(i)
        gates.append(gateName)
    circuitGates = [] #stores the types of gate names as arguments for connect class
    for aGate in range(len(gates)):
        name = 'g'+str(gates[aGate])
        gate_type = input('Gate type: ')
        if gate_type.lower() == 'and':
            name = AndGate(gateName)
            circuitGates.append(name)
        elif gate_type.lower() == 'or':
            name = OrGate(gateName)
            circuitGates.append(name)
        elif gate_type.lower() == 'nand':
            name = NandGate(gateName)
            circuitGates.append(name)
        elif gate_type.lower() == 'not':
            name = NotGate(gateName)
            circuitGates.append(name)
        elif gate_type.lower() == 'nor':
            name = NorGate(gateName)
            circuitGates.append(name)
        elif gate_type.lower() == 'xor':
            name = XorGate(gateName)
            circuitGates.append(name)
        else:
            #cant understand the gate type
            pass
            
    
        #Although I need an iterator for this
        i = 0
        while i< len(circuitGates):
            Connect(circuitGates[i], circuitGates[i+1])
            print('Connecting %s to %s'%(circuitGates[i], circuitGates[i+1]))
            i+=1
        print('Signal measured at output of %s'%(name[(len(gates)-1)]), name[(len(gates)-1)].getOutput())
"""
def main():
    sampleDesign()

if __name__ == "__main__":
    main()


