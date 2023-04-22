from PIL import Image
import cv2

name = 'Narendra'
emp_id = '1234567'
desig = 'Chief Ministor'
dist = 'Visakhapatnam'
mandal = 'Gajuvaka'
scval = '54'

template = cv2.imread('template.png')
cv2.putText(template,name,(240,460),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0),1,cv2.LINE_AA)
cv2.putText(template,emp_id,(240,500),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0),1,cv2.LINE_AA)
cv2.putText(template,desig,(240,542),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0),1,cv2.LINE_AA)
cv2.putText(template,dist,(240,582),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0),1,cv2.LINE_AA)
cv2.putText(template,mandal,(240,622),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0),1,cv2.LINE_AA)
cv2.putText(template,scval,(240,662),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0),1,cv2.LINE_AA)
cv2.imwrite(f'{name}.png',template)
print("certificate generated successfully")

image_1 = Image.open(f'{name}.png')
im_1 = image_1.convert('RGB')
im_1.save(f'{name}.pdf')