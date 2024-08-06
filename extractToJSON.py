import cv2
import mediapipe as mp
import os
import json


# Khởi tạo MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=False, model_complexity=1, enable_segmentation=False,
                    min_detection_confidence=0.5)


# Hàm để xử lý video và lưu tọa độ pose landmarks dưới dạng JSON
def process_video(video_path, output_json_path):
    # nếu chưa có thư mục thì tạo
    if not os.path.exists(output_json_path):
        os.makedirs(output_json_path)

    cap = cv2.VideoCapture(video_path)
    frame_data = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Chuyển đổi khung hình thành RGB
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Xử lý khung hình để phát hiện pose
        results = pose.process(image_rgb)

        # Lưu tọa độ pose landmarks nếu có
        if results.pose_landmarks:
            landmarks = []
            for lm in results.pose_landmarks.landmark:
                landmarks.append({
                    'x': lm.x,
                    'y': lm.y,
                    'z': lm.z,
                    'visibility': lm.visibility
                })
            frame_data.append(landmarks)

    cap.release()

    # Lưu dữ liệu pose landmarks vào tệp JSON
    with open(output_json_path, 'w') as json_file:
        json.dump(frame_data, json_file, indent=4)


# Đường dẫn đến video và tệp JSON đầu ra
video_path = 'D:/IT05/Project/dataset/single_bound'
output_json_path = 'pose_landmarks.json'

# lấy các list video từ thư mục
video_list = [os.path.join(video_path, f) for f in os.listdir(video_path) if f.endswith(('.mp4'))]

# Xử lý video và lưu tọa độ pose landmarks
for video in video_list:
    video_name = os.path.splitext(os.path.basename(video))[0]
    output_folder = os.path.join(output_json_path, video_name)
    process_video(video, output_json_path)
    print(f"Pose landmarks have been saved to {output_json_path}")