from django.shortcuts import render
from django.http import HttpResponse , HttpResponseNotAllowed, Http404, HttpResponseRedirect
from django.views.generic import TemplateView
from .models import Article
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
# Create your views here

########  List View  ########

class ArticleListView(TemplateView): # Article List
    template_name = 'article_list.html'
    queryset = Article.objects.all()

    '''
    def get_queryset(self):
        if not self.queryset:
            self.queryset = Article.objects.all()
        return self.queryset    '''

    def get(self, request, *args, **kwargs):
        print(request.GET)
        ctx = {
            'articles': self.queryset
        }
        return self.render_to_response(ctx)

#####   Detail View ########
class ArticleDetailView(TemplateView):  # Article Detail
    template_name = 'article_datail.html'
    queryset = Article.objects.all()
    pk_url_kwargs = 'article_id'

    def get_object(self, queryset = None):
        queryset = queryset or self.queryset            # queryset parameter 초기화
        pk = self. kwargs.get(self.pk_url_kwargs)       # pk는 모델에서 정의된 pk값, 여기서는 id
        print(self.kwargs)
        article = queryset.filter(pk=pk).first()           # pk로 겁색된 데이터가 있다면 그 중 첫번째 데이터 없으면 None

        if not article:
            raise Http404("invalid pk")
        return article


    def get(self, request, *args, **kwargs):
        article = self.get_object()
        ctx = {
           'article' : article
        }
        return self.render_to_response(ctx)
        
@method_decorator(csrf_exempt, name= 'dispatch')
class ArticleCreateUpdateView(TemplateView): # Article create and Update
    template_name = 'article_update.html'
    queryset = Article.objects.all()
    pk_url_kwargs = 'article_id'
    success_message = '게시글이 저장되었습니다.'

    
    def get_object(self, queryset = None):
        queryset = queryset or self.queryset            # queryset parameter 초기화
        pk = self. kwargs.get(self.pk_url_kwargs)       # pk는 모델에서 정의된 pk값, 여기서는 id
        print('self.kwargs' , self.kwargs)
        article =  queryset.filter(pk=pk).first()  

        if pk and not article:
            raise Http404('invalid pk')
        return article

    def get(self, request, *args, **kwargs):    # 화면 요청
        article =  self.get_object()
        
        ctx = {
            'article' : article
        }
        return self.render_to_response(ctx)
            
    def post(self, request, *args, **kwargs):   # Action
        action =  request.POST.get('action')
        post_data = {key: request.POST.get(key) for key in ('title', 'content', 'author')}
        print('post_data : ', post_data)
        
        for key in post_data:       # three data validaiton
            if not post_data[key]:
                # raise Http404('No Data for {}' .format(key))
                messages.error(self.request, '{} 값이 존재하지 않습니다.' .format(key), extra_tag='danger')

        if len(messages.get_messages(request)) == 0:
            if action == 'create':      # create function 
                print(" 생성 액션 시작")
                article = Article.objects.create(**post_data)
                messages.success(self.request, self.success_message)

            elif action == 'update':     # update function
                article = self.get_object()

                # if not article:         # Article existing test
                #     raise Http404('존재하지 않는 Article 입니다.')
                
                for key, value in post_data.items():
                    print(' 생성인데 왜 여기타니?')
                    setattr(article, key, value)
                article.save()
                messages.success(self.request, self.success_message)


            else:
                messages.error(self.request, '알 수 없는 요청입니다.', extra_tag = 'danger')
            return HttpResponseRedirect('/article/')
        
        print('article_DB:', self.get_object())
        
        ctx = {
            'article' : self.get_object() if action == 'update' else None
        }
        return self.render_to_response(ctx)



def hello(request, to):
    return HttpResponse('Hello {}.' .format(to) )




'''
def list_article(request):
    return HttpResponse('list')

def detail_article(request, article_id):
    return HttpResponse('detail {}' .format(article_id))

def create_or_update_article(request, article_id):
    if article_id:
        if request.method == 'GET':
            return HttpResponse('update {}' .format(article_id))
        elif request.method == 'POST':
            return do_create_article(request)
        else:
            return HttpResponseNotAllowed(['GET', 'POST'])
    else:
        if request.method == 'GET':
            return HttpResponse('create')
        elif request.method == 'POST':

    
    else:
        return HttpResponse('create')

def do_create_article(request):
    return HttpResponse(request.POST)

def do_update_article(request):
    return HttpResponse(request.POST)

'''