import torch
from transformers import AutoModelForImageSegmentation


MODEL_NAME = "ZhengPeng7/BiRefNet"


class BiRefNetModel:

    def __init__(self):

        self.device = (
            "cuda"
            if torch.cuda.is_available()
            else "cpu"
        )

        self.model = None


    def load(self):

        if self.model is not None:
            return


        print(
            f"Loading {MODEL_NAME} "
            f"on {self.device}..."
        )


        self.model = (
            AutoModelForImageSegmentation
            .from_pretrained(
                MODEL_NAME,
                trust_remote_code=True
            )
        )


        self.model = self.model.to(
            self.device
        )


        self.model.eval()


        print(
            "BiRefNet model loaded successfully."
        )


    def is_ready(self):

        return self.model is not None


ai_model = BiRefNetModel()
