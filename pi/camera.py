import time
import picamera
from datetime import datetime
from smb.SMBConnection import SMBConnection

host="192.168.0.100"  #ip or domain name
username="click"
password="password"
conn=SMBConnection(username,password,"","",use_ntlm_v2 = True)
result = conn.connect(host, 445)
print("login successful")


with picamera.PiCamera() as camera:
 camera.resolution = (1024, 768)
 camera.start_preview()
 time.sleep(2)
 timestr = datetime.now().strftime('%Y%m%d%H%M%S')
 camera.capture(timestr+'.jpg')