import pickle, os

import cv2
import mediapipe as mp
import numpy as np

dir_path = os.path.dirname(os.path.realpath(__file__))
folder_path = os.path.join(dir_path)

kkb = {
    "Hammer": {"Scissor": "Win", "Hammer": "Draw", "Paper": "Lose"},
    "Paper": {"Scissor": "Lose", "Hammer": "Win", "Paper": "Draw"},
    "Scissor": {"Scissor": "Draw", "Hammer": "Lose", "Paper": "Win"}
}
def predict(img, model):  
    #pre-processing
    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles

    data_aux = []
    x_ = []
    y_ = []
    labels_dict = {0: 'Hammer', 1: 'Paper', 2: 'Scissor'}

    hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)
    
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    results = hands.process(img_rgb)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                img,  # image to draw
                hand_landmarks,  # model output
                mp_hands.HAND_CONNECTIONS,  # hand connections
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style())

        for hand_landmarks in results.multi_hand_landmarks:
            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y

                x_.append(x)
                y_.append(y)

            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y
                data_aux.append(x - min(x_))
                data_aux.append(y - min(y_))
    
    prediction = model.predict([np.asarray(data_aux)])

    predicted_character = labels_dict[int(prediction[0])]

    return predicted_character

def match_rersult(c1_img, c2_img):
    #load model
    model_dict = pickle.load(open(os.path.join(folder_path, 'model.p'), 'rb'))
    model = model_dict['model']
    try:
        c1_result = predict(c1_img, model)
    except:
        c1_result = None
    try:
        c2_result = predict(c2_img, model)
    except:
        c2_result = None
    print(c1_result, c2_result)
    if c1_result == None and c2_result:
        return "Lose", "Win"
    if c2_result == None and c1_result:
        return "Win", "Lose"
    if c2_result == None and c1_result == None:
        return "Draw", "Draw"
    return kkb[c1_result][c2_result], kkb[c2_result][c1_result]