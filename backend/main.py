from flask import Flask, request, jsonify
from PIL import Image
import os
import uuid

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
RESULT_FOLDER = "results"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return jsonify({
        "status": "online",
        "message": "ImageAI Engine is running"
    })


@app.route("/process", methods=["POST"])
def process_image():

    if "image" not in request.files:
        return jsonify({
            "error": "No image uploaded"
        }), 400

    file = request.files["image"]

    if file.filename == "":
        return jsonify({
            "error": "Invalid filename"
        }), 400

    file_id = str(uuid.uuid4())

    input_path = os.path.join(
        UPLOAD_FOLDER,
        file_id + ".png"
    )

    output_path = os.path.join(
        RESULT_FOLDER,
        file_id + ".png"
    )

    image = Image.open(file)
    image.save(input_path)

    # هنا سنضع نموذج إزالة الخلفية لاحقًا
    # model.process(input_path, output_path)

    # مؤقتًا نحفظ الصورة كما هي
    image.save(output_path)

    return jsonify({
        "success": True,
        "file": output_path
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
