from django.db import models

# Create your models here.
class Guest(models.Model):
   # myno = models.AutoField(auto_created = True, primary_key = True) ==> 해당 컬럼때문에 id가 생성되지않는다.
    title = models.CharField(max_length=50)
    content = models.TextField()
    regdate = models.DateTimeField()
    
    
    def __str__(self):
        #return models.Model.__str__(self)__(self):
        return self.title
    
    # 정렬 방법2
    class Meta:
#        ordering = ('title',) # title 별 오름차순 정렬 : tuple 타입이어야 한다.
#        ordering = ('-title',) # title 별 내림차순 정렬
#        ordering = ('title','id') # n차 키를 부여할 수 있다.
        ordering = ('-id',)