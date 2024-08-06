import cv2
import os

# hàm để lấy và lưu các frame từ video
def frames(video_path, output_folder):
    # nếu chưa có thư mục thì tạo
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # đọc video
    cap = cv2.VideoCapture(video_path)
    cnt = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # lưu frame dưới dạng ảnh
        frame_path = os.path.join(output_folder, 'frame%d.jpg' % cnt)
        cv2.imwrite(frame_path, frame)
        cnt += 1

    cap.release()

# đường dẫn đến thư mục chứa dataset
# video_directory = "D:/IT05/Project/dataset/single_bound"
video_directory = "D:/IT05/Project/dataset/run_in_placed"

# thư mục để lưu các frame
output_dir = "output_frames"

# lấy các list video từ thư mục
video_list = [os.path.join(video_directory, f) for f in os.listdir(video_directory) if f.endswith(('.mp4'))]

for video in video_list:
    video_name = os.path.splitext(os.path.basename(video))[0]
    output_folder = os.path.join(output_dir, video_name)
    frames(video, output_folder)
    print(f"extracted frames from {video} to {output_folder}")

