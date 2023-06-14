# The example is taken from Ultralytics Docs https://docs.ultralytics.com/usage/python/

import argparse
import os
import sys
from ultralytics import YOLO
from pathlib import Path


FILE = Path(__file__).resolve()
ROOT = FILE.parents[1]  # YOLOv5 root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative


def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=str, default=ROOT / "coco128.yaml", help="dataset.yaml path")
    parser.add_argument("--weights", type=str, default=ROOT / "yolov8s.pt", help="model path(s)")
    parser.add_argument("--batch-size", type=int, default=32, help="batch size")
    parser.add_argument("--epochs", type=int, default=100, help="total training epochs")
    parser.add_argument("--augment", action="store_true", help="augmented inference")
    parser.add_argument("--project", default="runs/val", help="save to project/name")

    opt = parser.parse_args()
    return opt


def main(opt):
    # Load a model
    model = YOLO(opt.weights)  # load a pretrained model (recommended for training)

    # Use the model
    model.train(data=opt.data, epochs=opt.epochs, project=opt.project)  # train the model

    model.val()  # evaluate model performance on the validation set

    model("https://ultralytics.com/images/bus.jpg", save=True)  # predict on an image

    model.export(format="onnx")  # export the model to ONNX format


if __name__ == "__main__":
    opt = parse_opt()
    main(opt)
