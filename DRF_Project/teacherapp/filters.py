from django_filters import rest_framework as filters
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import teacher

#Create Custom Filter class for teacher model
class teacherFilter(filters.FilterSet):
    teacher_name=filters.CharFilter(field_name='teacher_name',lookup_expr='icontains')
    id=filters.NumberFilter(field_name='id',lookup_expr='iexact',label='ID')
    teacher_id=filters.CharFilter(field_name='teacher_id',lookup_expr='icontains',label='Teacher ID')
    #id_range=filters.RangeFilter(field_name='teacher_id') for filtering the range of the id which have character and degits we have to use conditons
    id_min=django_filters.CharFilter(method='filter_id_by_range',label='ID Min')
    id_max=django_filters.CharFilter(method='filter_id_by_range',label='ID Max')
    class Meta:
        model=teacher
        fields=['teacher_name', 'id', 'teacher_id','id_min','id_max']

    def filter_id_by_range(self, queryset,name,value):
        if name=='id_min':
            return queryset.filter(teacher_id__gte=value)
        elif name=='id_max':
            return queryset.filter(teacher_id__lte=value)
        return queryset
