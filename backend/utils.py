from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from rembg import remove
import numpy as np
from PIL import Image

model = load_model('models/model.h5')
output_class = ["battery", "glass", "metal","organic", "paper", "plastic"]
    
async def predict(new_image_path):
    try:
        test_image = Image.open(new_image_path)
        test_image = test_image.resize((224, 224)).convert("RGB")
        test_image = remove(test_image)
        test_image = test_image.convert("RGB")  # Convert to RGB format
        test_image = image.img_to_array(test_image) / 255
        test_image = np.expand_dims(test_image, axis=0)

        predicted_array = model.predict(test_image)
        predicted_value = output_class[np.argmax(predicted_array)]
        predicted_accuracy = round(np.max(predicted_array) * 100, 2)

        return predicted_value, predicted_accuracy
    except Exception as e:
        return f"Error processing image: {str(e)}", 0
