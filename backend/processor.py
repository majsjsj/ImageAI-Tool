from PIL import Image
from ai_model import ai_model
from torchvision import transforms
import torch


def process_image(input_path, output_path):

    # تحميل النموذج
    ai_model.load()

    # فتح الصورة
    image = Image.open(input_path).convert("RGB")

    # تجهيز الصورة بالشكل المطلوب للموديل
    transform = transforms.Compose([
        transforms.Resize((1024, 1024)),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )
    ])

    input_tensor = transform(image).unsqueeze(0)

    # نقل البيانات للجهاز المناسب
    input_tensor = input_tensor.to(ai_model.device)

    # تشغيل الذكاء الاصطناعي
    with torch.no_grad():

        prediction = ai_model.model(input_tensor)[-1].sigmoid().cpu()

    # استخراج الـ mask
    mask = prediction[0].squeeze()

    # تحويل الـ mask إلى صورة
    mask_image = transforms.ToPILImage()(mask)

    # إرجاع الـ mask لحجم الصورة الأصلي
    mask_image = mask_image.resize(image.size)

    # تحويل الصورة إلى RGBA
    result = image.convert("RGBA")

    # استخدام الـ mask كشفافية
    result.putalpha(mask_image)

    # حفظ النتيجة
    result.save(
        output_path,
        "PNG"
    )

    return output_path
