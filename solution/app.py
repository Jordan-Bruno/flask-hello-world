from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return 'This is the about page.'

@app.route('/html')
def html_page():
    return '<h1>Hello with HTML!</h1><p>This is a paragraph with HTML tags.</p>'

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post ID is {post_id}'

if __name__ == '__main__':
    app.run(debug=True)
