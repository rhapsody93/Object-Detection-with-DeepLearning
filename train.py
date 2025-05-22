import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

import torch
from ultralytics import YOLO

# dataset
dataset = [
    {
        "name": "custom_dataset",
        "data_yaml": "custom_dataset.yaml"
    }
]

# YOLO model & conditions setting
yolo_model = "yolov8l.pt"
epochs = 30
imgsz = 640
batch = 4
device = 0  # CUDA:0 (will use RTX 4060 GPU)

for train_set in dataset:
    print(f"\nTraining Start: {train_set['name']}")

    model = YOLO(yolo_model)

    try:
        model.train(
            data=train_set['data_yaml'],
            epochs=epochs,
            imgsz=imgsz,
            batch=batch,
            name=f"exp_{train_set['name']}",
            device=device
        )
        print(f"Train finished: {train_set['name']}\n")
    except Exception as e:
        print(f"Error has occurred: {train_set['name']}\nError: {e}\n")