from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'title', 'text')

        """
        Opcje jakie chcemy dołączyć do pola w HTML, 
        class by potem przypisać CSS
        """
        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'})
        }

        labels = {
            'title': "Tytuł",
            'text': "Tekst",
            'author': "Autor",
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text')

        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'})
        }

        labels = {
            'author': "Autor",
            'text': 'tekst',
        }
