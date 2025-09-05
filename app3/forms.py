from django import forms



class DemoForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter your full name'}))
    age = forms.IntegerField(
        label='Your age',
        widget=forms.NumberInput(attrs={'type': 'number', 'min': '0', 'step': '1'}),
        min_value=0
    )
    date_reservation = forms.DateField(label='Reservation Date', widget=forms.DateInput(attrs={'type': 'date'}))
    email = forms.EmailField(label='Your email')
    agree_to_terms = forms.BooleanField(label='I agree to the terms and conditions')
    upload = forms.FileField(label='Upload file', required=False)

    # Otros campos para probar:
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    bio = forms.CharField(label='Biography', widget=forms.Textarea(attrs={'rows': 3}))
    website = forms.URLField(label='Website', required=False)
    favorite_color = forms.ChoiceField(
        label='Favorite Color',
        choices=[('red', 'Red'), ('green', 'Green'), ('blue', 'Blue')],
        widget=forms.RadioSelect
    )
    profile_picture = forms.ImageField(label='Profile Picture', required=False)
    birth_month = forms.DateField(label='Birth Month', widget=forms.SelectDateWidget(years=range(1980, 2030)))
    interests = forms.MultipleChoiceField(
        label='Interests',
        choices=[('music', 'Music'), ('sports', 'Sports'), ('coding', 'Coding')],
        widget=forms.CheckboxSelectMultiple
    )


from .models import Logger
class logForm(forms.ModelForm):
    class Meta:
        model = Logger
        fields = '__all__'
