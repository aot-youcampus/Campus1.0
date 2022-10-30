from PIL import Image 
import math  
# Import an image from directory: 

main_image = Image.open("E:/image.jpg") 
# Extracting pixel map: 
main_image.show()

pixel_map = main_image.load()
# Extracting the width and height of the image: 

width, height = main_image.size
w=[]
for i in range(width):
    w.append(i)
h=[]
for i in range(height):
    h.append(i)

d=[]
k=0
for i in range(width): 
    c=[]
    k=[]
    for j in range(height): 

        # getting the RGB pixel value. 
        r, g, b= main_image.getpixel((i, j))
        c.append(r)
        c.append(g)
        c.append(b)
        k.append(c)
    d.append(k)
#print(len(d))
meu=float(input("Enter the value of key 1, give value between 3.5 and 4:     "))
while(meu<=3.5 or meu>4):
    meu=float(input("You entered wrong key enter value between 3.5 and 4:   "))
meu1=float(input("Enter the value of key 2, give value between 3.5 and 4:     "))
while(meu1<=3.5 or meu1>4):
    meu1=float(input("You entered wrong key enter value between 3.5 and 4:   "))
x=float(input("Enter the value of key 3, give value greater than 0 and less than 1:     "))
while(x<0 or x>1):
    x=float("Entered wrong value enter greater than 0 and less than 1:    ")
x1=float(input("Enter the value of key 4, give value greater than 0 and less than 1:     "))
while(x<0 or x>1):
    x1=float("Entered wrong value enter greater than 0 and less than 1:    ")
c=[]
for i in range(width):
    xn=meu*x*(1-x)
    c.append(xn)
    x=xn

#storing meu2 and xf for DNA cryptography
meu2=meu
xf=x1
c1=[]
for i in range(height):
    xn=meu1*x1*(1-x1)
    c1.append(xn)
    x1=xn
#print(len(c),len(c1))
#setting the rows with the help of logistic map array created in c
for i in range(len(w)):
    m=i
    for j in range(i+1,len(w)):
        if(c[m]<c[j]):
            m=j
    c[i],c[m]=c[m],c[i]
    w[i],w[m]=w[m],w[i]


#setting the coloumn with the use of array c1
for i in range(len(h)):
    m=i
    for j in range(i+1,len(h)):
        if(c1[m]<c1[j]):
            m=j
    c1[i],c1[m]=c1[m],c1[i]
    h[i],h[m]=h[m],h[i]
    
p=[]
for i in w: 
    for j in h: 

        # getting the RGB pixel value. 

        r, g, b= main_image.getpixel((i, j))
        p.append(r)
        p.append(g)
        p.append(b)
count=0
for i in range(len(w)):
    for j in range(len(h)):
        r=p[count]
        g=p[count+1]
        b=p[count+2]
        count=count+3
        pixel_map[i,j]=(r,g,b)
 
  
main_image.save("E:/encryptedIMGnew11.png", format="png") 
#main_image.show()

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

main_image = Image.open("E:/encryptedIMGnew11.png") 
  
# Extracting pixel map: 

pixel_map = main_image.load()
# Extracting the width and height of the image: 

width, height = main_image.size 

meu2=meu
xf=x1
c=[]
for i in range(width): 
    for j in range(height): 

        # getting the RGB pixel value. 

        r, g, b= main_image.getpixel((i, j))
        c1=r
        c2=g
        c3=b
        c.append(c1)
        c.append(c2)
        c.append(c3)
#storing the pixels value in binary form in d array
d=[]
for a in c:
    b=bin(a).replace('0b', '')
    while(len(b)<8):
        b='0'+b
    d.append(b)

#Alloting the 2-bit binary a letter by the key given by user
choice=int(input("Enter the key 5, value should be between 1-8:  "))
while(choice>8 or choice==0):
    choice=int(input("You entered wrong key enter between 1-8:   "))
print()
print("All your keys are accepted!!")

st=[]
if(choice==1):
    for i in d:
        for j in range(0,8,2):
            tmp=i[j:j+2]
            if(tmp=='00'):
                st.append('A')
            elif(tmp=='11'):
                st.append('T')
            elif(tmp=='01'):
                st.append('C')
            elif(tmp=='10'):
                st.append('G')
elif(choice==2):
    for i in d:
        for j in range(0,8,2):
            tmp=i[j:j+2]
            if(tmp=='00'):
                st.append('A')
            elif(tmp=='01'):
                st.append('G')
            elif(tmp=='10'):
                st.append('C')
            elif(tmp=='11'):
                st.append('T')
elif(choice==3):
    for i in d:
        for j in range(0,8,2):
            tmp=i[j:j+2]
            if(tmp=='00'):
                st.append('C')
            elif(tmp=='01'):
                st.append('A')
            elif(tmp=='10'):
                st.append('T')
            elif(tmp=='11'):
                st.append('G')
elif(choice==4):
    for i in d:
        for j in range(0,8,2):
            tmp=i[j:j+2]
            if(tmp=='00'):
                st.append('C')
            elif(tmp=='01'):
                st.append('T')
            elif(tmp=='10'):
                st.append('A')
            elif(tmp=='11'):
                st.append('G')        
elif(choice==5):
    for i in d:
        for j in range(0,8,2):
            tmp=i[j:j+2]
            if(tmp=='00'):
                st.append('G')
            elif(tmp=='01'):
                st.append('A')
            elif(tmp=='10'):
                st.append('T')
            elif(tmp=='11'):
                st.append('C')
