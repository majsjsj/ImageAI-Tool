import torch

MODEL_NAME = "briaai/RMBG-2.0"

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

IMAGE_SIZE = 1024

OUTPUT_FORMAT = "PNG"

MODEL_VERSION = "1.0"
