from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(1000))
    price = db.Column(db.Integer)
    isActive = db.Column(db.Boolean, default=True)
    txt = db.Column(db.Text)

    def __repr__(self):
        return self.title, self.price, self.txt

class Reg(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
    e_mail = db.Column(db.String(1000))
    pasw = db.Column(db.Integer)




@app.route('/')
def index():
    # items = Item.query.order_by[Item.price].all()
    # return render_template('index.html', data=items)
    return render_template('index.html')

@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        price = request.form['price']
        txt = request.form['txt']
        item = Item(title=title, price=price, txt=txt)
        try:
            db.session.add(item)
            db.session.commit()
            return redirect('/')
        except:
            'Error'
    else:
        return render_template('create.html')


@app.route('/reg',  methods=['POST', 'GET'])
def reg():
    for value in db.session.query(Reg):
        print(value.name)
    if request.method == 'POST':
        name = request.form['name']
        e_mail = request.form['e_mail']
        pasw = request.form['pasw']
        user = Reg(name=name, e_mail=e_mail, pasw=pasw)
        try:
            db.session.add(user)
            db.session.commit()
            return redirect('/')
        except:
            'Error'
    else:
        return render_template('reg.html')

@app.route('/sign', methods = ['POST', 'GET'])
def sign():
    e_mails = []
    pasws = []
    for value in db.session.query(Reg):
        e_mails.append(value.name)
        pasws.append(value.pasw)
    if request.method == 'POST':
        e_mail = request.form['e_mail']
        pasw = request.form['pasw']

        try:
            if e_mail in e_mails and pasw in pasws:
                return redirect('/')
        except:
            'Error'
    else:
        return render_template('sign.html')
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()
