from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("products/", views.products_list),
    path("products/<int:pk>/", views.product_detail),
    path("components/", views.components_list),
    path("components/<int:pk>/", views.component_detail),
    path("products/<int:pk>/produce", views.product_produce),
    path("stock-movements/", views.stock_movements_list),
    path("product-components/", views.product_component_list),
    path("product-components/<int:pk>/", views.product_component_detail)

]

urlpatterns = format_suffix_patterns(urlpatterns)
