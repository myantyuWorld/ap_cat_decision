# 概要

TBD

# CentOS初期設定　→　Yolov5動かすまで

## VirtualBoxでCentOSインストール

VirtualBoxへのインストール、Windows端末からTeraTermで接続するまでの手順は  
以下を参考にしました。  

 - [VirtualBoxへのCentOS8 install](https://qiita.com/yasushi-jp/items/01b4829a36272954719f)
 - [SSH接続](https://chibashi.me/development/centos8-ssh-2004/)

## Anaconda install

以下を参考にインストールしました。

- https://mebee.info/2020/11/07/post-22363/

動作確認

```
conda info
```

## Yolov5インストール

- git https://github.com/ultralytics/yolov5

## Yolov5動作確認

```
$ python detect.py --source 0  # webcam
                            file.jpg  # image 
                            file.mp4  # video
                            path/  # directory
                            path/*.jpg  # glob
                            'https://youtu.be/NUsoVlDFqZg'  # YouTube video
                            'rtsp://example.com/media.mp4'  # RTSP, RTMP, HTTP stream
```

今回はサンプル画像を使用し、動作確認した結果はこちら
```
(yolov5) [root@localhost yolov5]# python detect.py --source bus.jpg
detect: weights=yolov5s.pt, source=bus.jpg, imgsz=640, conf_thres=0.25, iou_thres=0.45, max_det=1000, device=, view_img=False, save_txt=False, save_conf=False, save_crop=False, nosave=False, classes=None, agnostic_nms=False, augment=False, update=False, project=runs/detect, name=exp, exist_ok=False, line_thickness=3, hide_labels=False, hide_conf=False, half=False
YOLOv5 ? v5.0-259-g831773f torch 1.9.0+cu102 CPU

Fusing layers...
[W NNPACK.cpp:79] Could not initialize NNPACK! Reason: Unsupported hardware.
/root/anaconda3/envs/yolov5/lib/python3.8/site-packages/torch/nn/functional.py:718: UserWarning: Named tensors and all their associated APIs are an experimental feature and subject to change. Please do not use them for anything important until they are released as stable. (Triggered internally at  /pytorch/c10/core/TensorImpl.h:1156.)
  return torch.max_pool2d(input, kernel_size, stride, padding, dilation, ceil_mode)
Model Summary: 224 layers, 7266973 parameters, 0 gradients
image 1/1 /root/yolov5/bus.jpg: 640x480 4 persons, 1 bus, 1 fire hydrant, Done. (1.132s)
Results saved to runs/detect/exp2
Done. (2.015s)
```

![image](https://user-images.githubusercontent.com/26809782/124346120-0bc94e00-dc18-11eb-8ef6-60e2363a6dc1.png)

# トラブルシューティング

- ImportError: libGL.so.1 on CentOS
 -  https://stackoverflow.com/questions/60628083/importerror-libgl-so-1-on-centos
 -  yum install mesa-libGL　で解決！
