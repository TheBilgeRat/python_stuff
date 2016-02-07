import unittest

import mock

from AlgorithmExercises.Circuits import LogicGate


class TestLogicGatePy(unittest.TestCase):
    def setUp(self):
        pass

    def testAndGate(self):
        gate = LogicGate.AndGate("g1")
        with mock.patch("builtins.input", side_effect=[1, 1]):
            self.assertEqual(gate.get_output(), 1)
        with mock.patch("builtins.input", side_effect=[1, 0]):
            self.assertEqual(gate.get_output(), 0)
        with mock.patch("builtins.input", side_effect=[0, 0]):
            self.assertEqual(gate.get_output(), 0)
        self.assertEqual(gate.get_label(), "g1")

    def testOrGate(self):
        gate = LogicGate.OrGate("g2")
        with mock.patch("builtins.input", side_effect=[1, 1]):
            self.assertEqual(gate.get_output(), 1)
        with mock.patch("builtins.input", side_effect=[1, 0]):
            self.assertEqual(gate.get_output(), 1)
        with mock.patch("builtins.input", side_effect=[0, 1]):
            self.assertEqual(gate.get_output(), 1)
        with mock.patch("builtins.input", side_effect=[0, 0]):
            self.assertEqual(gate.get_output(), 0)
        self.assertEqual(gate.get_label(), "g2")

    def testNotGate(self):
        gate = LogicGate.NotGate("g3")
        with mock.patch("builtins.input", return_value=1):
            self.assertEqual(gate.get_output(), 0)
        with mock.patch("builtins.input", return_value=0):
            self.assertEqual(gate.get_output(), 1)
        self.assertEqual(gate.get_label(), "g3")

    def testXOrGate(self):
        gate = LogicGate.XOrGate("g4")
        with mock.patch("builtins.input", side_effect=[1, 1]):
            self.assertEqual(gate.get_output(), 0)
        with mock.patch("builtins.input", side_effect=[1, 0]):
            self.assertEqual(gate.get_output(), 1)
        with mock.patch("builtins.input", side_effect=[0, 1]):
            self.assertEqual(gate.get_output(), 1)
        with mock.patch("builtins.input", side_effect=[0, 0]):
            self.assertEqual(gate.get_output(), 0)
        self.assertEqual(gate.get_label(), "g4")

    def testConnections(self):
        g1 = LogicGate.AndGate("g1")
        g2 = LogicGate.AndGate("g2")
        g3 = LogicGate.OrGate("g3")
        g4 = LogicGate.NotGate("g4")
        LogicGate.Connector(g1, g3)
        LogicGate.Connector(g2, g3)
        LogicGate.Connector(g3, g4)
        with mock.patch("builtins.input", side_effect=[0, 1, 1, 1]):
            self.assertEqual(g4.get_output(), 0)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
