from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        page_title = "Конвертер помола"
        grinders_name = {"Mahlkönig Tanzania Диск 0-9",
                        "Mahlkönig Tanzania Диск 3-15",
                        "Mahlkönig EK43 (turkish) Диск 1-11"}
        grind_sizes = {4, 4.5, 6}
        return render_template('index.html', page_title=page_title,
                               grinders_name=grinders_name,
                               grind_sizes=grind_sizes)

    return app