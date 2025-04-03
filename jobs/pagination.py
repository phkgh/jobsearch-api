from rest_framework.pagination import PageNumberPagination


class JobPostPagination(PageNumberPagination):
    page_size = 5  # You can change this to 10 or any number
