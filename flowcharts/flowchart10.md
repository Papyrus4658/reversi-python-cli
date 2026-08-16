```mermaid
---
title: 10.周辺のマスを確認
---
flowchart TD
5or9((5or9))-->LoopYCoeStart[/Y座標の係数\]
LoopYCoeStart-->YMove[Y座標を移動]
YMove-->LoopXCoeStart[/X座標の係数\]
LoopXCoeStart-->XMove[X座標を移動]
XMove-->CoordinateStatus{現在のマスは相手のマスか}
CoordinateStatus-->|True|11((11.奥のマスを確認))
11-->LoopXCoeEnd[\-1<=Xの係数<=1/]
LoopXCoeEnd-->LoopYCoeEnd[\-1<=Yの係数<=1/]
LoopYCoeEnd-->Back((呼出元に戻る))
````