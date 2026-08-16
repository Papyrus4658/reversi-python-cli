```mermaid
---
title: 7.プレイヤーの手番
---
flowchart TD
3((3))-->LoopInputStart[/プレイヤーの着手\]
LoopInputStart-->PlayerInput[/Y座標→X座標の順で入力/]
PlayerInput-->LoopInputEnd[\入力したマスは有効か/]
LoopInputEnd-->Back((呼出元に戻る))
````