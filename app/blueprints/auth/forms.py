from os import name
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField 
from wtforms.validators import Email, DataRequired, EqualTo, ValidationError
from .models import User
import random
from jinja2 import Markup
#flask_wsp, what's wrong? 


class LoginForm(FlaskForm): 
    email = StringField('Email Address', validators=[Email(), DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')

class RegisterForm(FlaskForm): 
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[Email(), DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Submit')

    #random numbers to generate random icon
    r1=random.randint(1,1000)
    r2=random.randint(1001,2000)
    r3=random.randint(2001,3000)
    r4=random.randint(3001,4000)
    r1_img= Markup(f'<img src = "https://avatars.dicebear.com/api/human/{r1}.svg" style="height:75px">')
    r2_img= Markup(f'<img src = "https://avatars.dicebear.com/api/human/{r2}.svg" style="height:75px">')
    r3_img= Markup(f'<img src = "https://avatars.dicebear.com/api/human/{r3}.svg" style="height:75px">')
    r4_img= Markup(f'<img src = "https://avatars.dicebear.com/api/human/{r4}.svg" style="height:75px">')

    icon = RadioField('Avatar', choices=[(r1,r1_img),(r2,r2_img),(r3,r3_img),(r4,r4_img)], validators=[DataRequired()])

    def validate_email(form, field):
        same_email_user = User.query.filter_by(email=field.data).first()
        if same_email_user:
            raise ValidationError("Email is Already in Use")

class EditProfileForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email Address', validators=[Email(),DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Submit')

    #random numbers to generate a random icon
    r1=random.randint(1,1000)
    r2=random.randint(1001,2000)
    r3=random.randint(2001,3000)
    r4=random.randint(3001,4000)
    r1_img=Markup(f'<img src="https://avatars.dicebear.com/api/bottts/{r1}.svg" style="height:75px">')
    r2_img=Markup(f'<img src="https://avatars.dicebear.com/api/bottts/{r2}.svg" style="height:75px">')
    r3_img=Markup(f'<img src="https://avatars.dicebear.com/api/bottts/{r3}.svg" style="height:75px">')
    r4_img=Markup(f'<img src="https://avatars.dicebear.com/api/bottts/{r4}.svg" style="height:75px">')

    icon = RadioField('Avatar', choices=[(9000,"Don't Change"),(r1,r1_img),(r2,r2_img),(r3,r3_img),(r4,r4_img)], validators=[DataRequired()])