
import cv2
import mediapipe as mp
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_face_mesh = mp.solutions.face_mesh




# For webcam input:
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,640)
gen=int(cap.get(3))
yuk=int(cap.get(4))

print(gen,yuk)



with mp_face_mesh.FaceMesh(
        max_num_faces=3,
        refine_landmarks=True,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as face_mesh:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            # If loading a video, use 'break' instead of 'continue'.
            continue

        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(image)

        # Draw the face mesh annotations on the image.
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        bos=np.zeros((yuk,gen),dtype=np.uint8)
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                for i in range(468):
                    pt=face_landmarks.landmark[i]
                    x=int(pt.x*gen)
                    y=int(pt.y*yuk)
                    
                    cv2.circle(bos, (x, y), 1, (100, 100, 0), cv2.FILLED)

        cv2.imshow('MediaPipe Face Mesh', cv2.flip(image, 1))
        cv2.imshow("mesh",cv2.flip(bos,1))
        
        if cv2.waitKey(5) & 0xFF == 27:
            break

cap.release()
