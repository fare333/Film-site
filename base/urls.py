from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("film/<str:product_id>/",views.film_details,name="film_detail"),
    path("popular_films/",views.popular_films,name="popular_films"),
    path("trending_films/",views.trending_films,name="trending_films"),
    path("search/",views.search,name="search"),
    path("categories/",views.categories,name="categories"),   
    path("category_films/<str:pk>/",views.category_films,name="category_films"),
    path("login/",views.signin,name="login"),
    path("register/",views.register,name="register"),
    path("logout/",views.signout,name="logout"),
]
