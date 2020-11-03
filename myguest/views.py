from django.shortcuts import render
from myguest.models import Guest
from boto.connection import HTTPResponse
from django.http.response import HttpResponseRedirect
from datetime import datetime

# Create your views here.
def MainFunc(request):
    return render(request, 'main.html')

def ListFunc(request):
    #gdata = Guest.objects.all()
   # print(gdata)  # QuerySet으로 리턴
   # print(Guest.objects.get(id=1)) # 값이 출력 
   # print(Guest.objects.filter(id=1)) # QuerySet[값]
   # print(Guest.objects.filter(title__contains='안녕')) # 안녕이라는 글자를 title에 갖고 있는 튜플 출력

    # 정렬 방법1
    #gdata = Guest.objects.all().order_by('title') # 제목순으로 정렬된다.(ascending sort)
    #gdata = Guest.objects.all().order_by('-id') # 아이디순으로 정렬된다.(descending sort)
    #gdata = Guest.objects.all().order_by('-id')[0:3] # 아이디의 0~ 2번째까지만 출력된다. => slicing 처리
    
    gdata = Guest.objects.all()
    context = {'gdatas' : gdata}
    
    return render(request, 'list.html', context)

def InsertFunc(request):
    return render(request, 'insert.html')

def InsertFuncOk(request):
    if request.method == 'POST' :
        print(request.POST.get('title'))
        print(request.POST['title']) # 위와 결과 동일
        Guest(
            title= request.POST.get('title'),
            content = request.POST.get('content'),
            regdate = datetime.now()
            ).save() #  레코드 추가 insert into myguest_guest values(...)와 같음.
            
        # 수정
        g = Guest.objects.get(id = 1)
        g.title = request.POST.get('title')
        g.save() # 바로 수정이 된다. update myguest_guest set title =...와 동일
            
        # 삭제
        g = Guest.objects.get(id =1)
        g.delete() # delete from myguest_guest whre id = 1 와 동일
    return HttpResponseRedirect('/guest')    # 추가 후 목록보기