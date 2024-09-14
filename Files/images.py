import cv2
image = cv2.imread('bmw1.jpg') 
if image is None:
    print("There is no Image!")
else:
    cv2.imshow('Image is loaded!', image)
    cv2.waitKey(0)  
    cv2.destroyAllWindows()  
