```mermaid
---
title: 11.奥のマスを確認
---
flowchart TD
10((10))-->YMove[Y座標を更に移動]
YMove-->XMove[X座標を更に移動]
XMove-->LoopCoordinateStart[/現在のマス\]
LoopCoordinateStart-->CoordinateCurrent{現在のマスは現在の手番の石か}
CoordinateCurrent-->|True|CheckCaller{"5or(7or8)"}
CheckCaller-->|5|AddValid[元のマスを有効マスに追加]
AddValid-->LoopCoordinateEnd[\現在のマスは相手のマスか/]
CheckCaller-->|7or8|12((12.石の反転))
12-->LoopCoordinateEnd
LoopCoordinateEnd-->Back((呼出元に戻る))
CoordinateCurrent-->|False|YMoveMore[Y座標を更に移動]
YMoveMore-->XMoveMore[X座標を更に移動]
XMoveMore-->LoopCoordinateEnd
````