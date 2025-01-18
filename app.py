from flask import Flask, render_template, request, redirect, url_for, flash
import random

app = Flask(__name__)
app.secret_key = "personal_key"

# List to store messages
messages = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        #Get the form data
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        #Check if the form data is empty
        if name == "" or email == "" or message == "":
            flash("Please fill the form correctly")
        else:
            flash("Your message has been sent successfully")

        # Save the message (replace this with a database in the future)
        messages.append({"name": name, "email": email, "message": message})
        
        # Show success message and redirect
        flash("Thank you for your message! I will get back to you soon.", "success")
        return redirect(url_for("home"))
    
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    # Placeholder for AI logic (expand this later with an AI model)
    preferences = request.form.get("preferences")

    # Sample project recommendations
    projects = [
        {"name": "AI Chatbot", "description": "A chatbot using natural language processing."},
        {"name": "Portfolio Website", "description": "A responsive personal website."},
        {"name": "E-commerce App", "description": "A Django-powered online store."}
    ]

    # Return a random recommendation for now
    recommended = random.choice(projects)
    return {
        "project_name": recommended["name"],
        "project_description": recommended["description"]
    }

if __name__ == "__main__":
    app.run(debug=True)
