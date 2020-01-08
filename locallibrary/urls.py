"""locallibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
]

# domain/catalog로 시작되는 request가 오면
# catalog/urls.py를 참조해서 관련 파일을 mapping하겠다는 의미
urlpatterns += [
    path('catalog/', include('catalog.urls')),
]

# RedirevtView(): path()에서 지정된 URL 패턴이 일치할 때
# 첫번째 파라미터를 /catalog/로 리다이렉트할 새로운 상대 URL로 간주
urlpatterns += [
    path('', RedirectView.as_view(url='/catalog/', permanent=True)),
]

# 개발 중 정적 파일을 사용 가능하게 하는 코드
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



