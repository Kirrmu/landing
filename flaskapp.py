from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__, static_folder="static", template_folder="templates")

# Configure Flask-Mail settings for Gmail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'sike2579@gmail.com'  # Your Gmail email address
app.config['MAIL_PASSWORD'] = 'vuukyvdwhvadzrqj'  # Your Gmail password

mail = Mail(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/law")
def law():
    return render_template("law.html")


@app.route("/contact")
def contact():
    return render_template("contactus.html")


@app.route("/submit", methods=['POST'])
def submit():
    if request.method == "POST":
        first_name = request.form['FirstName']
        last_name = request.form['LastName']
        email = request.form['Email']
        phone = request.form['Phone']
        message = request.form['Message']

        # Send email using Flask-Mail
        msg = Message('New Contact Form Submission',
                      sender=email,  # Your Gmail email address
                      recipients=['sike2579@gmail.com'])  # Recipient's email address
        msg.body = f"First Name: {first_name}\nLast Name: {last_name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
        mail.send(msg)

        success_message = "Thank you for your submission! We'll be in touch."
        return render_template("contactus.html", success_message=success_message)


if __name__ == "__main__":
    app.run(debug=True)
