from flask_wtf import FlaskForm
import wtforms


class MerchForm(FlaskForm):
    name = wtforms.StringField("Введіть своє ім'я")
    merches = wtforms.SelectMultipleField("Виберіть мерч")
    submit = wtforms.SubmitField("Купити")


class ReviewForm(FlaskForm):
    name = wtforms.StringField("Введіть своє ім'я")
    grades = wtforms.SelectField("Виберіть оцінку")
    review = wtforms.TextAreaField("Напишіть свій відгук")
    submit = wtforms.SubmitField("Відправити відгук")