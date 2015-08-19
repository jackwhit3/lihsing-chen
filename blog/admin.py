from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):

	fields = ['title','slug','pub_date','body']		#the order of attributes of models to display
	prepopulated_fields = {"slug": ("title",)}
	list_display = ('title','pub_date','body')				#what attributes to show on admin panel
	list_filter = ['pub_date']
	search_fields = ['title','body']


admin.site.register(Post, PostAdmin)