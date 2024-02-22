from flask import Flask,render_template,url_for,request,redirect
import csv
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template('page_name')

@app.route('/thank_you' )
def tanks_page():
    return render_template('thank_you.html')

def write_to_file(data):
     with open ('database.txt' , mode='a') as database:
          email= data["email"] 
          name = data["name"] 
          subjetc = data["subject"] 
          message = data["message"] 
          file = database.write(f'\nnome:{name},email:{email},assunto:{subjetc}, mensagem:{message}')

def write_to_csv(data):
     with open ('database.csv' ,  mode='a') as database2:
          email= data["email"] 
          name = data["name"] 
          subjetc = data["subject"] 
          message = data["message"] 
          csv_writer = csv.writer(database2,delimiter= ',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
          csv_writer.writerow([name,email,subjetc,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
         if request.method == 'POST':
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thank_you')
         else:
              return 'something went wrong, please Try Again!'


if __name__ == '__main__':
    app.run()
    