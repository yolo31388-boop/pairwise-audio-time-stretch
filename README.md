# pairwise-audio-time-stretch

## 领域

游戏、图形与多媒体

## 主题

音频时间伸缩

## 说明

相位连续、窗长联动与块边界淡化。

初始状态下 `media/audio_time_stretch.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
