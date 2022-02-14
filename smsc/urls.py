"""smsc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve

from main.views import *
from smsc import settings

urlpatterns = [
    path('', mainHandler),
    path('login/', loginHandler),
    path('course/', courseHandler),
    path('course/<int:course_id>/', courseItemHandler),

    path('profile/edit/', editHandler),
    path('profile/courses/', profileCoursesHandler),


    path('api/', apiHandler),
    path('api/coursecategory/', apiCourseCategoriesHandler),
    path('api/coursecategory/add/', apiCourseCategoriesAddHandler),
    path('api/coursecategory/<int:item_id>/', apiCourseCategoriesEditHandler),

    path('api/upload/', apiUploadHandler),

    path('api/courses/', apiCoursesHandler),
    path('api/courses/add/', apiCoursesAddHandler),
    path('api/courses/<int:item_id>/', apiCoursesEditHandler),


    path('api/news/', apiNewsHandler),
    path('api/news/add/', apiNewsAddHandler),
    path('api/news/<int:item_id>/', apiNewsEditHandler),



    path('logout', logoutHandler),
    path('register', registerHandler),
    path('admin/', admin.site.urls),


    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT
    })
]
