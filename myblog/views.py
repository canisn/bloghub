from django.views.generic.list import ListView
from myblog.models import Article, Category
import markdown2


# class IndexView(ListView):
#     template_name = "index.html"
#     context_object_name = "article_list"

#     def get_queryset(self):
#         article_list = Article.objects.filter(status='p')
#         for article in article_list:
#             article.body = markdown2.markdown(article.body, )
#         return article_list

#     def get_context_data(self, **kwargs):
#         kwargs['category_list'] = Category.objects.all().order_by('name')
#         return super(IndexView, self).get_context_data(**kwargs)
