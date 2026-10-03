from flask import Flask
import random


app = Flask(__name__)


@app.route("/")
def hello_world():
    facts = ["привет, меня зовут ангелина и мне 16 лет. <br> в этом блоге я расскажу пор <br> экзамены.",
    "flask помог мне создать этот сайт, открыв доступ к библиотеке.", 
    "с этого урока мне больше всего запомнилось подключение библиотеки."]
    return random.choice(facts)


app.run(debug=True)
