# 飼い猫判定AIを作ってみる


## 概要

飼い猫を物体検出の最新モデル"YOLOv5"で学習させ、Webカメラで写したとき、  
リアルタイムでどっちのねこなのかを矩形＋名前付きで表示させる  

YOLOv5のデフォルトモデルを使用すると、うちの飼い猫は”cat”らしい。  
では、"cat"のどっち？（名前）の猫なのかを、学習させて、判定してみる  

## 参考資料

* 解析対象の、ねこ。かわいい。  

なつ  
![image](https://user-images.githubusercontent.com/26809782/115238974-3ba89f80-a159-11eb-906f-1825ef6deebf.png)

きゅう  
![image](https://user-images.githubusercontent.com/26809782/115239045-50853300-a159-11eb-98c2-bd1baaab7873.png)

## 開発環境・手順

1. 以下の記事を参考に、猫判定AIを作ってみる  
https://qiita.com/PoodleMaster/items/5f2cc3248c03b03821b8  

1. 学習モデルの構築は"Google Colab"を使用する  
https://colab.research.google.com/notebooks/welcome.ipynb?hl=ja#scrollTo=aKc7JTHQMi-r

1. macへの"Anaconda"へのインストールは以下参照  
https://www.python.jp/install/anaconda/macos/install.html

## Google Colabでの学習モデル構築

https://colab.research.google.com/drive/1giVyUA0oirvbcvUcVfHmpr-rrr4zuUcF?hl=ja#scrollTo=-qNmUztKMptW

```
!git clone https://github.com/ultralytics/yolov5
!pip install -r yolov5/requirements.txt
%cd /content/yolov5
!python train.py --img 640 480 --batch 20 --epochs 100 --data '/content/drive/My Drive/cat_analysis/cat.yaml' --name cat_analysis
```

+ epochs(エポック数)  
学習の回数



## 実行手順（デフォルトモデル）

```
conda activate yolov5
cd yolov5
python detect.py --source 0　// モデル指定なし、のちに、猫学習モデルを移植して、引数には学習モデルを指定する
```

## Google Colabのモデル構築ログ

<details><summary>Google Colabのモデル構築中のログ</summary><div>


```
/content/yolov5
github: up to date with https://github.com/ultralytics/yolov5 ✅
YOLOv5 🚀 v5.0-14-g238583b torch 1.8.1+cu101 CPU

Namespace(adam=False, artifact_alias='latest', batch_size=20, bbox_interval=-1, bucket='', cache_images=False, cfg='', data='/content/drive/My Drive/cat_analysis/cat.yaml', device='', entity=None, epochs=300, evolve=False, exist_ok=False, global_rank=-1, hyp='data/hyp.scratch.yaml', image_weights=False, img_size=[640, 480], label_smoothing=0.0, linear_lr=False, local_rank=-1, multi_scale=False, name='cat_analysis', noautoanchor=False, nosave=False, notest=False, project='runs/train', quad=False, rect=False, resume=False, save_dir='runs/train/cat_analysis', save_period=-1, single_cls=False, sync_bn=False, total_batch_size=20, upload_dataset=False, weights='yolov5s.pt', workers=8, world_size=1)
tensorboard: Start with 'tensorboard --logdir runs/train', view at http://localhost:6006/
2021-04-19 13:04:03.570492: I tensorflow/stream_executor/platform/default/dso_loader.cc:49] Successfully opened dynamic library libcudart.so.11.0
hyperparameters: lr0=0.01, lrf=0.2, momentum=0.937, weight_decay=0.0005, warmup_epochs=3.0, warmup_momentum=0.8, warmup_bias_lr=0.1, box=0.05, cls=0.5, cls_pw=1.0, obj=1.0, obj_pw=1.0, iou_t=0.2, anchor_t=4.0, fl_gamma=0.0, hsv_h=0.015, hsv_s=0.7, hsv_v=0.4, degrees=0.0, translate=0.1, scale=0.5, shear=0.0, perspective=0.0, flipud=0.0, fliplr=0.5, mosaic=1.0, mixup=0.0
wandb: Install Weights & Biases for YOLOv5 logging with 'pip install wandb' (recommended)
Downloading https://github.com/ultralytics/yolov5/releases/download/v5.0/yolov5s.pt to yolov5s.pt...
100% 14.1M/14.1M [00:00<00:00, 16.8MB/s]

Overriding model.yaml nc=80 with nc=2

                 from  n    params  module                                  arguments                     
  0                -1  1      3520  models.common.Focus                     [3, 32, 3]                    
  1                -1  1     18560  models.common.Conv                      [32, 64, 3, 2]                
  2                -1  1     18816  models.common.C3                        [64, 64, 1]                   
  3                -1  1     73984  models.common.Conv                      [64, 128, 3, 2]               
  4                -1  1    156928  models.common.C3                        [128, 128, 3]                 
  5                -1  1    295424  models.common.Conv                      [128, 256, 3, 2]              
  6                -1  1    625152  models.common.C3                        [256, 256, 3]                 
  7                -1  1   1180672  models.common.Conv                      [256, 512, 3, 2]              
  8                -1  1    656896  models.common.SPP                       [512, 512, [5, 9, 13]]        
  9                -1  1   1182720  models.common.C3                        [512, 512, 1, False]          
 10                -1  1    131584  models.common.Conv                      [512, 256, 1, 1]              
 11                -1  1         0  torch.nn.modules.upsampling.Upsample    [None, 2, 'nearest']          
 12           [-1, 6]  1         0  models.common.Concat                    [1]                           
 13                -1  1    361984  models.common.C3                        [512, 256, 1, False]          
 14                -1  1     33024  models.common.Conv                      [256, 128, 1, 1]              
 15                -1  1         0  torch.nn.modules.upsampling.Upsample    [None, 2, 'nearest']          
 16           [-1, 4]  1         0  models.common.Concat                    [1]                           
 17                -1  1     90880  models.common.C3                        [256, 128, 1, False]          
 18                -1  1    147712  models.common.Conv                      [128, 128, 3, 2]              
 19          [-1, 14]  1         0  models.common.Concat                    [1]                           
 20                -1  1    296448  models.common.C3                        [256, 256, 1, False]          
 21                -1  1    590336  models.common.Conv                      [256, 256, 3, 2]              
 22          [-1, 10]  1         0  models.common.Concat                    [1]                           
 23                -1  1   1182720  models.common.C3                        [512, 512, 1, False]          
 24      [17, 20, 23]  1     18879  models.yolo.Detect                      [2, [[10, 13, 16, 30, 33, 23], [30, 61, 62, 45, 59, 119], [116, 90, 156, 198, 373, 326]], [128, 256, 512]]
Model Summary: 283 layers, 7066239 parameters, 7066239 gradients, 16.4 GFLOPS

Transferred 356/362 items from yolov5s.pt
Scaled weight_decay = 0.00046875
Optimizer groups: 62 .bias, 62 conv.weight, 59 other
train: Scanning '/content/drive/My Drive/cat_analysis' images and labels... 66 found, 0 missing, 0 empty, 0 corrupted: 100% 66/66 [01:25<00:00,  1.29s/it]
train: New cache created: /content/drive/My Drive/cat_analysis.cache
val: Scanning '/content/drive/My Drive/cat_analysis.cache' images and labels... 66 found, 0 missing, 0 empty, 0 corrupted: 100% 66/66 [00:00<00:00, 352642.12it/s]
Plotting labels... 

autoanchor: Analyzing anchors... anchors/target = 3.16, Best Possible Recall (BPR) = 1.0000
Image sizes 640 train, 480 test
Using 2 dataloader workers
Logging results to runs/train/cat_analysis
Starting training for 300 epochs...

     Epoch   gpu_mem       box       obj       cls     total    labels  img_size
     0/299        0G    0.1031   0.03668   0.02818    0.1679        16       640: 100% 4/4 [03:03<00:00, 45.95s/it]
               Class      Images      Labels           P           R      mAP@.5  mAP@.5:.95: 100% 2/2 [00:26<00:00, 13.33s/it]
                 all          66          73      0.0125       0.249      0.0115     0.00203

     Epoch   gpu_mem       box       obj       cls     total    labels  img_size
     1/299        0G    0.1024   0.03579   0.02888    0.1671        15       640: 100% 4/4 [02:00<00:00, 30.06s/it]
               Class      Images      Labels           P           R      mAP@.5  mAP@.5:.95: 100% 2/2 [00:25<00:00, 12.57s/it]
                 all          66          73      0.0157       0.198      0.0129     0.00214

     Epoch   gpu_mem       box       obj       cls     total    labels  img_size
     2/299        0G   0.09936   0.03617   0.02793    0.1635        21       640: 100% 4/4 [02:00<00:00, 30.03s/it]
               Class      Images      Labels           P           R      mAP@.5  mAP@.5:.95: 100% 2/2 [00:24<00:00, 12.07s/it]
                 all          66          73      0.0279      0.0814      0.0159     0.00308

     Epoch   gpu_mem       box       obj       cls     total    labels  img_size
     3/299        0G   0.09436   0.03262   0.02866    0.1556        13       640: 100% 4/4 [02:00<00:00, 30.05s/it]
               Class      Images      Labels           P           R      mAP@.5  mAP@.5:.95: 100% 2/2 [00:23<00:00, 11.62s/it]
                 all          66          73      0.0308      0.0814      0.0162     0.00277

     Epoch   gpu_mem       box       obj       cls     total    labels  img_size
     4/299        0G   0.09435    0.0322   0.02749     0.154        14       640: 100% 4/4 [02:06<00:00, 31.60s/it]
               Class      Images      Labels           P           R      mAP@.5  mAP@.5:.95: 100% 2/2 [00:22<00:00, 11.28s/it]
                 all          66          73      0.0375      0.0698      0.0175      0.0025

     Epoch   gpu_mem       box       obj       cls     total    labels  img_size
     5/299        0G   0.09613   0.03306   0.03058    0.1598        15       640: 100% 4/4 [02:00<00:00, 30.04s/it]
               Class      Images      Labels           P           R      mAP@.5  mAP@.5:.95:   0% 0/2 [00:00<?, ?it/s]

```　

</div></details>    

  
```
  
# 学習させた学習モデルで解析してみる
  
TOD


# ラズベリーパイにberryconda install

- ラズベリーパイ向けに作成されたconda

$  wget https://github.com/jjhelmus/berryconda/releases/download/v2.0.0/Berryconda3-2.0.0-Linux-armv6l.sh

$ chmod +x Berryconda3-2.0.0-Linux-armv7l.sh

$ ./Berryconda3-2.0.0-Linux-armv7l.sh

$ source ./.bashrc

$ conda update --all

# condaでYolov5動作確認

c:\>conda create -n yolov5 python=3.8
c:\>conda activate yolov5
(yolov5) c:\>git clone https://github.com/ultralytics/yolov5.git
(yolov5) c:\>cd yolov5
(yolov5) c:\yolov5>conda install pytorch torchvision -c pytorch 
(yolov5) c:\yolov5>pip install -U -r requirements.txt
(yolov5) c:\yolov5>python detect.py --source 0　// カメラ起動できたら、OK


