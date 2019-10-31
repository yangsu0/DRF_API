from django.shortcuts import render
from .models import UserPost
from .serializer import UserSerializer
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

# Create your views here.

class UserPostViewSet(viewsets.ModelViewSet):
    queryset = UserPost.objects.all()
    serializer_class = UserSerializer

    # 어떤것을 기반으로 검색을 진행할지 =필터 백앤드
    # 어떤 칼럼을 기반으로 검색을 한건지 =서치필드(무조건 튜풀)
    filter_backends = [SearchFilter]
    search_fields = ('title')

    def get_queryset(self):
        # 여기 내부에서 쿼리셋을 조정한 다음에 리턴해주는것입니당
        # 일단 부모클래스에서의 쿼리셋을 가져와야함
        qs = super().get_queryset()
        # qs = qs.filter(author__id=1)
        #혹은 .filter .exclude

        # 지금 로그인한 유저의 글만 필터링!

        # 지금 만약 로그인이 되어있다면 -> 로그인한 유저의 글을 필터링
        # 로그인이 안되어있다면 -> 비어있는 쿼리셋을 리턴해라!
        if self.request.user.is_authenticated:
            qs = qs.filter(author=self.request.user)
        else:
            qs = qs.none()

        return qs