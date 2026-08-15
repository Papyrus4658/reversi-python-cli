```mermaid
---
title: 1.全体の流れ
---
flowchart TD
Start(開始)-->BorW((2.先後選択))
BorW-->Play((3.対局))
Play-->Result((4.勝敗判定))
Result-->End(終了)
```