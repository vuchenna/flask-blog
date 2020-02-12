from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class PostForm(FlaskForm):
    first_name = StringField('First Name',
            validators=[
                Datarequired(),
                Length(min=4, max=30)
                ]
            )
    last_name = StringField('Last Name',
            validators=[
                DataRequired(),
                Length(min=4, max=30)
            ]
        )
    title = StringField('Title',
            validators=[
                DataRequired(),
                Length(min=4, max=100)
            ]
        )
    content = StringField('Content', 
            validators=[
                DataRequired(),
                Length(min=50, max=1000)
            ]
        )

    submit = SubmitField('Submit')


