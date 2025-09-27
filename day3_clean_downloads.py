#Day3 下载文件夹自动分类（由于我是纯纯新手，所以是在FakeDownloads里面操作）
import os
import shutil   #用来移动文件

DOWNLOADS = '/Users/zz/Desktop/FakeDownloads'    #改成你的路径
PICTURE = ('.jpg','.jpeg','.png','.gif','.bmp')
DOC = ('.pdf','.doc','.docx','.xls','.xlsx','.ppt','.pptx','.txt')
VIDEO = ('.mp4','.avi','.mkv','.mov','.flv')
ZIP = ('.zip','.rar','.7z','.tar','.gz')

#创建分类目录
for folder in ('图片','文档','视频','压缩包','其他'):
    os.makedirs(os.path.join(DOWNLOADS,folder),exist_ok=True)

#遍历文件并分类
for name in os.listdir(DOWNLOADS):
    src = os.path.join(DOWNLOADS,name)
    if os.path.isfile(src):      #只处理文件，跳过文件夹
        ext = os.path.splitext(name)[1].lower()  #取后缀
        if ext in PICTURE:
            dst = os.path.join(DOWNLOADS,'图片',name)
        elif ext in DOC:
            dst = os.path.join(DOWNLOADS,'文档',name)
        elif ext in VIDEO:
            dst = os.path.join(DOWNLOADS,'视频',name)
        elif ext in ZIP:
            dst = os.path.join(DOWNLOADS,'压缩包',name)
        else:
            dst = os.path.join(DOWNLOADS,'其他',name)
        shutil.move(src,dst)    #正式移动
        print(f'已移动:{name}➡️{os.path.basename(os.path.dirname(dst))}')

print('下载文件夹整理完成！')
