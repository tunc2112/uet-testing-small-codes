from simple_date import is_valid_day
import unittest


class WhiteBoxTest(unittest.TestCase):
    def test_c2(self):
        testcases = [
            (('11', '11', '2011'), False),
            (('11', '11', 2011), False),
            (('11', 11, 2011), False),
            ((10, 10, 2010), True),
            ((11, 11, 2011), True),
            ((29, 2, 2020), True),
            ((29, 2, 2021), False)
        ]
        for k, (sys_input, exp_output) in enumerate(testcases):
            with self.subTest(msg='test_%d: %r' % (k, sys_input)):
                self.assertEqual(is_valid_day(*sys_input), exp_output)


if __name__ == '__main__':
    unittest.main()
