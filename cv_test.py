import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

model_path = "pose_landmarker.task"

base_options = python.BaseOptions(model_asset_path=model_path)
options = vision.PoseLandmarkerOptions(
    base_options=base_options,
    running_mode=vision.RunningMode.VIDEO
)
landmarker = vision.PoseLandmarker.create_from_options(options)

cap = cv2.VideoCapture("CV_Practice.MOV")

cv2.namedWindow("My Video", cv2.WINDOW_NORMAL)
cv2.resizeWindow("My Video", 640, 480)

frame_timestamp_ms = 0
fps = cap.get(cv2.CAP_PROP_FPS)
frame_duration_ms = int(1000 / fps)

while True:
    success, frame = cap.read()
    if not success:
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)

    result = landmarker.detect_for_video(mp_image, frame_timestamp_ms)
    frame_timestamp_ms += frame_duration_ms

    if result.pose_landmarks:
        for landmark in result.pose_landmarks[0]:
            x = int(landmark.x * frame.shape[1])
            y = int(landmark.y * frame.shape[0])
            cv2.circle(frame, (x, y), 4, (0, 255, 0), -1)

    cv2.imshow("My Video", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()