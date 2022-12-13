from flask import Flask, render_template
import random
app = Flask(__name__)

images = [
	"https://media.tenor.com/fTTVgygGDh8AAAAC/kitty-cat-sandwich.gif",
	"https://media.tenor.com/w0Rv_cu3bJAAAAAC/kitty-cute.gif",
	"https://media.tenor.com/L4CcAh4ljlwAAAAd/good-night-cute.gif",
	"https://media.tenor.com/HYXVuDJDa0kAAAAd/kittykiss-little-kitty.gif",
	"https://media.tenor.com/217aKgnf16sAAAAC/kiss.gif",
	"https://media.tenor.com/B9WxfhMIYpIAAAAd/cats-hugs.gif",
	"https://media.tenor.com/dteyPLcdJJkAAAAC/cats-love.gif",
	"https://media.tenor.com/_XPaZI5cBQYAAAAd/cats-cat-love.gif",
	"https://media.tenor.com/PS9Tcg6mIY4AAAAd/cat-ayasan.gif",
	"https://media.tenor.com/2v1aDCelTJgAAAAC/cat-cats.gif"
]

@app.route('/')

def index():
	url = random.choice(images)
	return render_template('index.html', url = url)

if __name__ == "__main__":
	app.run(host="0.0.0.0")

