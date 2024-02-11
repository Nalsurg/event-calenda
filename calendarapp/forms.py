from django.forms import ModelForm, DateInput
from calendarapp.models import Event, EventMember
from django import forms

# Формы  модальном окне
class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ["title", "resourceId", "description", "start_time", "end_time"]
        # datetime-local is a HTML5 input type
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter event title"}
            ),
            "resourceId": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Выбирите кабинет",  "id": "resourceId", "value": ""}
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter event description",
                }
            ),
            "start_time": DateInput(
                attrs={"type": "datetime-local", "class": "form-control", "id": "startDateTime", "value": ""},
                format="%Y-%m-%dT%H:%M",
            ),
            "end_time": DateInput(
                attrs={"type": "datetime-local", "class": "form-control", "id": "endDateTime", "value": ""},
                format="%Y-%m-%dT%H:%M",
            ),
        }
        exclude = ["user"]

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        # input_formats для анализа HTML5 datetime-local ввода в поле datetime
        self.fields["start_time"].input_formats = ("%Y-%m-%dT%H:%M",)
        self.fields["end_time"].input_formats = ("%Y-%m-%dT%H:%M",)


class AddMemberForm(forms.ModelForm):
    class Meta:
        model = EventMember
        fields = ["user"]
