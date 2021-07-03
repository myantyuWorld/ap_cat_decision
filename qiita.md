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

- https://github.com/ultralytics/yolov5


## Yolov5の使用方法

```
$ python detect.py --source 0  # webcam
                            file.jpg  # image 
                            file.mp4  # video
                            path/  # directory
                            path/*.jpg  # glob
                            'https://youtu.be/NUsoVlDFqZg'  # YouTube video
                            'rtsp://example.com/media.mp4'  # RTSP, RTMP, HTTP stream
```

# トラブルシューティング

- ImportError: libGL.so.1 on CentOS
 -  https://stackoverflow.com/questions/60628083/importerror-libgl-so-1-on-centos
 -  yum install mesa-libGL　で解決！
