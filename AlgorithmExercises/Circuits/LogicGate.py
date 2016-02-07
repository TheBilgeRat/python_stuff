class LogicGate:
    """
    Virtual Class for a series of logic gates.  Do not instansiate.
    """

    def __init__(self, label):
        self.label = label
        self.output = None

    def get_label(self):
        """
        label of gate
        :return: label
        """
        return self.label

    def get_output(self):
        """
        def performGateLogic must be implemented by any inheriting class
        :return: output gate
        """
        self.output = self.perform_gate_logic()
        return self.output


class BinaryGate(LogicGate):
    """
    Virtual class for gate type wth two input pins.
    Do not instantiate this class
    """
    def __init__(self, label):
        LogicGate.__init__(self, label)

        self.pinA = None
        self.pinB = None

    def get_pin_A(self):
        if self.pinA is None:
            return input("Enter Pin A input for gate "+ self.get_label()
                         + "--->")
        else:
            return self.pinA.get_from().get_output()

    def get_pin_B(self):
        if self.pinB is None:
            return input("Enter Pin B input for gate " + self.get_label()
                         + "--->")
        else:
            return self.pinB.get_from().get_output()

    def set_next_pin(self, source):
        if self.pinA is None:
            self.pinA = source
        elif self.pinB is None:
            self.pinB = source
        else:
            print("Cannot connect: NO EMPTY PINS")


class UnaryGate(LogicGate):
    """
    Virtual class for gate with a single input pin.
    Do not instantiate this class.
    """
    def __init__(self, label):
        LogicGate.__init__(self, label)
        self.pin = None

    def get_pin(self):
        if self.pin is None:
            return input("Enter Pin input for gate " + self.get_label()
                         + "--->")
        else:
            return self.pin.get_from().get_output()

    def set_next_pin(self, source):
        if self.pin is None:
            self.pin = source
        else:
            print("Cannot connect: NO EMPTY PINS")


class AndGate(BinaryGate):
    """
    And gate representation
    """
    def __init__(self, label):
        BinaryGate.__init__(self, label)

    def perform_gate_logic(self):
        gateA = self.get_pin_A()
        gateB = self.get_pin_B()

        if gateA == 1 and gateB == 1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):
    """
    Or Gate representation
    """
    def __init__(self, label):
        BinaryGate.__init__(self, label)

    def perform_gate_logic(self):
        gateA = self.get_pin_A()
        gateB = self.get_pin_B()

        if gateA == 1 or gateB == 1:
            return 1
        else:
            return 0


class XOrGate(BinaryGate):
    """
    XOR gate representation
    """
    def __init__(self, label):
        BinaryGate.__init__(self, label)

    def perform_gate_logic(self):
        gateA = self.get_pin_A()
        gateB = self.get_pin_B()

        if gateA == 1 and gateB == 0 or gateA == 0 and gateB == 1:
            return 1
        else:
            return 0


class NotGate(UnaryGate):
    """
    Not gate representation
    """
    def __init__(self, label):
        UnaryGate.__init__(self, label)

    def perform_gate_logic(self):
        if self.get_pin():
            return 0
        else:
            return 1


class Connector:
    """
    class which connects two logic gates together.
    """
    def __init__(self, fromGate, toGate):
        self.fromgate = fromGate
        self.togate = toGate

        toGate.set_next_pin(self)

    def get_from(self):
        return self.fromgate

    def get_to(self):
        return self.togate
