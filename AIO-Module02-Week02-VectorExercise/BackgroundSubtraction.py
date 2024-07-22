import numpy as np
import cv2

bg1_img = cv2.imread('AIO-Homework/AIO-Module02-Week02-VectorExercise/Picture/GreenBackground.png')
ob_img = cv2.imread('AIO-Homework/AIO-Module02-Week02-VectorExercise/Picture/Object.png')
bg2_img = cv2.imread('AIO-Homework/AIO-Module02-Week02-VectorExercise/Picture/NewBackground.jpg')

IMAGE_SIZE = (678, 381)

bg1_img = cv2.resize(bg1_img, IMAGE_SIZE)
ob_img = cv2.resize(ob_img, IMAGE_SIZE)
bg2_img = cv2.resize(bg2_img, IMAGE_SIZE)

def compute_difference(bg_img, input_img):
    difference_three_channel = cv2.absdiff(bg_img, input_img)
    difference_single_channel = np.sum(difference_three_channel, axis=2) / 3.0
    difference_single_channel = difference_single_channel.astype('uint8')

    return difference_single_channel

difference_single_channel = compute_difference(bg1_img, ob_img)

def compute_binary_mask(difference_single_channel):
    difference_binary = np.where(difference_single_channel >= 15, 255, 0)
    difference_binary = np.stack([difference_binary]*3, axis=-1)
    return difference_binary

binary_mask = compute_binary_mask(difference_single_channel)

def replace_background(bg1_img, bg2_img, ob_img):
    difference_single_channel = compute_difference(bg1_img, ob_img)
    binary_mask = compute_binary_mask(difference_single_channel)

    ouput = np.where(binary_mask==255, ob_img, bg2_img)
    return ouput

result = replace_background(bg1_img, bg2_img, ob_img)
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()