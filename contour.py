import cv2

# read image and pre-processing
image = cv2.imread("./crescent.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.medianBlur(gray, 5)
edges = cv2.Canny(blurred, 100, 200)
cv2.imshow("edges detection", edges)
_, binary = cv2.threshold(edges, 127, 255, 0)
w, h, c = image.shape

# contours detection
_, contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
res = cv2.imread("./blank.png")
res = cv2.resize(res, (h, w))

print(len(contours))
for i in range(len(contours)):
    area = cv2.contourArea(contours[i])
    perimeter = cv2.arcLength(contours[i], True)
    print('area=', area, 'perimeter', perimeter)

# plot contours
cv2.drawContours(res, contours, -1, (0, 0, 0), 3)
cv2.imshow("contours", res)
cv2.waitKey(0)
