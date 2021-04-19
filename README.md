# 飼い猫判定AIを作ってみる


## 概要

飼い猫を物体検出の最新モデル"YOLOv5"で学習させ、Webカメラで写したとき、  
リアルタイムでどっちのねこなのかを矩形＋名前付きで表示させる  

## 参考資料

* 解析対象の、ねこ  

なつ  
![image](https://user-images.githubusercontent.com/26809782/115238974-3ba89f80-a159-11eb-906f-1825ef6deebf.png)

きゅう  
![image](https://user-images.githubusercontent.com/26809782/115239045-50853300-a159-11eb-98c2-bd1baaab7873.png)

## 開発環境・手順

1. 以下の記事を参考に、猫判定AIを作ってみる  
https://qiita.com/PoodleMaster/items/5f2cc3248c03b03821b8  

1. 学習モデルの構築は"Google Colab"を使用する  
https://colab.research.google.com/notebooks/welcome.ipynb?hl=ja#scrollTo=aKc7JTHQMi-r
