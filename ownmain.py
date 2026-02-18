import cv2
import time
import mediapipe as mp

face_mesh = mp.solutions.face_mesh.Facemesh(
max_num_faces = 1, refine_landmarks= False)

mp_drawing = mp.solutions.drawing_utils


def runcam():
    capture = cv2.VideoCapture(0)

    if not capture.isOpened():
        raise RuntimeError("cant open yo cam bro")

    while True:
        ok, frame = capture.read()

        if not ok:
            break

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(rgb)


        if results.multi_face_landmarks:

            cv2.putText(frame, "FACE DETECTED", (20, 85), cv2.FONT_HERSHEY_COMPLEX, 5, (0, 255, 0), 5, cv2.LINE_AA)



        for i in results.multi_face_landmarks:
            mp_drawing.draw_landmarks(
                frame, i, face_mesh.FACEMESH_TESSELATION)

        cv2.imshow("4k hd footage", frame)
        key = cv2.waitKey(1)

        if key == ord('q') or key == ord('Q'):
            break
    
    capture.release()
    cv2.destroyAllWindows()

runcam()


