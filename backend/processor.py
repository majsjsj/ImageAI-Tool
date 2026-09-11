from PIL import Image
import os


class ImageProcessor:

    def __init__(self):
        self.model = None

    def load_model(self):
        """
        هنا سنحمّل نموذج إزالة الخلفية.
        """
        print("Loading AI model...")

        # سيتم تركيب RMBG-2.0 هنا لاحقًا

        self.model = True

        print("AI model loaded.")

    def remove_background(self, input_path, output_path):

        if self.model is None:
            self.load_model()

        image = Image.open(input_path).convert("RGBA")

        # مؤقتًا: نحفظ الصورة كما هي
        # سيتم استبدال هذا الجزء بخوارزمية RMBG

        image.save(output_path, "PNG")

        return output_path


processor = ImageProcessor()
