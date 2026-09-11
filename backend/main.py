from flask import Flask, request, jsonify, send_file
from flask_cors import CORS

from processor import process_image

import os
import uuid


app = Flask(__name__)

# السماح للواجهة بالاتصال بالـ Backend
CORS(app)


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
        file_id + ".input"
    )

    output_path = os.path.join(
        RESULT_FOLDER,
        file_id + ".png"
    )


    try:

        # حفظ الملف الأصلي
        image.save(input_path)


        # تشغيل الذكاء الاصطناعي
        process_image(
            input_path,
            output_path
        )


        # إرسال PNG للواجهة
        return send_file(
            output_path,
            mimetype="image/png",
            as_attachment=False
        )


    except Exception as error:

        print("Processing error:", error)

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
