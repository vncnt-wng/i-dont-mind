from django import forms

class JoinRoomForm(forms.Form):
    room_id = forms.CharField(label='Room ID', max_length=100)