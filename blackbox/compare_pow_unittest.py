from compare_pow import compare_pow
import unittest


def generate_expected_output(x, y):
    if x <= 0 == y or x == 0 >= y:
        return None

    u = x**y
    v = y**x
    return "<" if u < v else ">" if u > v else "="


class TestComparePow(unittest.TestCase):
    def test_small_input(self):
        max_xy = 8
        xy_set = [(x, y) for x in range(-max_xy, max_xy+1) for y in range(-max_xy, max_xy+1)]
        for k, xy in enumerate(xy_set):
            exp_output = generate_expected_output(*xy)
            with self.subTest(msg='test_%d: %r' % (k, xy)):
                self.assertEqual(compare_pow(*xy), exp_output)

    def test_large_input(self):
        xy_set = [
            ((876543, 372647), "<"),
            ((987654321, 123456987), "<"),
            ((1000000000, 999999999), "<"),
            ((1000000000, 2), "<"),
            ((1000000000, 1), ">"),
            ((987654321, 123456789), "<"),
            ((1000000000, 1000000000), "="),
            ((4359435, 4396510), ">"),
            ((25936809, 25936809), "="),
            ((53602896, 3), "<"),
            ((13208659, 1), ">"),
            ((620537015, 620537016), ">"),
            ((56498103, 56498102), "<"),
            ((4, 1000000000), ">"),
            ((10000035, 1000432), "<"),
            ((15657413, 15657414), ">")
        ]
        for k, (xy, exp_output) in enumerate(xy_set):
            with self.subTest(msg='test_%d: %r' % (k, xy)):
                self.assertEqual(compare_pow(*xy), exp_output)

    def test_xy_subsets(self):
        xy_set = [
            (-74, -70), (-70, -35), (-34, 66), (-38, 97), (-16, 0), (-12, -1), (-28, 1), (-60, -3), (-56, 3),
            (-65, -84), (-25, -9), (-55, 98), (-31, 5), (-43, 0), (-69, -1), (-31, 1), (-87, -3), (-47, 3),
            (18, -26), (78, -33), (14, 50), (68, 77), (24, 0), (100, -1), (92, 1), (84, -3), (40, 3),
            (57, -26), (5, -67), (37, 72), (11, 13), (47, 0), (29, -1), (65, 1), (45, -3), (59, 3),
            (0, -40), (0, -63), (0, 22), (0, 75), (0, 0), (0, -1), (0, 1), (0, -3), (0, 3),
            (-1, -20), (-1, -51), (-1, 82), (-1, 99), (-1, 0), (-1, -1), (-1, 1), (-1, -3), (-1, 3),
            (1, -58), (1, -7), (1, 96), (1, 71), (1, 0), (1, -1), (1, 1), (1, -3), (1, 3),
            (-3, -86), (-3, -5), (-3, 78), (-3, 73), (-3, 0), (-3, -1), (-3, 1), (-3, -3), (-3, 3),
            (3, -54), (3, -7), (3, 58), (3, 97), (3, 0), (3, -1), (3, 1), (3, -3), (3, 3)
        ]
        for k, xy in enumerate(xy_set):
            exp_output = generate_expected_output(*xy)
            with self.subTest(msg='test_%d: %r' % (k, xy)):
                self.assertEqual(compare_pow(*xy), exp_output)

    def test_condition_table(self):
        xy_set = [
            (2, 4), (1, 1), (0, 0), (0, -1), (-1, 0), (0, 2), (2, 0),
            (-5, 2), (-3, 5), (2, -5), (3, -3),
            (1, 4), (4, 1), (3, 4), (4, 3), (4, 5), (5, 4),
            (-5, -4), (-4, -5), (-6, -4), (-4, -6), (-1, -5), (-5, -1), (-3, -5), (-5, -3), (-7, -5), (-5, -7),
        ]
        for k, xy in enumerate(xy_set):
            exp_output = generate_expected_output(*xy)
            with self.subTest(msg='test_%d: %r' % (k, xy)):
                self.assertEqual(compare_pow(*xy), exp_output)


if __name__ == '__main__':
    unittest.main()
