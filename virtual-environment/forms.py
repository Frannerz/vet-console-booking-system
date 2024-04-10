from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DateField
from wtforms.validators import DataRequired

class PetForm(FlaskForm):
    OwnerId = IntegerField("Owner Id", validators=[DataRequired()])
    petName = StringField("Pet Name", validators=[DataRequired()])
    species = StringField("Species", validators=[DataRequired()])
    age = IntegerField("Age", validators=[DataRequired()])
    submit = SubmitField("Submit")