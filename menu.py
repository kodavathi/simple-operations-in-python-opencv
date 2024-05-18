import cv2

print("\tworking on open-cv\n\t----------------------\n\t1.original image\n\t2.BGR2GRAY\n\t3.BGR2RGB\n\t4.BGR2HSV\n\t5.image transformation\n\t6.flip image\n\t7.Add two image\n\t8.subtract two image\n\t9.image tresholding\n\t10.drawing on image\n\t11.stop running the program")
while True:
    choice=int(input("Enter your choice:"))

                                     
    if choice==1:
        img=cv2.imread("C:/Users/ADMIN/Desktop/th (1).jpeg")
        cv2.imshow("original image",img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif choice==2:
        img=cv2.imread("C:/Users/ADMIN/Desktop/th (1).jpeg")
        gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imshow("GRAY image",gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif choice==3: 
        img=cv2.imread("C:/Users/ADMIN/Desktop/th (1).jpeg")
        RGB= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        cv2.imshow("RGB image",RGB)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif choice==4:
        img=cv2.imread("C:/Users/ADMIN/Desktop/th (1).jpeg")
        HSV= cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        cv2.imshow("HSV image",HSV)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
 
    elif choice==5:
        img=cv2.imread("C:/Users/ADMIN/Desktop/th (1).jpeg")
        angle=int(input("Enter rotation angle: "))
        if angle==90:
            rotate=cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
        elif angle==180:
            rotate=cv2.rotate(img,cv2.ROTATE_180)
        else:
            rotate=cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)
        cv2.imshow("rotated image",rotate)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
 
    elif choice==6:
        img=cv2.imread("C:/Users/ADMIN/Desktop/th (1).jpeg")
        typ=int(input("enter how to rotate(1.vertical|2.horizontal|3.horizontalvertical:"))
        if typ==1:
            flipped=cv2.flip(img,0)
        if typ==2:
            flipped=cv2.flip(img,1)
        if typ==3:
            flipped=cv2.flip(img,-1)
        cv2.imshow("flipped image",flipped)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    if choice==7:
        img=cv2.imread("C:/Users/ADMIN/Desktop/th (1).jpeg")
        img1=cv2.imread("C:/Users/ADMIN/Desktop/th.jpeg")
        add=cv2.add(img,img1)
        cv2.imshow("added image",add)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    if choice==8:
        img=cv2.imread("C:/Users/ADMIN/Desktop/th (1).jpeg")
        img1=cv2.imread("C:/Users/ADMIN/Desktop/th.jpeg")
        sub=cv2.subtract(img,img1)
        cv2.imshow("subtracted image",sub)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    if choice==9:
        img=cv2.imread("C:/Users/ADMIN/Desktop/th (1).jpeg")
        gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        thresh=int(input("enter threshold value"))
        _, threshimg=cv2.threshold(gray,thresh,255,cv2.THRESH_BINARY)
        cv2.imshow("GRAY image",threshimg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


    if choice==10:
        img=cv2.imread("C:/Users/ADMIN/Desktop/th (1).jpeg")
        print(img.shape)
        inp=int(input("enter the shape to draw(1.line,2.rectangle,3.circle):: "))
        if inp==1:
            line=cv2.line(img,(50,25),(100,75),(255,0,0),thickness=2)
            cv2.imshow("line in image",line)
        if inp==2:
            rec=cv2.rectangle(img,(50,25),(100,75),(255,0,0),thickness=2)
            cv2.imshow("rectangle in image",rec)
        if inp==3:
            circ=cv2.circle(img,(50,25),50,(255,0,0),thickness=2)
            cv2.imshow("circle in image",circ)


    elif choice==11:
        break
























    
