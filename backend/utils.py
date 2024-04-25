from keras.models import load_model
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input
import numpy as np
import os
from openai import OpenAI
from groq import Groq

client = Groq(api_key=os.getenv("OPENAI_API_KEY"))
model = load_model('models/model.h5')
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
