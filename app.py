from flask import Flask, render_template


app = Flask(__name__, template_folder='templates')

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/Sign_Up', methods=['GET', 'POST'])
def sign_up():
    return render_template('signup.html')

@app.route('/Profile')
def profile():
    return render_template('Profile.html')

@app.route('/Create_List')
def create_list():
    return render_template('createlist.html')

app.debug = True

if __name__ == '__main__':
    app.run()

