import cv2
import mediapipe as mp


class Face:
    """Direct access of face module"""
    def __init__(self):
        self.frame_rgb = None
        self.mp_face_detection = mp.solutions.face_detection.FaceDetection()

    def detected(self, frame):
        """Detect the face and return true or false"""

        # Process the frame with the Face Detection module
        self.frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame with the Face Detection module
        results = self.mp_face_detection.process(self.frame_rgb)

        # Draw a bounding box around the detected face
        if results.detections:
            for detection in results.detections:
                bbox = detection.location_data.relative_bounding_box
                h, w, _ = frame.shape
                x, y, width, height = int(bbox.xmin * w), int(bbox.ymin * h), int(bbox.width * w), int(bbox.height * h)
                cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 2)
            return True
        else:
            return False
