import time
import picamera
from datetime import datetime

with picamera.PiCamera() as camera:
 camera.resolution = (1024, 768)
 camera.start_preview()
 time.sleep(2)
 timestr = datetime.now().strftime('%Y%m%d%H%M%S')
 camera.capture(timestr+'.jpg')