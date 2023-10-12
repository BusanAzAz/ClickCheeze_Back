from .serializers import ImageSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .module.colorchart import getChart
from .module.http import ok
from .module.character_recomend import getBackColor

import os
import subprocess

# Create your views here.
@api_view(['POST'])
def post(request):
    if request.method == 'POST':
        serializer = ImageSerializer(data=request.FILES)
        print(serializer.is_valid())
        if serializer.is_valid(raise_exception = True):
            print('이거까진 됨')
            serializer.save()
            # 현재 디렉토리 저장
            original_dir = os.getcwd()
            # 새로운 디렉토리로 이동
            os.chdir("color/src")
            try:
                # 스크립트 실행
                print(serializer.data['image'])
                res = subprocess.check_output("python main.py --image ../.." + serializer.data['image'], shell=True)
            except subprocess.CalledProcessError as e:
                print(e)
                return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            finally:
                # 원래의 디렉토리로 돌아가기
                os.chdir(original_dir)
            return Response(ok("퍼스널컬러 차트 로드 성공", rtnColorChart(res.decode("utf-8"))), status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def rtnColorChart(result):
    personal_color_info = result.split('퍼스널 컬러는 ')[1]
    tone = personal_color_info.split('(')[0]

    colorChart = getChart(tone)

    result = {
        "tone" : tone,
        "personal_color" : colorChart
    }
    return result

@api_view(['GET'])
def get(request, category):
    if request.method == 'GET':
        res = getBackColor(category)
        return Response(ok("카테고리 로드 성공", res), status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)