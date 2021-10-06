from currency.models import Currency, CurrencyRate
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('num_code', 'char_code', 'name', )
        model = Currency


class CurrencyRateSerializer(serializers.ModelSerializer):
    currency = CurrencySerializer(read_only=True)

    class Meta:
        fields = ('pk', 'date', 'currency', 'value', 'nominal',)
        model = CurrencyRate


# class UserEditSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = ('username',
#                   'password', 'bio', 'first_name', 'last_name')
#         model = User


# class CategorySerializer(serializers.ModelSerializer):
#     name = serializers.CharField(max_length=100)
#     slug = serializers.CharField(max_length=100, validators=[
#         UniqueValidator(queryset=Category.objects.all())])

#     class Meta:
#         model = Category
#         fields = ('name', 'slug')


# class GenreSerializer(serializers.ModelSerializer):
#     name = serializers.CharField(max_length=100)
#     slug = serializers.CharField(max_length=100, validators=[
#         UniqueValidator(queryset=Genre.objects.all())])

#     class Meta:
#         model = Genre
#         fields = ('name', 'slug')


# class ReviewSerializer(serializers.ModelSerializer):
#     author = serializers.ReadOnlyField(source='author.username')

#     def validate(self, attrs):
#         if self.context["request"].method not in ['POST']:
#             return attrs
#         author = self.context["request"].user.id,
#         title = self.context["view"].kwargs.get("title_id")
#         message = 'Author review already exist'
#         if not self.instance and Review.objects.filter(title=title,
#                                                        author=author).exists():
#             raise serializers.ValidationError(message)
#         return attrs

#     class Meta:
#         model = Review
#         fields = ('id', 'text', 'author', 'score', 'pub_date')


# class TitleReadSerializer(serializers.ModelSerializer):
#     rating = serializers.DecimalField(read_only=True,
#                                       max_digits=10,
#                                       decimal_places=1,
#                                       coerce_to_string=False)
#     category = CategorySerializer(read_only=True)
#     genre = GenreSerializer(many=True)

#     class Meta:
#         fields = '__all__'
#         model = Title


# class TitleWriteSerializer(serializers.ModelSerializer):
#     rating = serializers.DecimalField(read_only=True, max_digits=10,
#                                       decimal_places=1,
#                                       coerce_to_string=False)

#     category = serializers.SlugRelatedField(
#         queryset=Category.objects.all(),
#         slug_field='slug',
#         required=False,
#     )
#     genre = serializers.SlugRelatedField(
#         queryset=Genre.objects.all(),
#         slug_field='slug',
#         many=True,
#         required=False,
#     )

#     class Meta:
#         fields = '__all__'
#         model = Title


# class CommentSerializer(serializers.ModelSerializer):
#     author = serializers.SlugRelatedField(
#         many=False,
#         read_only=True,
#         slug_field='username'
#     )

#     class Meta:
#         fields = ('id', 'text', 'author', 'pub_date')
#         model = Comment
