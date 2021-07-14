from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField, SelectField
from wtforms.validators import DataRequired


class GrindConverterForm(FlaskForm):
    grinders_name = [("Mahlkönig Tanzania Диск 0-9", "Mahlkönig Tanzania Диск 0-9"),
                     ("Mahlkönig Tanzania Диск 3-15", "Mahlkönig Tanzania Диск 3-15"),
                     ("Mahlkönig EK43 (turkish) Диск 1-11", "Mahlkönig EK43 (turkish) Диск 1-11")]
    grind_sizes = [4, 4.5, 6]
    # defaultfieldarguments, choices = [], coerce = unicode, option_widget = None
    grinder_from = SelectField("Наименование кофемолки",
                                       choices=grinders_name,
                                       render_kw={"class": "form-control"})

    grind_size = SelectField("Помол", choices=grind_sizes,
                                     render_kw={"class": "form-control"})

    grinder_to = SelectMultipleField("В помол какой кофемолки конвертируем",
                                     validators=[DataRequired()],
                                     choices=grinders_name,
                                     render_kw={"class": "form-control"})

    submit = SubmitField("Отправить", render_kw={"class": "btn btn-primary"})