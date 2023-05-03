from flask import Flask, render_template
app = Flask(__name__) #creates the Flask application instance, __name__ tells flask to use current Python module as the app name


@app.route("/") #defining the route for the root path/homepage
def home(): #executed when the user navigates to the path defined above, rendering the home.html
    return render_template("home.html")


@app.route("/about") #defines about route
def about(): #executed when the user navigates to /about, rendering the about.html
    return render_template("about.html")


if __name__ == "__main__": #
    app.run(debug=True) #starts the app in debug mode