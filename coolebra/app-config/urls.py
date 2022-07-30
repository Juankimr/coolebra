"""coolebra URL Configuration
Function views
     path('', views.home, name='home')
Class-based views
     path('', Home.as_view(), name='home')
Including another URLconf
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('portfolio/', include('portfolio.urls')),
]
