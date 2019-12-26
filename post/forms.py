from django.forms import ModelForm, Textarea
from post.models import Post, PostInfo


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        labels = {
            'title': '제목',
            'content': '내용',
        }
        widgets = {
            'content': Textarea(attrs={'cols': 80, 'rows': 20}),
        }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.label_suffix = ""
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['content'].widget.attrs['class'] = 'form-control'


class PostInfoForm(ModelForm):
    class Meta:
        model = PostInfo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PostInfoForm, self).__init__(*args, **kwargs)
