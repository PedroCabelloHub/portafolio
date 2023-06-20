from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo de la tarea", widget=forms.TextInput(attrs={'class':'input'}))
    description = forms.CharField(label="descripcion de la tarea", widget=forms.Textarea(attrs={'class':'input'}))

class CreateNewProject(forms.Form):
    name = forms.CharField(label='Nombre del projecto',widget=forms.TextInput(attrs={'class':'input'}))