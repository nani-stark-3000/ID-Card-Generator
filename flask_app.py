from flask import Flask,render_template,request,make_response
from PIL import Image
import cv2
from matplotlib import pyplot

def id(name,emp_id,desig,dist,mandal,scval):
    template = cv2.imread('template.png')
    cv2.putText(template,name,(240,460),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0),1,cv2.LINE_AA)
    cv2.putText(template,emp_id,(240,500),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0),1,cv2.LINE_AA)
    cv2.putText(template,desig,(240,542),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0),1,cv2.LINE_AA)
    cv2.putText(template,dist,(240,582),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0),1,cv2.LINE_AA)
    cv2.putText(template,mandal,(240,622),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0),1,cv2.LINE_AA)
    cv2.putText(template,scval,(240,662),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0),1,cv2.LINE_AA)
    cv2.imwrite('static/id.png',template)
    pdf()

def pdf():
    image_1 = Image.open('static/id.png')
    im_1 = image_1.convert('RGB')
    im_1.save('static/id.pdf')

app = Flask(__name__,template_folder='template')

@app.route('/')

def _main_():
    return render_template("index.html")

@app.route('/details', methods=['POST','GET'])

def _id_():
    if request.method=='POST':
        name = request.form['user-name']
        emp_id = request.form['emp_id']
        desig = request.form['desig']
        dist = 'Visakhapatnam'
        mandal = request.form['mandal']
        scval = request.form['scval']
        id(name,emp_id,desig,dist,mandal,scval)
        return render_template('index.html',file=1)
    return render_template("index.html")

@app.route('/pdf',methods=['POST','GET'])

def _pdf_():
    if request.method=='POST':
        return render_template("index.html")
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True,port=34)
