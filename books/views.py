from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from books.models import Book
from books.serializers import BookSerializer
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin
from rest_framework.response import Response

class BookListView(APIView, UpdateModelMixin, DestroyModelMixin):
    def get(self, request, id=None):
        if id:
            try:
                book = Book.objects.get(pk=pk)

            except Book.DoesNotExist:
                return Response({'message': 'The book does not exist'}, status=status.HTTP_404_NOT_FOUND)

            book_serializer = BookSerializer(book)
        else:
            books = Book.objects.all()
            title = request.GET.get('title', None)
            if title is not None:
                books = books.filter(title__icontains=title)

            books_serializer = BookSerializer(books, many=True)
        return Response(books_serializer.data)

    def post(self, request):
        book_serializer = BookSerializer(data=request.data)
        if book_serializer.is_valid():
            saved_book_data = book_serializer.save()
            return Response(book_serializer.data, status=status.HTTP_201_CREATED)
        return Response(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        count = Book.objects.all().delete()
        return Response({'message': '{} Books were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

class BookDetailView(APIView, UpdateModelMixin, DestroyModelMixin):
    def get(self, request, pk=None):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({'message': 'The book does not exist'}, status=status.HTTP_404_NOT_FOUND)

        book_serializer = BookSerializer(book)

        return Response(book_serializer.data)

    def put(self, request, pk=None):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({'message': 'The book does not exist'}, status=status.HTTP_404_NOT_FOUND)

        book_serializer = BookSerializer(book, data=request.data)
        if book_serializer.is_valid():
            book_serializer.save()
            return Response(book_serializer.data)
        return Response(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({'message': 'The book does not exist'}, status=status.HTTP_404_NOT_FOUND)
        book.delete()
        return Response({'message': 'Book was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

class BookSpecialView(APIView):
    def get(self, request):
        books = Book.objects.filter(published=True)
        books_serializer = BookSerializer(books, many=True)
        return Response(books_serializer.data)

# @api_view(['GET', 'POST', 'DELETE'])
# def book_list(request):
#     if request.method == 'GET':
#         books = Book.objects.all()

#         title = request.GET.get('title', None)
#         if title is not None:
#             books = books.filter(title__icontains=title)

#         books_serializer = BookSerializer(books, many=True)
#         return JsonResponse(books_serializer.data, safe=False)
#     elif request.method == 'POST':
#         book_data = JSONParser().parse(request)
#         book_serializer = BookSerializer(data=book_data)
#         if book_serializer.is_valid():
#             book_serializer.save()
#             return JsonResponse(book_serializer.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         count = Book.objects.all().delete()
#         return JsonResponse({'message': '{} Books were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'PUT', 'DELETE'])
# def book_detail(request, pk):
#     try:
#         book = Book.objects.get(pk=pk)
#         if request.method == 'GET':
#             book_serializer = BookSerializer(book)
#             return JsonResponse(book_serializer.data)
#         elif request.method == 'PUT':
#             book_data = JSONParser().parse(request)
#             book_serializer = BookSerializer(
#                 book, data=book_data)
#             if book_serializer.is_valid():
#                 book_serializer.save()
#                 return JsonResponse(book_serializer.data)
#         elif request.method == 'DELETE':
#             book.delete()
#             return JsonResponse({'message': 'Book was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
#         return JsonResponse(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     except Book.DoesNotExist:
#         return JsonResponse({'message': 'The book does not exist'}, status=status.HTTP_404_NOT_FOUND)


# @api_view(['GET'])
# def book_list_published(request):
#     books = Tutorial.objects.filter(published=True)

#     if request.method == 'GET':
#         books_serializer = BookSerializer(books, many=True)
#         return JsonResponse(books_serializer.data, safe=False)
