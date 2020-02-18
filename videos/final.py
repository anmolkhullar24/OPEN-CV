import cv2



# if the file or object is open then cap.isOpened()  {for the file} will be true otherwise it will be false

cap = cv2.VideoCapture(0)





# its the codec

fourcc = cv2.VideoWriter_fourcc(*'XVID')





# fourcc codes for codec and 20.0 is number of frames per second and fourth argument is size

out = cv2.VideoWriter('output.avi',fourcc, 20.0 , (640,480) )

while (True):

 #in ret will be boolean ( ie True or false) and the frame will be stored in frame

 ret, frame = cap.read()





 # Prints the frame width

 print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

 print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))







 # if the return value is false then it will print sorry

 if ret == True :

  #saves the video on disk

  out.write(frame)





  #convert the images to gray color

  #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

  #show the gray color images (videos) on the screen

  ##cv2.imshow('Name',gray)

  # Shows the coloured images on the screen

  cv2.imshow("Frame",frame)





  # wait for 1 milli second

  k = cv2.waitKey(1)





  # if the input is esc or q then the program will continue

  if k == ord('q') or k == 27:

   break





# release the camera resource

cap.release()





# release video writer resource

out.release()





# close the window

cv2.destroyAllWindows()