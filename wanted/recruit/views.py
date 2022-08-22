from django.shortcuts import render,get_object_or_404,redirect
from .models import Notification
from .forms import NotificationForm
from django.db.models import Q


def index(request): 
    search = request.GET.get('search', '')  # 검색어
    notification_list = Notification.objects.order_by('-id') # 채용공고 게시 역순
    if search:
        notification_list = notification_list.filter(
             Q(content__icontains=search)  
        ).distinct()
    context = {'notification_list': notification_list,'search': search}
    return render(request, 'recruit/notification_list.html', context)


def detail(request,notification_id): # 상세페이지
    notification = get_object_or_404(Notification,pk=notification_id)
    another= Notification.objects.exclude(id=notification_id).values()
    context = {'notification': notification, 'another':another}
    return render(request, 'recruit/notification_detail.html', context)


def another_page(request,slug):
    another = Notification.objects.get(slug=slug)
    notification_list = another.notification_set.all()

    return render(
        request,
        'recruit/notification_list.html',
        {
            'notification_list' : notification_list,
            'another' : another,
        }
    )
    
    # 회사가 올린 다른 채용공고 구현 시도
    # a = []
    # d = {}
    # for v in another:
    #     # print(v['company_id'])
    #     if v['company_id'] == notification.__str__():
    #     #     # d['company_id'] = v['company_id']
    #        print(v)

       
    # # print(notification.company)
    


def notification_create(request): # 채용공고 등록
     if request.method == 'POST':
        form = NotificationForm(request.POST)
        if form.is_valid():
            notification = form.save(commit=False)
            notification.save()
            return redirect('recruit:index')
     else:
        form = NotificationForm()
        context = {'form': form}
        return render(request, 'recruit/notification_form.html', context)

# 채용공고 지원
def user_apply(request, notification_id):
    notification = get_object_or_404(Notification, pk=notification_id)
    notification.user_set.create(user_id=request.POST.get('user_id'))
    return redirect('recruit:detail', notification_id=notification.id)

# 채용공고 수정
def notification_modify(request, notification_id): # 채용 공고 수정
    notification = get_object_or_404(Notification, pk=notification_id)
    if request.method == "POST":
        form = NotificationForm(request.POST, instance=notification)
        if form.is_valid():
            notification = form.save(commit=False)
            notification.save()
            return redirect('recruit:detail', notification_id=notification.id)
    else:
        form = NotificationForm(instance=notification)
    context = {'form': form}
    return render(request, 'recruit/notification_form.html', context)

# 채용공고 삭제
def notification_delete(request, notification_id): # 채용 공고 삭제
    notification= get_object_or_404(Notification, pk=notification_id)
    notification.delete()
    return redirect('recruit:index')


    
