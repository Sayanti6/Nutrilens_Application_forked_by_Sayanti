from ultralytics import YOLO
import os
import torch

def train_v11_model():
    """
    Trains (fine-tunes) the YOLOv11 model for Indian Food Detection.
    Includes hardware-optimized configurations.
    """
    # 1. Load the pre-trained YOLO11 Medium model (Excellent accuracy/speed balance)
    print("Loading base model: yolo11m.pt...")
    model = YOLO("yolo11m.pt")

    # 2. Path to our Indian Food dataset configuration
    # Note: prepare_dataset.py should be run first to reorganize data
    DATASET_CONFIG = "d:/Projects/Nutrilens/ai_model/dataset/dataset.yaml"
    
    if not os.path.exists(DATASET_CONFIG):
        print(f"Error: Dataset configuration not found at {DATASET_CONFIG}")
        print("Please run prepare_dataset.py first.")
        return

    # 3. Hardware Optimization
    device = "0" if torch.cuda.is_available() else "cpu"
    print(f"Using device: {device}")
    
    # 4. Start Training with Enhanced Augmentation
    print("Starting Training with YOLOv11 optimized configuration...")
    
    results = model.train(
        data=DATASET_CONFIG,
        epochs=100,             # Full training run
        imgsz=640,              # Standard YOLO resolution
        batch=16,               # Safe batch size for mid-range GPUs
        device=device,          # Auto-detect GPU/CPU
        patience=30,            # Stop early if no improvement for 30 epochs
        save=True,              # Save weights
        project="Nutrilens",    # Output project name
        name="IndianFoodV2",    # v2 for YOLOv11
        
        # --- Advanced Augmentation (To handle real-world dining photos) ---
        hsv_h=0.015,            # image HSV-Hue augmentation (fraction)
        hsv_s=0.7,              # image HSV-Saturation augmentation (fraction)
        hsv_v=0.4,              # image HSV-Value augmentation (fraction)
        degrees=10.0,           # image rotation (+/- deg)
        translate=0.1,          # image translation (+/- fraction)
        scale=0.5,              # image scale (+/- gain)
        fliplr=0.5,             # image flip left-right (probability)
        mosaic=1.0,             # image mosaic (probability)
        mixup=0.1,              # image mixup (probability)
        
        # --- Stability ---
        amp=True,               # Automatic Mixed Precision
        workers=4,              # CPU workers
        exist_ok=True           # Overwrite if name already exists
    )

    print("Training Complete!")
    print(f"The improved model is saved in: runs/Nutrilens/IndianFoodV2/weights/best.pt")

if __name__ == "__main__":
    try:
        train_v11_model()
    except Exception as e:
        print(f"Training failed: {e}")
