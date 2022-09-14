from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('photo','category', 'area', 'title', 'text', 'location', 'phone_number', 'tag', 'stars', 'lat','lng')
		labels = {
            'photo': '圖片',
            'title': '標題',
            'text':'內文',
            'category':'請選擇類別',
            'area':'請選擇縣市',
            'location':'地址',
            'phone_number':'電話',
            'tag':'標籤',
            'stars':'想去指數',
            'lat':'緯度',
            'lng':'經度',
        }

class post_comment_form(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_man', 'comment_content']