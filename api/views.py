from rest_framework import viewsets
from .models import Meal, Rating
from .serializers import MealSerializer, RatingSerializer


# A viewset that provides default create(), retrieve(), update(), partial_update(), destroy() and list() actions.
class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
