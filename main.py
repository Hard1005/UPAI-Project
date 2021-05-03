import cv2 as cv
import json


img1 = cv.imread("img1.jpeg")
img2 = cv.imread("img2.jpeg")


def draw(image , json_path):

    f = open(json_path, 'r')
    result = json.load(f)
    data = result['data']['output']['results'] 
    count = 0
    for box in data:
        if box['className'] == "car":
            bbox = box['bbox']
            count += 1
            s_x = bbox['xmin']
            s_y = bbox['ymin']
            e_x = bbox['xmax']
            e_y = bbox['ymax']
            image = cv.rectangle(image , (s_x , s_y) , (e_x , e_y) , (0,255,0),1)

    cv.imshow("result" , image)
    cv.waitKey(1000)
    return count




count1 = draw(img1 , "data1.json")
count2 = draw(img2 , "data2.json")

if count1 > count2:
    print("lane 1 is given more green light time")
else:
    print("lane 2 is given more green light time")