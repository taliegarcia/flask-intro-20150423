from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Home Page</title>
        </head>
        <body>
            <h3>Hi! This is the home page.</h3>
            <a href="/hello">Go to Hello page</a>
        </body>
    </html>
    """

# route to display a simple web page
@app.route('/hello')
def say_hello():
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Hi There!</title>
        </head>
        <body>
            <h1>Hi There!</h1>
            <form action="/greet">
                <label>What's your name? <input type="text" name="person"></label>
                    <br>
                <label>Choose Compliment:
                    <br>
                    <input type="radio" name="compliment" value="awesome">awesome
                    <br>              
                    <input type="radio" name="compliment" value="terrific">terrific
                    <br>
                    <input type="radio" name="compliment" value="fantastic">fantastic
                    <br>
                    <input type="radio" name="compliment" value="neato">neato
                    <br>
                    <input type="radio" name="compliment" value="fantabulous">fantabulous
                    <br>
                    <input type="radio" name="compliment" value="wowza">wowza
                    <br>
                    <input type="radio" name="compliment" value="oh-so-not-meh">oh-so-not-meh
                    <br>
                    <input type="radio" name="compliment" value="brilliant">brilliant
                    <br>
                    <input type="radio" name="compliment" value="ducky">ducky
                    <br>
                    <input type="radio" name="compliment" value="coolio">coolio
                    <br>
                    <input type="radio" name="compliment" value="incredible">incredible
                    <br>
                    <input type="radio" name="compliment" value="wonderful">wonderful
                    <br>
                    <input type="radio" name="compliment" value="smashing">smashing
                    <br>
                    <input type="radio" name="compliment" value="lovely">lovely
                </label>
                    <br>
                <input type="submit">

            </form>
        </body>
    </html>

    """

@app.route('/greet')
def greet_person():
    player = request.args.get("person")

    # AWESOMENESS = [
    #     'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    #     'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

    compliment = request.args.get("compliment")

    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>A Compliment</title>
        </head>
        <body>
            Hi %s I think you're %s!
        </body>
    </html>""" % (player, compliment)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
