from django import forms

class AutorFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    profesion = forms.CharField()

class CategoriaFormulario(forms.Form):
    nombre = forms.CharField()

class PostFormulario(forms.Form):
    titulo = forms.CharField()
    contenido = forms.CharField(widget=forms.Textarea)
    fecha_publicacion = forms.DateField(widget=forms.SelectDateWidget)

class BusquedaFormulario(forms.Form):
    termino = forms.CharField(label="Buscar autor por nombre")