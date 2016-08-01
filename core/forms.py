from .models import Event, Comments

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('date',
                  'location_title',
                  'location_code',
                  'title',
                  'picture_url',
                  'notes',
                  'additional_notes',
                  'confirmed',
                  'booked',
                  'event_url',)
