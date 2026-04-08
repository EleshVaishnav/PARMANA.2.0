import base64

def encode_image(image_path):
    """Converts an image file to a base64 string for the API."""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def prepare_vision_payload(image_path, text_prompt):
    """Formats the message to include both image and text."""
    base64_image = encode_image(image_path)
    return [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": text_prompt},
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}
                }
            ]
        }
    ]
