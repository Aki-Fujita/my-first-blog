from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model): # これは天下り的なもので、DBに保存すべきもの、といっている
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)#他のモデルへのリンク
    title = models.CharField(max_length = 200) #fieldのタイプをきてめいてこれは文字数制限付きテキスト
    text = models.TextField() #制限なしの長いテキスト用
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank = True, null = True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self): #アンダースコア二つで書くと外部の参照を受けない感が出るらしい。
        return self.title


