from django.forms import ModelForm, Textarea
from post.models import Post, PostInfo
from post.common.views import ParsePost


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'content': Textarea(attrs={'cols': 80, 'rows': 20}),
        }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.label_suffix = ""
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['content'].widget.attrs['class'] = 'form-control'
        if self.instance.content:
            content = ParsePost(self.instance.content)
            self.initial['content'] = content


class PostInfoForm(ModelForm):
    class Meta:
        model = PostInfo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PostInfoForm, self).__init__(*args, **kwargs)
