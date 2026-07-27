import cv2
print("AI Fitness Coach has started!")

reps = input("Enter the number of repetitions you completed: ")
weight = input("Enter the weight you lifted (in lbs): ")

volume = round(int(reps) * float(weight))
print(f"Total volume lifted: {volume} lbs")

def isRepValid(angle, minAngle = 30, maxAngle = 160):
    return minAngle <= angle <= maxAngle

def average_angle(angle_list):
    total = 0
    for i in range (len(angle_list)):
        total += angle_list[i]
    return total / len(angle_list)

test_angles = [10, 20, 30]
result = average_angle(test_angles)
print(result)  # should print 20.0

def get_visible_joints(joints_dict):
    result = []
    for key, value in joints_dict.items():
        if value['visibility'] > 0.5:
            result.append(key)
    return result

joints_dict = {
    "left_elbow": {"x": 0.5, "y": 0.6, "visibility": 0.9},
    "right_elbow": {"x": 0.3, "y": 0.4, "visibility": 0.2},
    "left_knee": {"x": 0.5, "y": 0.8, "visibility": 0.7}
}

print(get_visible_joints(joints_dict))

def count_valid_reps():
    rep_count = 0
    while True:
        angle = float(input("Enter the angle of your joint (or type '-1' to finish): "))
        if angle == -1:
            break
        elif angle <30:
            rep_count += 1
    return rep_count

print ("Total valid repetitions counted:", count_valid_reps())

class Joint:
    def __init__(self, name, x, y, visibility):
        self.name = name
        self.x = x
        self.y = y
        self.visibility = visibility

    def is_visible(self):
        return self.visibility > 0.5

elbow = Joint("left_elbow", 0.5, 0.6, 0.9)
print(elbow.name)
print(elbow.is_visible())


cap = cv2.VideoCapture("CV_Practice.MOV")

while True:
    success, frame = cap.read()

    if not success:
        break

    cv2.imshow("My Video", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()