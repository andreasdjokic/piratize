from piratize_translate import *
import unittest

class MyTest(unittest.TestCase):
    def test(self):
        test_list_1 = ["Hello my friend", "Where is the treasure"]
        test_list_1_result = ["Ahoy me bucko", "Whar be th' "]
        test_list_2 = [2.5, 0.3]
        test_list_2_result = [Fraction(5,2), Fraction(1,4)]
        self.assertEqual(translate_to_pirish("Hello my friend"), "Ahoy me bucko")
        self.assertEqual(translate_to_pirish("Where is the treasure"), "Whar be th' ")
        self.assertEqual(float_to_rational(2.5), Fraction(5, 2))
        self.assertEqual(float_to_rational(0.3), Fraction(1, 4))
        self.assertEqual(process_array(test_list_1), test_list_1_result)
        self.assertEqual(process_array(test_list_2), test_list_2_result)
        
if __name__ == '__main__':
    unittest.main()