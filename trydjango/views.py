from django.http import HttpResponse
from django.template.loader import render_to_string
import random

from articles.models import Article

def home_view(request):
    random_id = random.randint(1,4)

    #From the database
    article_obj = Article.objects.get(id=random_id)
    article_qs = Article.objects.all()
    
    context = {
        'object_list': article_qs,
        'object': article_obj,
        'title': article_obj.title,
        'id': article_obj.id,
        'content': article_obj.content
    }
    #Django tmeplate


    HTML_STRING = render_to_string('home-view.html', context=context)
    # HTML_STRING = '''
    # <h1> {title} (id: {id}) </h1>
    # <p>{content} </p>
    # '''.format(**context)
    return HttpResponse(HTML_STRING) 