from abc import ABC, abstractmethod


class BackgroundRemovalModel(ABC):

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def remove_background(self, image_path, output_path):
        pass


class LocalModel(BackgroundRemovalModel):

    def __init__(self):
        self.loaded = False

    def load(self):
        print("Loading background removal model...")
        self.loaded = True
        print("Model loaded successfully.")

    def remove_background(self, image_path, output_path):

        if not self.loaded:
            self.load()

        # سيتم وضع النموذج الحقيقي هنا
        # بدون تغيير باقي المشروع

        raise NotImplementedError(
            "AI model has not been connected yet."
        )
