import os
from fastapi import FastAPI, File, UploadFile
import cv2 as cv
from mtcnn_cv2 import MTCNN
from torchvision import transforms
from PIL import Image
import torch
import numpy as np


device = 'cpu'
emotion_model = torch.load('./weights/EmotionNet_b27.pt',
                           map_location=torch.device('cpu'))
emotion_model.eval()
idx_to_class = {0: 'Anger', 1: 'Disgust', 2: 'Fear',
                3: 'Happiness', 4: 'Neutral', 5: 'Sadness', 6: 'Surprise'}
test_transforms = transforms.Compose(
    [
        transforms.Resize((260, 260)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225])
    ]
)

detector = MTCNN()
emotion_detector = emotion_model


def infer(image):
    faces = detector.detect_faces(image)
    counter = 0
    emotion_list = []
    for bx in faces:
        box = bx['box']

        cropped = image[box[1]:box[1]+box[3],
                        box[0]:box[0] + box[2]]
        counter += 1

        img_tensor = test_transforms(Image.fromarray(cropped))
        img_tensor.unsqueeze_(0)
        with torch.no_grad():
            scores = emotion_model(img_tensor.to(device))
        scores = scores[0].data.cpu().numpy()
        emotion = idx_to_class[np.argmax(scores)]
        emotion_list.append(emotion)

    counter = 0
    for em in emotion_list:
        faces[counter]["emotion"] = em
        counter += 1
    return faces


app = FastAPI(
    title="Facial detection and emotion recognition services",
    version="0.8",
    contact={
        "name": "Ali Amini Bagh",
        "email": "aliaminibagh@gmail.com",
        "github": 'https://github.com/aliaminibagh'
    }
)


@app.post("/infer", tags=["Inference"])
async def Infer(image: UploadFile = File(...)):
    if not os.path.exists('./uploaded_images'):
        os.makedirs('./uploaded_images')
    tempName = os.path.join("uploaded_images", 'temp.jpg')
    with open((tempName), "wb+") as file_object:
        file_object.write(image.file.read())

    img = cv.imread(tempName)
    results = infer(img)
    if len(results) == 0:
        {'status': 201, 'message': 'no faces detected'}
    return ({f'Face_{num+1}': i['box'], 'Confidence': round(i['confidence'], 4), 'Emotion': i['emotion']} for num, i in enumerate(results))
