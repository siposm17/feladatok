import data
import password_manager
from flask import Flask, render_template, redirect, url_for, request, session


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/")
def index():
    username = None
    if 'username' in session:
        username = session['username']
    return render_template('index.html', username=username)


@app.route('/login', methods=["GET", "POST"])
def login_page():
    if request.method == "POST":
        session['username'] = request.form['ID']
        password = request.form['password']
        if session['username'] in data.users.keys():
            if password_manager.verify_password(password, data.users[session['username']]):
                return redirect('/')
        is_login_invalid = True
        return render_template('login_page.html', is_login_invalid=is_login_invalid)
    return render_template('login_page.html')


@app.route('/test', methods=["GET", "POST"])
def test_page():
    if 'username' in session:
        number = session.get('number', 0)
        if request.method == "POST":
            if request.form['submit'] in ['Submit', 'Start quiz']:
                answer = request.form.get('answer', False)
                for index, question in enumerate(data.questions):
                    if number == len(data.questions):
                        if answer == 'True':
                            session['good_answer'] = session['good_answer'] + 1
                        session.pop('number', None)
                        return redirect(url_for('result_page'))
                    if index == number:
                        questions = data.questions[question]
                        session['number'] = index + 1
                        if answer == 'True':
                            session['good_answer'] = session['good_answer'] + 1
                        return render_template('test_page.html', questions=questions, question=question)
        session['good_answer'] = 0
        return render_template('test_page.html')
    else:
        return redirect('/')


@app.route('/result', methods=["GET", "POST"])
def result_page():
    if 'username' in session:
        good_answer = session['good_answer']
        return render_template('result_page.html', good_answer=good_answer)
    else:
        return redirect('/')


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
