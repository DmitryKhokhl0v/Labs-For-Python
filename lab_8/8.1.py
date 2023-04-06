import cv2

img = cv2.imread('variant-1.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Original Image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
