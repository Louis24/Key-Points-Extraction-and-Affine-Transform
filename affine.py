import cv2
import numpy as np

image = cv2.imread("./crescent.png")

corners = np.float32([[667, 321], [817, 372], [594, 556], [764, 616]])
# the coordinates might have some problem should be 856 according to the MM_favefit_card_design_02.pdf
canvas = np.float32([[0, 0], [540, 0], [0, 750], [540, 750]])


M = cv2.getPerspectiveTransform(corners, canvas)
result = cv2.warpPerspective(image, M, (0, 0))

cv2.imshow("res", result)
cv2.waitKey(0)
