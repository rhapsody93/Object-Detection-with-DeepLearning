import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

import torch
from ultralytics import YOLO

dataset = [
    {
        "name": "custom_dataset",
        "model_path": "C:/Users/USER/anaconda3/envs/obj_det/object_detection/runs/detect/exp_custom_dataset84/weights/best.pt",
        "data_yaml": "custom_dataset.yaml"
    }
]

# YOLO model & conditions setting
trained_model = dataset[0]["model_path"]  # best model path
imgsz = 640
batch = 4
device = 0  # CUDA:0 (will use RTX 4060 GPU)

for test_set in dataset:
    print(f"\nTesting Start: {test_set['name']}")

    model = YOLO(trained_model)

    try:
        # test execution
        results = model.val(
            data=test_set['data_yaml'],
            imgsz=imgsz,
            batch=batch,
            name=f"test_{test_set['name']}",
            device=device,
            split='test'  # test set
        )

        # test result
        metrics = results.box  # box detection results
        print(f"\nTest Results for {test_set['name']}:")
        print(f"mAP50: {metrics.map50:.4f}")
        print(f"mAP50-95: {metrics.map:.4f}")
        print(f"Precision: {metrics.p:.4f}")
        print(f"Recall: {metrics.r:.4f}")
        print(f"Test finished: {test_set['name']}\n")

    except Exception as e:
        print(f"Error has occurred: {test_set['name']}\nError: {e}\n")
