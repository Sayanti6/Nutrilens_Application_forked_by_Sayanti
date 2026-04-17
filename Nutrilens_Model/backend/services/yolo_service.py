import cv2
import numpy as np
from ultralytics import YOLO
from PIL import Image
import io
from backend.core.config import settings

class YOLOService:
    _instance = None
    _model = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(YOLOService, cls).__new__(cls)
            # Initialize the model only once
            try:
                cls._model = YOLO(settings.MODEL_PATH)
                print(f"Model loaded successfully from {settings.MODEL_PATH}")
            except Exception as e:
                print(f"FAILED to load model from {settings.MODEL_PATH}: {e}")
                # Fallback to local model if path is wrong
                cls._model = YOLO("yolov8s.pt") 
        return cls._instance

    @property
    def model(self):
        return self._model

    def predict(self, image_input):
        """
        Runs YOLO inference on the input image.
        image_input: bytes or PIL.Image.Image or numpy array
        """
        # Convert bytes to PIL if necessary
        if isinstance(image_input, bytes):
            image_input = Image.open(io.BytesIO(image_input))
        
        # Run inference
        results = self.model.predict(
            source=image_input, 
            conf=settings.CONFIDENCE_THRESHOLD,
            save=False
        )

        detections = []
        for result in results:
            boxes = result.boxes
            for box in boxes:
                # Get bounding box coordinates
                x1, y1, x2, y2 = box.xyxy[0].tolist()
                
                # Get class label and confidence
                cls_id = int(box.cls[0])
                label = self.model.names[cls_id]
                confidence = float(box.conf[0])
                
                detections.append({
                    "class": label,
                    "confidence": round(confidence, 3),
                    "bbox": {
                        "x_min": round(x1, 2),
                        "y_min": round(y1, 2),
                        "x_max": round(x2, 2),
                        "y_max": round(y2, 2)
                    }
                })
        
        return detections

yolo_service = YOLOService()
