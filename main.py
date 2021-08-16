from flask import Flask,render_template,request
from flask_cors import cross_origin
from detection import SSDmobileNet, predict, Decode

#######################
ssd = SSDmobileNet()
net = ssd.network()
label = ssd.classNames()
##########################

app = Flask(__name__)

@app.route('/',methods=['GET'])
@cross_origin()
def index():
    return render_template('index.html')

@app.route('/result',methods=['GET','POST'])
@cross_origin()
def result():
    if request.method == 'POST':
        image = request.json['image']
        img = Decode(image).copy()
        #img = cv2.resize(img, (480, 320))
        res = predict(net, label, img)
        #print(res)
        return render_template('index.html')
    return render_template('index.html')



if __name__=="__main__":
    app.run(host="0.0.0.0",port="8888")

# Author: Swati Sinha & Maitry Sinha
# Date : 13-08-2021