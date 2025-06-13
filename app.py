from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    flag = "flag{SSTI_sagano_high_school}"
    result = ""

    if request.method == "POST":
        name = request.form.get("name", "")
        # 脆弱なテンプレート処理（SSTI）
        template = f"Hello {name}!"
        result = render_template_string(template, flag=flag)

    # 入力フォームのHTMLテンプレート
    html = """
        <h1>What is your name?</h1>
        <form method="POST">
            <input type="text" name="name" placeholder="Your name or payload">
            <input type="submit" value="Submit">
        </form>
        <p>{{ result|safe }}</p>
    """
    return render_template_string(html, result=result)

if __name__ == "__main__":
    app.run(debug=True)
