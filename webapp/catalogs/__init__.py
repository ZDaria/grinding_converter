from flask import Flask, render_template

#from .weather import weather_by_city
#from .python_org_news import get_python_news
import configparser

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")

    @app.route('/')
    def index():
        page_title = "Конвертер помолов"
        #weather = weather_by_city(webapp.config['WEATHER_SITY'])
        #news_list = get_python_news()
        #return render_template('index.html', page_title=page_title,
        #                      weather=weather, news_list=news_list)
    return app