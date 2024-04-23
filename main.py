from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
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


# class Reg(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(1000))
#     e_mail = db.Column(db.String(1000)
#     pasw = db.Column(db.Integer)


@app.route('/')
def index():
    items = Item.query.order_by[Item.price].all()
    return render_template('index.html', data=items)


@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        price = request.form['price']
        txt = request.form['txt']
        itrm = Item(title=title, price=price, txt=txt)
        try:
            db.session.add(itrm)
            db.session.commit()
            return redirect('/')
        except:
            'Error'
    else:
        return render_template('create.html')


@app.route('/reg')
def reg():
    return render_template('reg.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
