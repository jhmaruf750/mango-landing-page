from flask import Flask, render_template
from factory import PageFactory
from observer import Subject, Observer

app = Flask(__name__)

# Observer setup
subject = Subject()
observer = Observer()
subject.register(observer)

# Create dummy sections
sections = ["Hero", "Business Details", "Order System", "FAQs", "Feedback"]
for sec in sections:
    s = PageFactory.create_section(sec)
    subject.notify(s)

@app.route("/")
def home():
    return render_template("index.html", sections=sections)

if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(debug=True)
