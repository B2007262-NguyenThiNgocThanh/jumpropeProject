import cv2
import mediapipe as mp

mp_pose = mp.solutions.pose
mp_draw = mp.solutions.drawing_utils
pose = mp_pose.Pose()
# cap = cv2.VideoCapture("D:\IT05\Project\dataset\An8tB6p4kE6JmTRUZXw4uCzfLi67gBLyOTIc0DlVEEgaMkF6lBea8U9QAQANnYUCapxCWoNHGIhA7xJYUGTWgBBf.mp4")
cap = cv2.VideoCapture("D:\IT05\Project\dataset\An8h7tAB_DzV2Ln_4HOl11IGGK-VmQWxVnFs5mwBUHb18zTTOJjpRU1KfesLJ2dw0tvhRw2GvX1yhFhd6FlBxH4.mp4"
                       )

# load video
while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (800,1080))
    results = pose.process(frame)
    mp_draw.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
    print(results.pose_landmarks)
    cv2.imshow("Pose Estimation",  frame)
    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

# Camera
# cap_camera = cv2.VideoCapture(0)
#
# while cap_camera.isOpened():
#     ret, frame = cap_camera.read()
#     frame = cv2.resize(frame, (640, 480))
#     results = pose.process(frame)
#     mp_draw.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
#     print(results.pose_landmarks)
#     cv2.imshow("Pose Estimation", frame)
#
#
#     if cv2.waitKey(10) & 0xFF == ord("q"):
#         break
#
# cap_camera.release()
# cv2.destroyAllWindows()