from flask import Flask, request, jsonify, send_file
from processor import process_image

import os
import uuid

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
RESULT_FOLDER = "results"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)


@app.get("/")
def home():
    return jsonify({
        "status": "online",
        "engine": "ImageAI",
        "message": "AI image engine is ready"
    })


@app.post("/process")
def process():

    if "image" not in request.files:
        return jsonify({
            "success": False,
            "error": "No image uploaded"
        }), 400

    image = request.files["image"]

    if not image.filename:
        return jsonify({
            "success": False,
            "error": "Invalid image"
        }), 400

    file_id = uuid.uuid4().hex

    input_path = os.path.join(
        UPLOAD_FOLDER,
        file_id + ".png"
    )

    output_path = os.path.join(
        RESULT_FOLDER,
        file_id + ".png"
    )

    try:

        image.save(input_path)

        process_image(
            input_path,
            output_path
        )

        return send_file(
            output_path,
            mimetype="image/png",
            as_attachment=False
        )

    except Exception as error:

        return jsonify({
            "success": False,
            "error": str(error)
        }), 500


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )
