import cv2

def detect_faces(image_path):
    try:
        
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        
        image = cv2.imread(image_path)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        
        faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5)

        if len(faces) == 0:
            print("No faces detected in the image.")
        else:
            print(f"Detected {len(faces)} face(s).")

            
            for (x, y, w, h) in faces:
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

            
            cv2.imshow("Detected Faces", image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    except Exception as e:
        print(f"An error occurred: {e}")

def detect_faces_in_Live():
    try:
        
        video_capture = cv2.VideoCapture(0)

        
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        while True:
            ret, frame = video_capture.read()
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5)

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            cv2.imshow("Video - Press 'q' to exit", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        video_capture.release()
        cv2.destroyAllWindows()

    except Exception as e:
        print(f"An error occurred: {e}")
        
def detect_faces_in_video(video_path):
    try:
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        video_capture = cv2.VideoCapture(video_path)

        while True:
            ret, frame = video_capture.read()
            if not ret:
                break

            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5)

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            cv2.imshow('Detected Faces', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        video_capture.release()
        cv2.destroyAllWindows()

    except Exception as e:
        print(f"An error occurred: {e}")        

if __name__ == "__main__":
    while True:
        A = input("What do you want to upload (Image, Video, Both or live): ")
        
        if A.lower() == "exit":
            break
        
        if A.lower() == "image":
            image_path = input("Enter the image file path: ")
            detect_faces(image_path)
            print("✨if u want exit type exit✨")
    
        elif A.lower() == "live":
            detect_faces_in_Live()
            print("✨if u want exit type exit✨")
            
        elif A.lower() == "video":
            video_path = input("Enter the video file path: ")
            detect_faces_in_video(video_path)
            print("✨if u want exit type exit✨")
    
        elif A.lower() == "both":
            image_path = input("Enter the image file path: ")
            video_path = input("Enter the video file path: ")
            detect_faces(image_path)
            detect_faces_in_video(video_path)
            print("✨if u want exit type exit✨")
