# import cv2
#
# # RTSP URL
# rtsp_url = "rtsp://10.15.18.255:8554/input"
#
# # 视频编解码器
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
#
# # 创建VideoWriter对象
# output_file = "/home/server/file/ycy/project/save_video.mp4"
# out = None
#
# # 打开RTSP流
# cap = cv2.VideoCapture(rtsp_url)
#
# # 检查摄像头是否成功打开
# if not cap.isOpened():
#     print("Error: Failed to open RTSP stream.")
#     exit()
#
# # 获取RTSP流的帧率
# fps = cap.get(cv2.CAP_PROP_FPS)
# print("FPS:", fps)
#
# # 获取RTSP流的第一帧，以获取宽度和高度
# ret, frame = cap.read()
# if ret:
#     frame_height, frame_width, _ = frame.shape
#     print("Frame size:", frame_width, "x", frame_height)
#
#     # 视频编解码器
#     fourcc = cv2.VideoWriter_fourcc(*'mp4v')
#     # 创建VideoWriter对象
#     out = cv2.VideoWriter(output_file, fourcc, fps, (frame_width, frame_height))
#
# # 读取RTSP流并保存为MP4
# while True:
#     ret, frame = cap.read()
#     if ret:
#         # 写入视频帧到输出文件
#         out.write(frame)
#         # 关闭VideoWriter
#         out.release()
#         # 重新创建VideoWriter对象
#         out = cv2.VideoWriter(output_file, fourcc, fps, (frame_width, frame_height), isColor=True)
#     else:
#         print("Error: Failed to read frame.")
#         break
#
# # 关闭VideoWriter和摄像头
# if out is not None:
#     out.release()
# cap.release()
# cv2.destroyAllWindows()
import cv2

# RTSP URL
rtsp_url = "rtsp://10.15.18.255:8554/input"

# 视频编解码器
fourcc = cv2.VideoWriter_fourcc(*'MJPG')

# 创建VideoWriter对象
output_file = "/home/server/file/ycy/project/save_video.avi"
out = None

# 打开RTSP流
cap = cv2.VideoCapture(rtsp_url)

# 检查摄像头是否成功打开
if not cap.isOpened():
    print("Error: Failed to open RTSP stream.")
    exit()

# 获取RTSP流的帧率
fps = cap.get(cv2.CAP_PROP_FPS)
print("FPS:", fps)

# 获取RTSP流的第一帧，以获取宽度和高度
ret, frame = cap.read()
if ret:
    frame_height, frame_width, _ = frame.shape
    print("Frame size:", frame_width, "x", frame_height)

    # 视频编解码器
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    # 创建VideoWriter对象
    out = cv2.VideoWriter(output_file, fourcc, fps, (frame_width, frame_height))

# 读取RTSP流并保存为MP4
while True:
    ret, frame = cap.read()
    if ret:
        # 写入视频帧到输出文件
        out.write(frame)
    else:
        print("Error: Failed to read frame.")
        break

# 关闭VideoWriter和摄像头
if out is not None:
    out.release()
cap.release()
cv2.destroyAllWindows()