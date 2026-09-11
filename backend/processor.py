from PIL import Image
from ai_model import ai_model
from torchvision import transforms
import torch


def process_image(input_path, output_path):

    ai_model.load()

    image = Image.open(input_path).convert("RGB")

    transform = transforms.Compose([
        transforms.Resize((1024, 1024)),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )
    ])

    input_tensor = transform(image).unsqueeze(0)

    # نفس نوع البيانات المستخدم في الموديل
    input_tensor = input_tensor.to(
        device=ai_model.device,
        dtype=torch.float16
    )

    with torch.no_grad():
        prediction = ai_model.model(input_tensor)[-1].sigmoid().cpu()

    mask = prediction[0].squeeze()

    mask_image = transforms.ToPILImage()(mask)
    mask_image = mask_image.resize(image.size)

    result = image.convert("RGBA")
    result.putalpha(mask_image)

    result.save(output_path, "PNG")

    return output_path
