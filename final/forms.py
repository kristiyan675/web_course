from django import forms
from .models import Post, Category

choices = Category.objects.all().values_list("name", 'name')
list_of_choices = []
for x in choices:
    list_of_choices.append(x)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', "title_tag", "author", "category", "body", 'snippet', 'header_image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type Here'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'user', 'type': 'hidden'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=list_of_choices, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }
