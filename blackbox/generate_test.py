import itertools
import random

from compare_pow import compare_pow
from compare_pow_unittest import generate_expected_output

MAX = 100
x_subsets = {
    "ne": (-MAX, -2+1, 2),
    "no": (-MAX+1, -5+1, 2),
    "pe": (2, MAX+1, 2),
    "po": (5, MAX, 2),
    "0" : (0, 0+1, 1),
    "m1": (-1, -1+1, 1),
    "p1": (+1, +1+1, 1),
    "m3": (-3, -3+1, 1),
    "p3": (+3, +3+1, 1)
}
xy_set = [
    (2, 4), (1, 1), (0, 0), (0, -1), (-1, 0), (0, 2), (2, 0),
    (-5, 2), (-3, 5), (2, -5), (3, -3),
    (1, 4), (4, 1), (3, 4), (4, 3), (4, 5), (5, 4),
    (-5, -4), (-4, -5), (-6, -4), (-4, -6), (-1, -5), (-5, -1), (-3, -5), (-5, -3), (-7, -5), (-5, -7), 
]
x_subset_name = list(x_subsets.keys())
test_id = 0
"""
for u_name, v_name in itertools.product(x_subset_name, x_subset_name):
    test_id += 1
    u = random.randrange(*x_subsets[u_name])
    v = random.randrange(*x_subsets[v_name])
    exp_output = generate_expected_output(u, v)
    usr_output = compare_pow(u, v)
    verdict = "Passed" if exp_output == usr_output else "Not passed"
    print(f"R{test_id} & ({u}, {v}) & {exp_output} & {usr_output} & {verdict} & $x \\in X_{{{u_name}}},\\ y \\in Y_{{{v_name}}}$ \\\\ \\hline")
"""
for u, v in xy_set:
    exp_output = generate_expected_output(u, v)
    usr_output = compare_pow(u, v)
    verdict = "Passed" if exp_output == usr_output else "Not passed"
    print(f"R{test_id} & ({u}, {v}) & {exp_output} & {usr_output} & {verdict} \\\\ \\hline")
    test_id += 1
