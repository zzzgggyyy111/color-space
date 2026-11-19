# 色彩空间：sRGB、XYZ 与亮度

颜色在不同空间转换后偏色、暗部发灰：sRGB 没有分段线性，XYZ 矩阵系数错，逆矩阵没对齐，亮度用 gamma 值而不是线性值，负数没有钳制，空输入崩，批量转换只成功一半。

## 目录结构

```
README.md
conftest.py
.gitignore
color/__init__.py
color/space.py
tests/test_space.py
```

## 当前状态

`color/space.py` 中所有函数只保留签名与文档字符串，函数体统一
`raise NotImplementedError`。`tests/test_space.py` 有 15 个参数化用例，
初始全部失败。

## 需要修复的 10 个问题

1. sRGB 分段线性
2. XYZ 矩阵系数
3. 逆矩阵对齐
4. 亮度用线性值
5. 负数钳制
6. 空输入兜底

## 验收

```bash
python -m pytest -q
```

初始应得到 `15 failed`，且没有 collection error。实现 `color/space.py`
后 15 条用例应全部通过。
