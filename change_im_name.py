#批量给图片改名
import os

class BatchRename():

      def rename(self):
        path="./img"
        filelist=os.listdir(path)
        total_num = len(filelist)
        i=0
        for item in filelist:
            if item.endswith('.jpg'):
                src=os.path.join(os.path.abspath(path),item)
                dst=os.path.join(os.path.abspath(path),'x'+str(i)+'x'+'.jpg') #可根据自己需求选择格式
                  # dst=os.path.join(os.path.abspath(path),'00000'+format(str(i))+'.jpg') #可根据自己需求选择格式,自定义图片名字
                try:
                    os.rename(src,dst) #src:原名称  dst新名称d
                    i+=1
                except:
                    continue
        print ('total %d to rename & converted %d jpg'%(total_num,i))

if __name__=='__main__':
    demo = BatchRename()
    demo.rename()