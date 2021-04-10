
from flask_wtf import FlaskForm
from wtforms import TextAreaField
from flask_wtf.file import FileField, FileAllowed, FileRequired 
from wtforms.validators import DataRequired


class UploadForm(FlaskForm):
    description = TextAreaField('Description', validators=[DataRequired()])
    image = FileField('Image', validators=[
        FileRequired(),
        FileAllowed(['jpg','png','jpeg'], 'Images only')
    ])