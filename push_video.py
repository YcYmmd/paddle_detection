# import cv2
# import subprocess as sp
# import time
#
# cap = cv2.VideoCapture("/home/server/file/ycy/project/test_fight_long.mp4")
# out_rtsp_url = 'rtsp://10.15.18.255:8554/input'
#
# fps = 25
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#
# command = ['ffmpeg',
#            '-y',
#            '-f', 'rawvideo',
#            '-vcodec', 'rawvideo',
#            '-pix_fmt', 'bgr24',
#            '-s', "{}x{}".format(width, height),
#            '-r', str(fps),
#            '-i', '-',
#            '-c:v', 'libx264',
#            '-pix_fmt', 'yuv420p',
#            '-f', 'rtsp',
#            out_rtsp_url]
#
# p = sp.Popen(command, stdin=sp.PIPE)
#
# frame_rate_delay = 1.0 / fps  # frame rate delay in seconds
#
# while (cap.isOpened()):
#     ret, frame = cap.read()
#     if not ret:
#         print("Opening camera is failed")
#         break
#     p.stdin.write(frame.tostring())
#     time.sleep(frame_rate_delay)  # add delay


import cv2
import subprocess as sp

# 此处从摄像头获取视频
cap = cv2.VideoCapture("/home/server/file/ycy/project/test_fight_long.mp4")
out_rtsp_url =  'rtsp://10.15.18.255:8554/input'
# Get video information
fps = int(cap.get(cv2.CAP_PROP_FPS))
print(fps)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
command = ['ffmpeg',
           '-y',
           '-f', 'rawvideo',
           '-vcodec', 'rawvideo',
           '-pix_fmt', 'bgr24',
           '-s', "{}x{}".format(width, height),
           '-r', str(fps),
           '-i', '-',
           '-c:v', 'libx264',
           '-pix_fmt', 'yuv420p',
           # '-preset', 'ultrafast',
           '-f', 'rtsp',
           out_rtsp_url]
p = sp.Popen(command, stdin=sp.PIPE)

while (cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
        print("Opening camera is failed")
        break
    frame = frame
    # print(frame.shape)
    p.stdin.write(frame.tostring())