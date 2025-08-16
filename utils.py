import numpy as np
import torch
import torchvision.models as models
import torchvision.transforms as transforms
from sklearn.feature_extraction.text import TfidfVectorizer
from PIL import Image

# Load pretrained ResNet
resnet = models.resnet50(pretrained=True)
resnet.fc = torch.nn.Identity()
resnet.eval()

# Text vectorizer (TF-IDF)
vectorizer = TfidfVectorizer(stop_words="english")

def extract_text_features(texts):
    return vectorizer.fit_transform(texts)

def extract_image_features(image_path):
    transform = transforms.Compose([
        transforms.Resize((224,224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485,0.456,0.406], std=[0.229,0.224,0.225])
    ])
    image = Image.open(image_path).convert("RGB")
    img_tensor = transform(image).unsqueeze(0)
    with torch.no_grad():
        features = resnet(img_tensor).numpy()
    return features

def recommend_products(product_id, data):
    # Placeholder for recommendation logic
    # Combine text + image similarity
    return data.sample(5).to_dict("records")