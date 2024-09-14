import cv2
image = cv2.imread('../Images/sample.jpg') 
if image is None:
    print("Error: Could not load image.")
else:
    cv2.imshow('Loaded Image', image)
    cv2.waitKey(0)  
    cv2.destroyAllWindows()  
