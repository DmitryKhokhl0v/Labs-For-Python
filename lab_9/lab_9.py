from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1000), nullable=False)
    important = db.Column(db.Boolean, default=False)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        important = 'important' in request.form
        note = Note(text=text, important=important)
        db.session.add(note)
        db.session.commit()

    notes = Note.query.all()
    return render_template('index.html', notes=notes)

@app.route('/delete/<int:id>')
def delete(id):
    note = Note.query.get_or_404(id)
    db.session.delete(note)
    db.session.commit()
    return redirect('/')

@app.route('/delete-all')
def delete_all():
    db.session.query(Note).delete()
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=False)
