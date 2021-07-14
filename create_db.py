from webapp.catalogs import create_app
from grinding_converter.webapp import create_db


create_db.create_all(app=create_app())