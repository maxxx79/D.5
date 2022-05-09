from django_filters import FilterSet, ModelChoiceFilter, \
    DateFromToRangeFilter, CharFilter
# from django_filters.widgets import RangeWidget, SuffixedMultiWidget

from .models import Post, Author, Category, Comment, PostCategory



# class DurationRangeWidget(SuffixedMultiWidget, RangeWidget):
#     suffixes = ['min', 'max']
class PostFilter(FilterSet):

    creation_date = DateFromToRangeFilter(
        field_name={'creation_date': '%d-%m-%Y'},
        label='Дата',
        lookup_expr='gt'
    )
    title = CharFilter(
        field_name='title',
        label='Заголовок содержит',
        lookup_expr='icontains'
    )
    author = ModelChoiceFilter(
        field_name='author',
        label='Автор',
        lookup_expr='exact',
        queryset=Author.objects.all()
    )
    post_category = ModelChoiceFilter(
        field_name='post_category',
        label='Категория',
        lookup_expr='exact',
        queryset=Category.objects.all()
    )

    class Meta:
        model = Post
        fields = ['author', 'post_category', 'creation_date', 'title']



