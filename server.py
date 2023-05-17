from flask import Flask, render_template, request
import requests
import json
from forms import ContactForm

app = Flask(__name__)

@app.route('/')
def home():
    blog_url = "https://api.npoint.io/f2377440887cd2f720a1"
    blog_response = requests.get(url=blog_url)
    blog_data = blog_response.json()
    return render_template('index.html', posts=blog_data)


@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    blog_url = "https://api.npoint.io/f2377440887cd2f720a1"
    blog_response = requests.get(url=blog_url)
    blog_data = blog_response.json()
    for blog_post in blog_data:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/work')
def work():
    return render_template('work.html')


@app.route('/band')
def band():
    return render_template('band.html')


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == 'POST':
        data = request.form
        name = data['name']
        email = data['email']
        phone = data['phone']
        message = data['message']
        print(data['name'])
        print(data['email'])
        print(data['phone'])
        print(data['message'])
        form = ContactForm(name, email, phone, message)
        form.fill_form()
        return render_template('contact.html', submit=True)
    else:
        return render_template('contact.html', submit=False)


@app.route('/index')
def index():
    blog_url = "https://api.npoint.io/f2377440887cd2f720a1"
    blog_response = requests.get(url=blog_url)
    blog_data = blog_response.json()
    return render_template('index.html', posts=blog_data)


if __name__ == "__main__":
    app.run(debug=True)
