from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)

# Replace with your actual MongoDB connection string
app.config['MONGO_URI'] = "mongodb+srv://sanketpatil:<password>@cluster0.emfejl3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Connect to MongoDB
client = MongoClient(app.config['MONGO_URI'])
db = client['login']  # Specify the database name
collection = db['users']  # Specify the collection name

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get data from form
        name = request.form.get("uname")
        password = request.form.get("password")
        
        # Insert data into MongoDB
        if name and password:
            collection.insert_one({"name": name, "password": password})
        return redirect("/")
    
    # Retrieve all users from MongoDB
    users = list(collection.find({}))
    return render_template("index.html", users=users)


if __name__ == "__main__":
    app.run(debug=True)
