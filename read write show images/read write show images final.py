import cv2
# import image to img
img = cv2.imread('lena.jpg', 1)
#show image and the name of image will be 123
cv2.imshow('123',img)
#print image in 3d array
print(img)
# wait for 5s
# cv2.waitKey(5000)
k = cv2.waitKey(0)
if k == 27:
	# Destroy all windows
	print('hello')
	cv2.destroyAllWindows()
# if the input word is "s" then the file will be saved with a new file name new_lena
elif k == ord('s'):

	cv2.imwrite('new_lena.png',img)
else :
	print('bye')





# create a new png file
#cv2.imwrite('lena_copy.png',img)