
from django.urls import path
from . import views as blog_views

app_name= 'blog'
#it is a good practice to define the app name in case of many app
#we may have many 'details' view to manage and reference inside the templates!

urlpatterns = [
    path('', blog_views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', blog_views.detail, name="detail")
]

