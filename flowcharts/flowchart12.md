```mermaid
---
title: 12.石の反転
---
flowchart TD
11((11))-->YBack[Y座標を元に近づける]
YBack-->XBack[X座標を元に近づける]
XBack-->LoopCoordinate[/現在のマス\]
LoopCoordinate-->Reverse[現在のマスの石を反転]
Reverse-->YBackMore[Y座標を元に近づける]
YBackMore-->XBackMore[X座標を元に近づける]
XBackMore-->LoopCoordinateEnd[\現在のマスは相手のマスか/]
LoopCoordinateEnd-->Back((呼出元に戻る))
````