from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os

PIC_ROOT = 'img/'
PIC_URL = 'http://localhost:8000/upload/img/'


@csrf_exempt
def uploadImage(request):
    # file template
    file = request.FILES.get('file')
    userId = request.POST.get('user_id')
    fileName = file.name
    try:
        # 图片格式
        imageFormat = fileName.split('.')[-1]
        if imageFormat not in ['jpeg', 'jpg', 'png', 'bmp', 'tif', 'gif']:
            return JsonResponse({'code': -2, 'message': '图片格式有误'})
        # 图片路径
        if not os.path.exists(PIC_ROOT):
            os.makedirs(PIC_ROOT)
        imagePath = PIC_ROOT + '/' + 'avatar_' + userId + imageFormat
        # 导入图片
        with open(imagePath, 'wb+') as f:
            for chunk in file.chunks():
                f.write(chunk)
        f.close()
        return JsonResponse({'code': 0, 'message': '', 'image_path': imagePath})
    except Exception as e:
        print(e)
        return JsonResponse({'code': -2, 'message': '图片存储错误'})