elif(choice==6):
    for i in d:
        for j in range(0,8,2):
            tmp=i[j:j+2]
            if(tmp=='00'):
                st.append('G')
            elif(tmp=='01'):
                st.append('T')
            elif(tmp=='10'):
                st.append('A')
            elif(tmp=='11'):
                st.append('C')
elif(choice==7):
    for i in d:
        for j in range(0,8,2):
            tmp=i[j:j+2]
            if(tmp=='00'):
                st.append('T')
            elif(tmp=='01'):
                st.append('C')
            elif(tmp=='10'):
                st.append('G')
            elif(tmp=='11'):
                st.append('A')
elif(choice==8):
    for i in d:
        for j in range(0,8,2):
            tmp=i[j:j+2]
            if(tmp=='00'):
                st.append('T')
            elif(tmp=='01'):
                st.append('G')
            elif(tmp=='10'):
                st.append('C')
            elif(tmp=='11'):
                st.append('A')

alot=[]
for i in range(16):
    s=bin(i).replace("0b","")
    x=s[::-1]
    while(len(x)<4):
        x=x+"0"
    s=x[::-1]
    alot.append(str(s))


tmp1=[]
for i in range(16):
    xn=meu2*(1-xf)
    tmp1.append(xf)
    xf=xn
for i in range(len(alot)):
    m=i
    for j in range(i+1,len(alot)):
        if(tmp1[m]<tmp1[j]):
            m=j
    tmp1[i],tmp1[m]=tmp1[m],tmp1[i]
    alot[i],alot[m]=alot[m],alot[i]
#print(alot)
c=[]
d=[]
tmp=[]
a=0
for i in range(0,len(st),4):
   c.append(st[i+1])
   c.append(st[i+2])
   d.append(st[i])
   d.append(st[i+3])
   if(c[a]=="A" and c[a+1]=="A"):
       tmp.append(alot[0])
   elif(c[a]=="A" and c[a+1]=="C"):
       tmp.append(alot[1])
   elif(c[a]=="A" and c[a+1]=="T"):
       tmp.append(alot[2])
   elif(c[a]=="A" and c[a+1]=="G"):
       tmp.append(alot[3])
   elif(c[a]=="C" and c[a+1]=="A"):
       tmp.append(alot[4])
   elif(c[a]=="C" and c[a+1]=="C"):
       tmp.append(alot[5])
   elif(c[a]=="C" and c[a+1]=="T"):
       tmp.append(alot[6])
   elif(c[a]=="C" and c[a+1]=="G"):
       tmp.append(alot[7]);
   elif(c[a]=="T" and c[a+1]=="A"):
       tmp.append(alot[8]);
   elif(c[a]=="T" and c[a+1]=="C"):
       tmp.append(alot[9]);
   elif(c[a]=="T" and c[a+1]=="T"):
       tmp.append(alot[10]);
   elif(c[a]=="T" and c[a+1]=="G"):
       tmp.append(alot[11]);
   elif(c[a]=="G" and c[a+1]=="A"):
       tmp.append(alot[12]);
   elif(c[a]=="G" and c[a+1]=="C"):
       tmp.append(alot[13]);
   elif(c[a]=="G" and c[a+1]=="T"):
       tmp.append(alot[14]);
   elif(c[a]=="G" and c[a+1]=="G"):
       tmp.append(alot[15]);
   c=[]
   if(d[a]=="A" and d[a+1]=="A"):
       tmp.append(alot[0])
   elif(d[a]=="A" and d[a+1]=="C"):
       tmp.append(alot[1])
   elif(d[a]=="A" and d[a+1]=="T"):
       tmp.append(alot[2])
   elif(d[a]=="A" and d[a+1]=="G"):
       tmp.append(alot[3])
   elif(d[a]=="C" and d[a+1]=="A"):
       tmp.append(alot[4])
   elif(d[a]=="C" and d[a+1]=="C"):
       tmp.append(alot[5])
   elif(d[a]=="C" and d[a+1]=="T"):
       tmp.append(alot[6])
   elif(d[a]=="C" and d[a+1]=="G"):
       tmp.append(alot[7]);
   elif(d[a]=="T" and d[a+1]=="A"):
       tmp.append(alot[8]);
   elif(d[a]=="T" and d[a+1]=="C"):
       tmp.append(alot[9]);
   elif(d[a]=="T" and d[a+1]=="T"):
       tmp.append(alot[10]);
   elif(d[a]=="T" and d[a+1]=="G"):
       tmp.append(alot[11]);
   elif(d[a]=="G" and d[a+1]=="A"):
       tmp.append(alot[12]);
   elif(d[a]=="G" and d[a+1]=="C"):
       tmp.append(alot[13]);
   elif(d[a]=="G" and d[a+1]=="T"):
       tmp.append(alot[14]);
   elif(d[a]=="G" and d[a+1]=="G"):
       tmp.append(alot[15]);
   d=[]

#converting the encoded binary into a character
m=[]
for i in range(0,len(tmp),2):
    s=tmp[i]+tmp[i+1]
    cal=0
    s=int(s)
    c=0
    while(s>0):
        d=s%10
        cal=cal+int(math.pow(2,c))*d
        s=s//10
        c=c+1
    m.append(cal)
count=0
for i in range(width): 
    for j in range(height): 

        # getting the RGB pixel value. 

        r=m[count]
        g=m[count+1]
        b=m[count+2]
        count=count+3
        pixel_map[i, j] = (int(r), int(g), int(b))
        #print(pixel_map[i,j])
main_image.save("E:/encryptedIMG.png", format="png") 
main_image.show()
print("ENCRYPTION DONE.. ♥☺☻")