import cv2

print("\tworking on open-cv\n\t----------------------\n\t1.original image\n\t2.BGR2GRAY\n\t3.BGR2RGB\n\t4.BGR2HSV\n\t5.image transformation\n\t6.flip image\n\t7.Add two image\n\t8.subtract two image\n\t9.image tresholding\n\t10.drawing on image\n\t11.stop running the program")

def display(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

while True:
    choice=int(input("Enter your choice:"))

                                     
    if choice==1:
        usr=input("enter the path of the image:")
        img=cv2.imread(usr)
        display("original image",img)
        
    elif choice==2:
        usr=input("enter the path of the image:")
        img=cv2.imread(usr)
        gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        display("GRAY image",gray)
        
    elif choice==3:
        usr=input("enter the path of the image:")
        img=cv2.imread(usr)
        RGB= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        display("RGB image",RGB)
        
    elif choice==4:
        usr=input("enter the path of the image:")
        img=cv2.imread(usr)
        HSV= cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        display("HSV image",HSV)
        
    elif choice==5:
        usr=input("enter the path of the image:")
        img=cv2.imread(usr)
        angle=int(input("Enter rotation angle: "))
        if angle==90:
            rotate=cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
        elif angle==180:
            rotate=cv2.rotate(img,cv2.ROTATE_180)
        else:
            rotate=cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)
        display("rotated image",rotate)
        
 
    elif choice==6:
        usr=input("enter the path of the image:")
        img=cv2.imread(usr)
        typ=int(input("enter how to rotate(1.vertical|2.horizontal|3.horizontalvertical:"))
        if typ==1:
            flipped=cv2.flip(img,0)
        if typ==2:
            flipped=cv2.flip(img,1)
        if typ==3:
            flipped=cv2.flip(img,-1)
        display("flipped image",flipped)

    if choice==7:
        usr1=input("enter the path of the image1:")
        usr2=input("enter the path of the image2:")
        img=cv2.imread(usr1)
        img1=cv2.imread(usr2)
        add=cv2.add(img,img1)
        display("added image",add)
        

    if choice==8:
        usr1=input("enter the path of the image1:")
        usr2=input("enter the path of the image2:")
        img=cv2.imread(usr1)
        img1=cv2.imread(usr2)
        sub=cv2.subtract(img,img1)
        display("subtracted image",sub)
        
    if choice==9:
        usr=input("enter the path of the image:")
        img=cv2.imread(usr)
        gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        thresh=int(input("enter threshold value"))
        _, threshimg=cv2.threshold(gray,thresh,255,cv2.THRESH_BINARY)
        display("GRAY image",threshimg)
        

    if choice==10:
        usr=input("enter the path of the image:")
        img=cv2.imread(usr)
        
        inp=int(input("enter the shape to draw(1.line,2.rectangle,3.circle):: "))
        if inp==1:
            x1=int(input("initial position at x-axis:"))
            y1=int(input("initial position at y-axis:"))
            x2=int(input("final position at x-axis:"))
            y2=int(input("final position at y-axis:"))
            thick=int(input("enter thickness:"))
            line=cv2.line(img,(x1,y1),(x2,y2),(255,0,0),thickness=thick)
            display("line in image",line)
        if inp==2:
            x1=int(input("initial position at x-axis:"))
            y1=int(input("initial position at y-axis:"))
            x2=int(input("final position at x-axis:"))
            y2=int(input("final position at y-axis:"))
            thick=int(input("enter thickness:"))
            rec=cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,0),thickness=thick)
            display("rectangle in image",rec)
        if inp==3:
            x =int(input("enter centre point in x axis:"))
            y =int(input("enter centre point in y axis:"))
            radius =int(input("enter radius of the circle:"))
            thickness =int(input("enter thickness:"))
            circ = cv2.circle(img,(x,y), radius,(255,0,0), thickness=thickness)
            display("circle in image",circ)


    elif choice==11:
        break






























    
