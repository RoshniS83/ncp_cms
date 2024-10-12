from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from ncpforpeople.models import People
from ncpforpeople.serializers import PeopleSerializer


# Create your views here.
class PeopleAPI(ModelViewSet):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer

    def list(self, request, *args, **kwargs):
        try:
            people = People.objects.all()
            serializer = self.get_serializer(people, many=True)
            api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_200_OK,
                                        'message': 'All People Issues',
                                        'all_products': serializer.data,
                              }
            return Response(api_response)
        except Exception as e:
            error_message = 'An error occurred while fetching product: {}'.format(str(e))
            error_response = {
                              'status': 'error',
                              'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                              'message': error_message
                    }
            return Response(error_response)

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_200_OK,
                                        'message': 'People Issue details fetched successfully',
                                        'product_details': serializer.data,
                              }
            return Response(api_response)
        except Exception as e:
            error_message = 'An error occurred while fetching product: {}'.format(str(e))
            error_response = {
                                        'status': 'error',
                                        'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                                        'message': error_message
                              }
            return Response(error_response)

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            api_response = {
                'status': 'success',
                'code': status.HTTP_201_CREATED,
                'message': 'People issue details added successfully',
                'new_category': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_message = 'Failed to add People Issue details:{}'.format(str(e))
            error_response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': error_message
            }
        return Response(error_response)

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_200_OK,
                                        'message': 'People issue updated successfully',
                                        'updated_peopleIssue': serializer.data,
                              }
            return Response(api_response)
        except Exception as e:
            error_message = 'Failed to update product details:{}'.format(str(e))
            error_response = {
                                        'status': 'error',
                                        'code': status.HTTP_400_BAD_REQUEST,
                                        'message': error_message
                              }
            return Response(error_response)

    def partial_update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_200_OK,
                                        'message': 'People issue updated successfully',
                                        'updated_product': serializer.data,
                              }
            return Response(api_response)
        except Exception as e:
            error_message = 'Failed to partially update product details:{}'.format(str(e))
            error_response = {
                                        'status': 'error',
                                        'code': status.HTTP_400_BAD_REQUEST,
                                        'message': error_message
                              }
            return Response(error_response)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()

            api_response = {
                                        'status': 'success',
                                        'code': status.HTTP_200_OK,
                                        'message': 'PeopleIssue deleted successfully',
                              }
            return Response(api_response)
        except Exception as e:
            error_message = 'Failed to delete peopleIssue details:{}'.format(str(e))
            error_response = {
                                        'status': 'error',
                                        'code': status.HTTP_400_BAD_REQUEST,
                                        'message': error_message
                              }
            return Response(error_response)

# Create your views here.
