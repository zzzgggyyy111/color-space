"""色彩空间：sRGB、XYZ 与亮度：待实现的核心模块。"""


def srgb_to_linear(value):
    """sRGB 转线性。"""
    raise NotImplementedError

def linear_to_srgb(value):
    """线性转 sRGB。"""
    raise NotImplementedError

def rgb_to_xyz(rgb):
    """RGB 转 XYZ。"""
    raise NotImplementedError

def xyz_to_rgb(xyz):
    """XYZ 转 RGB。"""
    raise NotImplementedError

def luminance(rgb):
    """亮度。"""
    raise NotImplementedError
