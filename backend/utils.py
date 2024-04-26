# from keras.models import load_model
# from keras.preprocessing import image
# from keras.applications.resnet50 import preprocess_input
import numpy as np
import os
import requests
# from openai import OpenAI
from groq import Groq
import base64

client = Groq(api_key=os.getenv("OPENAI_API_KEY"))
HF_API = os.getenv("HF_API")
# model = load_model('models/model.h5')
output_class = ["battery", "glass", "metal","organic", "paper", "plastic"]
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

def preprocessing_input(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img) # ResNet50 preprocess_input
    return img

async def predict(new_image_path):
    try:
        test_image = preprocessing_input(new_image_path)
        predicted_array = model.predict(test_image)
        predicted_value = output_class[np.argmax(predicted_array)]
        predicted_accuracy = round(np.max(predicted_array) * 100, 2)

        return predicted_value, predicted_accuracy
    except Exception as e:
        return f"Error processing image: {str(e)}", 0

async def predict_zeroshot(new_image_path):
    try:
        API_URL = "https://api-inference.huggingface.co/models/openai/clip-vit-large-patch14-336"
        headers = {"Authorization": f"Bearer {HF_API}"}

        def query(data):
            with open(data["image_path"], "rb") as f:
                img = f.read()
            payload={
                "parameters": data["parameters"],
                "inputs": base64.b64encode(img).decode("utf-8")
            }
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()

        output = query({
            "image_path": f"{new_image_path}",
            "parameters": {"candidate_labels": output_class},
        })
        max_component = max(output, key=lambda x: x['score'])
        predicted_value, predicted_accuracy = max_component['label'], max_component['score']
        return predicted_value, predicted_accuracy
        
    except Exception as e:
        return f"Error processing image: {str(e)}", 0 


def input_trash(input):
    messages = [
        {"role": "system", "content": "Bạn là một nhà tuyên truyền bảo vệ môi trường. Nhiệm vụ của bạn là cung cấp cho tôi thông tin cần thiết nhất về loại rác mà tôi đưa ra trong một list chỉ 2 dòng (đổi tên loại rác sang tiếng Việt trước khi trả lời), tập trung vào quá trình phân hủy và cách xử lý loại rác này. Tránh chi tiết hoặc giải thích không cần thiết."},
    ]
    messages.append(
        {"role": "user", "content": f"{input}"},
    )
    chat = client.chat.completions.create(model="llama3-8b-8192", messages=messages)
    reply = chat.choices[0].message.content
    return reply
