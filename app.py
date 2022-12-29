from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    
    list = ["0","1","2","3","4","5","6","7","8","9"]
    dictionary={"好きなゲーム":"valorant","好きな食べ物":"モンブラン","好きな場所":"家"}
    judge =True
    return render_template('index.html',list=list,dictionary=dictionary,judge=judge)


if __name__ == "__main__":
    app.run(port=8080)