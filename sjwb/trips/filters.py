from cProfile import label
from cgitb import lookup
from secrets import choice
from django.db.models import Q
import django_filters
from django_filters import CharFilter, ChoiceFilter, OrderingFilter

from trips.models import *

STARS_CHOICES = (
    (1, '1星'),
    (2, '2星'),
    (3, '3星'),
    (4, '4星'),
    (5, '5星'),
)

class PostFilter(django_filters.FilterSet):
    text = CharFilter(label='關鍵字',method='my_custom_filter')
    stars = ChoiceFilter(label='想去指數',choices=STARS_CHOICES, field_name='stars')
    order = OrderingFilter(
        label='排序',
        empty_label='預設排序(最想去)',
        fields=(
            ('published_date', 'published_date'),
            ('stars'),
        ),
         field_labels={
            'published_date': '更新日期',
            'stars': '想去指數',
        }
        )
    class Meta:
        model = Post
        fields = ['area']

    def my_custom_filter(self, queryset, name, value):
        return queryset.filter(
            Q(title__icontains=value) | Q(text__icontains=value) | Q(tags__name__icontains=value)
        ).distinct()

    def __init__(self, *args, **kwargs):
        super(PostFilter, self).__init__(*args, **kwargs)
        for filter in self.filters:
            if filter != 'text' and filter != 'order':
                self.filters[filter].extra.update(
                {'empty_label': '請選擇'})
            if  filter== 'area':
                self.filters[filter].label = "地區"
            
