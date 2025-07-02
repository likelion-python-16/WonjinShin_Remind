from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from collections import OrderedDict
from django.conf import settings

class CustomPageNumberPagination(PageNumberPagination):
  default_page_size = settings.REST_FRAMEWORK.get("PAGE_SIZE", 10) # 세팅사이즈가 없을때 디폴트사이즈 값을 따라라 

  def paginate_queryset(self, queryset, request, view=None): # 데이터를 몇개로 나눌껀지. 
    page_size = request.query_params.get("page_size", self.default_page_size)

    if page_size == "all": # size = all 전체조건을 보여줘라
      self.page_size = queryset.count()
    else:
      try:
        self.page_size = int(page_size)
      except ValueError:
        self.page_size = self.default_page_size

    return super().paginate_queryset(queryset, request, view)

  def get_paginated_response(self, data):
    return Response(
      OrderedDict([
        ("data", data),
        ("page_size", len(data)),
        ("total_count", self.page.paginator.count),
        ("page_count", self.page.paginator.num_pages),
        ("current_page", self.page.number),
        ("next", self.get_next_link()),
        ("previous", self.get_previous_link()),
      ])
    )