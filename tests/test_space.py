import pytest

from color import space as mod

CASES = [
    ('srgb_to_linear', [0.5], 0.21404114048223255, True),
    ('srgb_to_linear', [0.0], 0.0, True),
    ('linear_to_srgb', [0.5], 0.7353569830524495, True),
    ('linear_to_srgb', [0.001], 0.012920000000000001, True),
    ('rgb_to_xyz', [[1, 1, 1]], [0.9505, 1.0, 1.089], True),
    ('xyz_to_rgb', [[0.95, 1.0, 1.09]], [0.9978960000000001, 1.00058, 1.0010450000000002], True),
    ('luminance', [[1, 1, 1]], 1.0, True),
    ('luminance', [[0, 1, 0]], 0.7152, True),
    ('srgb_to_linear', [1.0], 1.0, True),
    ('linear_to_srgb', [0.0], 0.0, True),
    ('rgb_to_xyz', [[0, 0, 0]], [0.0, 0.0, 0.0], True),
    ('xyz_to_rgb', [[0, 0, 0]], [0.0, 0.0, 0.0], True),
    ('luminance', [[1, 0, 0]], 0.2126, True),
    ('luminance', [[0, 0, 1]], 0.0722, True),
    ('linear_to_srgb', [1.0], 0.9999999999999999, True),
]


@pytest.mark.parametrize("func_name,args,expected,approx", CASES)
def test_space_contract(func_name, args, expected, approx):
    func = getattr(mod, func_name)
    result = func(*args)
    if approx:
        assert result == pytest.approx(expected)
    else:
        assert result == expected
