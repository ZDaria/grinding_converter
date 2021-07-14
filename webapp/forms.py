from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField



class GrindConverterForm(FlaskForm):
    grinders_name = ["Mahlkönig Tanzania Диск 0-9",
                     "Mahlkönig Tanzania Диск 3-15",
                     "Mahlkönig EK43 (turkish) Диск 1-11"]
    grind_sizes = [4, 4.5, 6]

    grinder_from = SelectField("Наименование кофемолки",
                                       choices=grinders_name,
                                       render_kw={"class": "form-control"})

    grind_size = SelectField("Помол", choices=grind_sizes,
                                     render_kw={"class": "form-control"})

    grinder_to = SelectField("В помол какой кофемолки конвертируем",
                             choices=grinders_name,
                             render_kw={"class": "form-control"})

    grind_size_result = SubmitField("Помол", render_kw={"class": "form-control"})

    submit = SubmitField("Отправить", render_kw={"class": "btn btn-primary"})
