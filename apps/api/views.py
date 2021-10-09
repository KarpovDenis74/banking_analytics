import datetime

from django.contrib.auth import get_user_model
from django_filters import BaseInFilter, FilterSet, NumberFilter
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from apps.api.permissions import IsAdminOrReadOnly
# from api.pagination import CustomPagination
from apps.api.serializers import CurrencyRateSerializer
from apps.currency.models import CurrencyRate

User = get_user_model()


class NumberInFilter(BaseInFilter, NumberFilter):
    pass


class ProductFilter(FilterSet):
    currency = NumberFilter()
    currency__in = NumberInFilter(
        field_name='currency', lookup_expr='in')


class CurrencyAPI(viewsets.ReadOnlyModelViewSet):
    queryset = CurrencyRate.objects.all()
    permission_classes = [IsAdminOrReadOnly, ]
    serializer_class = CurrencyRateSerializer
    # filter_backends = (ProductFilter,)
    # filterset_fields = ('date', 'currency')

    def get_queryset(self):
        queryset = CurrencyRate.objects.all()
        date = self.request.query_params.get('date')
        date = datetime.datetime.strptime(date, "%Y-%m-%d")
        currency = self.request.query_params.get('currency')
        if currency is not None:
            currency = currency.split(",")
            print(currency)
            queryset = queryset.filter(date=date, currency__in=currency)
        else:
            queryset = queryset.filter(date=date)
            print(queryset)
        return queryset

    # def get_queryset(self):
    #     cur_day_str = str(self.kwargs.get("cur_day"))
    #     try:
    #         cur_day_dt = dt.datetime.strptime(
    #             cur_day_str, "%Y-%m-%d")  # Date="20210831" -> datetime
    #     except Exception:
    #         return None
    #     queryset = get_list_or_404(
    #         CurrencyRate,
    #         date=cur_day_dt)
    #     return queryset

# class MixinViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin,
#                    mixins.ListModelMixin, GenericViewSet):
#     pass


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [IsAuthenticated, Permission1]
#     pagination_class = CustomPagination
#     lookup_field = 'username'

#     @action(detail=False, methods=['GET'], url_path='me',
#             permission_classes=[IsAuthenticated])
#     def get(self, request):
#         user = request.user
#         serializer = UserSerializer(user, many=False)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     @action(detail=True, methods=['PATCH'], url_path='me')
#     def patch(self, request):
#         permission_classes = [IsAuthenticated]
#         user = request.user
#         serializer = UserEditSerializer(
#             user, data=request.data, many=False, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(status=status.HTTP_403_FORBIDDEN)


# def get_tokens_for_user(user):
#     refresh = RefreshToken.for_user(user)
#     return {
#         'refresh': str(refresh),
#         'access': str(refresh.access_token),
#     }


# @api_view(('POST',))
# def token(request):
#     email = request.data.get('email')
#     confirmation_code = request.data.get('confirmation_code')
#     user = get_object_or_404(
#         User, email=email)
#     tokens = get_tokens_for_user(user)
#     return Response({"message": tokens})


# @api_view(('POST',))
# def reg_user_email(request):
#     if not request.data.get('email'):
#         return Response({'message': {
#             'Ошибка': 'Не указана почта для регистрации'}},
#             status=status.HTTP_403_FORBIDDEN)
#     try:
#         email = request.data.get('email')
#         confirmation_code = random.randint(1, 100000000)
#         a, b = User.objects.get_or_create(
#             email=email, defaults={'confirmation_code': confirmation_code})
#     except:
#         return Response({'message': {
#             'Ошибка': 'Ошибка запроса'}}, status=status.HTTP_403_FORBIDDEN)
#     send_mail(
#         'Подтверждение адреса электронной почты YaTube',
#         'Вы получили это письмо, потому что регистрируетесь на ресурсе '
#         'YaTube Код подтверждения confirmation_code='
#          + str(confirmation_code),
#         settings.DEFAULT_FROM_EMAIL,
#         [email, ],
#         fail_silently=False,)
#     return Response({'message': {
#         'ОК': f'Пользователь c email {email} создан успешно. '
#         'Код подтверждения отправлен на электронную почту'}})


# class CategoryAPI(MixinViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['=name']
#     lookup_field = 'slug'
#     permission_classes = [IsAdminOrReadOnly]
#     pagination_class = PageNumberPagination


# class GenresAPI(MixinViewSet):
#     queryset = Genre.objects.all()
#     serializer_class = GenreSerializer
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['=name']
#     lookup_field = 'slug'
#     permission_classes = [IsAdminOrReadOnly]
#     pagination_class = PageNumberPagination


# class TitleAPI(viewsets.ModelViewSet):
#     queryset = Title.objects.annotate(rating=Avg('review__score'))
#     permission_classes = [IsAdminOrReadOnly]
#     pagination_class = PageNumberPagination
#     __basic_fields = ('genre', 'category', 'year', 'name')
#     filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
#     search_fields = __basic_fields
#     filterset_class = TitleFilter

#     def get_serializer_class(self):
#         if self.request.method == 'GET':
#             return TitleReadSerializer
#         else:
#             return TitleWriteSerializer


# class ReviewAPI(viewsets.ModelViewSet):
#     serializer_class = ReviewSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly, ReviewCommentPermission]
#     pagination_class = PageNumberPagination

#     def get_queryset(self):
#         title = get_object_or_404(
#             Title,
#             id=self.kwargs.get('title_id')
#         )
#         return title.review.all()

#     def perform_create(self, serializer):
#         title = get_object_or_404(
#             Title,
#             id=self.kwargs.get('title_id')
#         )
#         serializer.save(
#             author=self.request.user,
#             title=title
#         )


# class CommentsAPI(viewsets.ModelViewSet):
#     serializer_class = CommentSerializer
#     filter_backends = [filters.SearchFilter]
#     permission_classes = [IsAuthenticatedOrReadOnly, ReviewCommentPermission]
#     pagination_class = PageNumberPagination

#     def get_queryset(self):
#         queryset = get_object_or_404(
#             Review,
#             id=self.kwargs.get("review_id"),
#             title=self.kwargs.get("title_id"), )
#         return queryset.comments.all()

#     def perform_create(self, serializer):
#         review = get_object_or_404(
#             Review,
#             id=self.kwargs.get("review_id"),
#             title__id=self.kwargs.get("title_id"), )
#         serializer.save(
#             author=self.request.user,
#             reviews=review
#         )
