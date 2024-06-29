from flask import Flask, render_template, request, redirect, url_for, flash,send_file,session

app = Flask(__name__, static_url_path='/static')
app.secret_key = 'your_secret_key'

# Routes

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/single')
def single():
    return render_template('single-post.html')

@app.route('/about-us')
def about():
    return render_template('about-us.html')

@app.route('/services')
def services():
    return render_template('base.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/certificate')
def elements():
    return render_template('elements.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')


#https://website-port.onrender.com/
@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/singledetails')
def single_blog():
    return render_template('single-blog.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        flash('Contact message submitted successfully!', 'success')
        return redirect(url_for('thank_you'))

    return render_template('contact.html')

@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')

@app.route('/admin')
def admin():
    flash('Unauthorized! Please login first.', 'danger')
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'ratheesh' and password == '123':
            session['logged_in'] = True
            flash('Login successful!', 'success')
            return redirect(url_for('admin'))
        else:
            flash('Invalid username or password. Please try again.', 'danger')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/download_resume')
def download_resume():
    resume_path = 'static/Ratheesh.R..pdf'
    return send_file(resume_path, as_attachment=True)

@app.route('/python_project')
def python_project():
    return render_template('python_project.html')

@app.route('/ml_project')
def ml_project():
    return render_template('ml_project.html')

@app.route('/mini_project')
def mini_project():
    return render_template('mini_project.html')

@app.route('/web_project')
def web_project():
    return render_template('web_project.html')



if __name__ == '__main__':
    app.run(debug=True)
