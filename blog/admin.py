from django.contrib import admin
from .models import Post
#below two are for ckeditor
from ckeditor.widgets import CKEditorWidget
from django import forms


class PostAdminForm(forms.ModelForm):
	body = forms.CharField(widget=CKEditorWidget())
	class Meta:
		model = Post
		fields = '__all__'

class PostAdmin(admin.ModelAdmin):
	fields = ['title','slug','pub_date','body']		#the order of attributes of models to display
	prepopulated_fields = {"slug": ("title",)}
	list_display = ('title','pub_date','body')				#what attributes to show on admin panel
	list_filter = ['pub_date']
	search_fields = ['title','body']
	form = PostAdminForm

admin.site.register(Post, PostAdmin)
