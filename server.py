from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'



@app.route('/')
def main():
    if 'random' not in session:
        session["random"] = random.randint(1,100)
    number = session["random"]
    if 'guess' not in session:
        session["guess"] = 0
    if 'guessCount' not in session or session["guessCount"] > 6:
        session["guessCount"] = 0
    guess = session["guess"]
    return render_template("index.html", low = low , high = high, number = number, correct = correct, guess = guess, fail = fail)

low = '<div class="container red mb-3"><h2>Too Low!</h2></div>'
high = '<div class="container red mb-3"><h2>Too High!</h2></div>'
correct = '<div class="container green mb-3"><h2>You guessed Correct!!</h2></div>'
fail = '<div class="container fail mb-3"><h2>You fail me!!</h2><form action="/gg" ><input type="submit" name="submit" value="Play Again" class="ms-2"></form></div>'

@app.route('/guess', methods=["POST"])
def guessing():
    if request.form["number"] == "":
        pass
    else:
        session["guess"] = int(request.form["number"])
        session["guessCount"] = session["guessCount"] + 1
    return redirect("/")

@app.route('/gg')
def gg():
    session.clear()
    return redirect("/")


if __name__=="__main__":
    app.run(debug=True)
