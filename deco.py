# -*- coding: gbk -*-
# flake8: noqa
import sys, os, qiniu.config, time, traceback
from qiniu import Auth, put_file, etag, urlsafe_base64_encode

#timestamp = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))     #获取时间戳的方法

#本地文件夹路径
fileDir = r"D:\COMPANY\TestPics\20170411\01"

# 上传时增加的文件前缀名
prefix = '2017041101-'

#七牛云的信息
access_key = 'JDfJ_laknrdt5UveDvgB46o_JD8bM8rhLkng_Xda'
secret_key = 'CQfkc_JlY6F7WII8zbZUfsy5U-OjStB7BEpZxz3c'
bucket_name = 'zyfzyfhaha'

class upload():

    def qiNiuAccess(self):
        # 构建鉴权对象
        q = Auth(access_key, secret_key)
        return q

    #拼装本地信息
    def packageLocalInfo(self):

        #获取文件夹中需要上传的文件
        fileList = (os.listdir(fileDir))
        fileListLength = len(fileList)
        try:
            # 打印文件夹内的文件名列表
            if(fileListLength != 0):
                print ("文件夹内共有%d个文件，分别为：" %fileListLength)
                for i in range(fileListLength):
                    print (" %s" %fileList[i])

                # 拼装上传所需要的本地路径
                localFileList = []
                for i in range(fileListLength):
                    localFileList.append(fileDir + '\\' + fileList[i])

                #拼装上传到七牛云后保存的文件名
                keyList = []
                for i in range(fileListLength):
                    keyList.append(prefix + fileList[i])
                    keyListLength = len(keyList)
                print ("上传到七牛云的%d个文件名分别为：" %keyListLength)
                for j in range(fileListLength):
                    print (" %s" %keyList[j])
            else:
                print("吼吼，文件夹竟然是空的，那还传个毛啊！")
                os._exit(0)
        except:
            traceback.print_exc()


    # def uploadPics(self, keyList, ):
    #     #生成上传 Token，可以指定过期时间等
    #     tokenList = []
    #     for i in range(keyListLength):
    #         token = q.upload_token(bucket_name,keyList[i],3600)
    #         tokenList.append(token)
    #     print tokenList[0]
    #     print keyList[0]
    #     print localFileList[0]
    #
    #     infoList = []
    #     for i in range(keyListLength):
    #         ret, info = put_file(tokenList[i],keyList[i],localFileList[i])
    #         infoList.append(info)
    #     print (infoList)

    # ret, info = put_file(token, key, localfile)
    # print(info)
    # assert ret['key'] == key
    # assert ret['hash'] == etag(localfile)

if __name__ == '__main__':
    upload().packageLocalInfo()

