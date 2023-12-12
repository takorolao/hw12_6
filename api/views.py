from rest_framework.viewsets import ModelViewSet
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated
from django.views.generic import TemplateView

class ProductView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

class Home(TemplateView):
    template_name = 'home.html'
