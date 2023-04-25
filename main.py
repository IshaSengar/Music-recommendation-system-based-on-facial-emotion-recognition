from fer import FER
import cv2
import webbrowser

cam = cv2.VideoCapture(0)
while True :
    ret, frame = cam.read()
    cv2.imshow("Capturing Your Emotion", frame)
    if not ret :
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
        
    elif k%256 == 32:
        # SPACE pressed
        img_name = "emotion.jpg"
        cv2.imwrite(img_name, frame)
        print("Your emotion has been captured.")
        break

cam.release()
cv2.destroyAllWindows()

emotion_detector = FER(mtcnn=True)
test_img = cv2.imread("emotion.jpg")
emotion, _ = emotion_detector.top_emotion(test_img)
# angry, disgust, fear, sad, happy, surprise, neutral


singer = input("Please enter the name of the singer:")
lang = input("Please enter the language:")
print(f"You are feeling {emotion} so your recommendations are")
webbrowser.open(f"https://www.youtube.com/results?search_query={lang}+{emotion}+song+{singer}")