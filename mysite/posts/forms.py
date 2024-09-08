
from django import  forms

from posts.models import Post


class PostForm(forms.ModelForm):
    # django --> build form based on model ?
    class Meta:
        model = Post
        fields = '__all__'


    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 50:
            raise forms.ValidationError("title is too long")
        if title.lower() in ["post title", "mytitle", "my post"]:
            raise forms.ValidationError("Post mustmn't have title like this")
        return title

