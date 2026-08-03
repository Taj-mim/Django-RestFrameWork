from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

# Create your custom pagination class here.
class CustomTeacherPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'Blog_size'
    max_page_size = 100
    def get_paginated_response(self, data):
     return Response({
        'Next': self.get_next_link(),
        'Previous': self.get_previous_link(),
        'Total Pages': self.page.paginator.num_pages,
        'Total Items': self.page.paginator.count,
    })