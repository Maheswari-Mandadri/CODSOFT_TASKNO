from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import os

# Load model
processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

# Images folder
folder = "images"

# Process every image
for file in os.listdir(folder):

    if file.lower().endswith((".jpg", ".jpeg", ".png")):

        image_path = os.path.join(folder, file)

        image = Image.open(image_path)

        # Process image
        inputs = processor(
            images=image,
            return_tensors="pt"
        )

        # Generate caption
        output = model.generate(
            **inputs,
            max_new_tokens=30
        )

        caption = processor.decode(
            output[0],
            skip_special_tokens=True
        )

        print("\nImage:", file)
        print("Caption:", caption)