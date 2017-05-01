from flask import Flask, redirect, url_for, request
import gui

from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.route('/success/<result>')
def success(result):
   return 'welcome %s' % result

@app.route('/check',methods = ['POST', 'GET', 'OPTIONS'])
def hello_world():
   if request.method == 'POST':
      url = request.form['yoyo'] #Save
      return gui.detect(url)#redirect(url_for('success',result = "url"))
   # else:
   #    user = request.args.get('input')
   #    return url#gui.detect(url)
      #Mera command nhi chal rha , yeh upar waala comment karn
      #return "working"
      #return json.dumps({'success':True,'data':'working'}), 500, {'ContentType':'application/json'}
#cors?

      #return "working"


if __name__ == '__main__':
	app.debug=True
	app.run(debug= True)