from mediapipe.tasks.python import BaseOptions
from mediapipe.tasks.python import vision
from pathlib import Path
import time, cv2, random, os, core_funcs as cf, mediapipe as medpi, pygame as pg

os.chdir(Path(__file__).resolve().parent)

pg.mixer.init()

baseopt = BaseOptions(model_asset_path='face_landmarker.task')
options = vision.FaceLandmarkerOptions(base_options=baseopt, num_faces=1)
detect = vision.FaceLandmarker.create_from_options(options)

cap = cv2.VideoCapture(3)

currenttime = None
waittime = 0.7

bug = 0

thresh= -0.001

if not cap.isOpened():
    raise RuntimeError("can't open yo cam bro")

while True: 
    ok, frame = cap.read()
    
    if bug > 90:
        break
    if not ok:
        bug+=1
        continue
    
    bug=0

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_img = medpi.Image(image_format=medpi.ImageFormat.SRGB, data=rgb)
    result = detect.detect(mp_img)

    if not result.face_landmarks:
        cv2.putText(frame, "No Face", (99, 150), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 3)
        cv2.imshow("CAM", frame)

        if cv2.waitKey(1) == ord('q'):
            break
        continue

    lms = result.face_landmarks[0]

    score = cf.smilescore(lms)

    if score > thresh:
        if currenttime is None:
            currenttime = time.time()
            i, j = random.randint(1, 5), random.randint(1, 4)             


        if (time.time() - currenttime) > waittime:

           
            #cv2.putText(frame, f"SMILE DETECTED {score}", (99, 150), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 3)



            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)


            frame = cf.display_overlay(i, frame)
            cv2.imshow("CAM", frame)
            play = cf.phonk(j)



            freeze = time.time()
            quit = False
            while (time.time() - freeze < 6):

                cap.grab()

                if cv2.waitKey(1) == ord('q'):
                    quit = True
                    break   
            currenttime = None

            if quit:
                break
        else:
            cv2.imshow("CAM", frame)


    else:
        cv2.imshow("CAM", frame)
        currenttime= None


    if cv2.waitKey(1) == ord('q'):
            break
    
print(bug)
pg.mixer.quit()
cap.release()
cv2.destroyAllWindows()