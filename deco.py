# -*- coding: gbk -*-
# flake8: noqa
import sys, os, qiniu.config, time, traceback
from qiniu import Auth, put_file, etag, urlsafe_base64_encode

#timestamp = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))     #��ȡʱ����ķ���

#�����ļ���·��
fileDir = r"D:\COMPANY\TestPics\20170411\01"

# �ϴ�ʱ���ӵ��ļ�ǰ׺��
prefix = '2017041101-'

#��ţ�Ƶ���Ϣ
access_key = 'JDfJ_laknrdt5UveDvgB46o_JD8bM8rhLkng_Xda'
secret_key = 'CQfkc_JlY6F7WII8zbZUfsy5U-OjStB7BEpZxz3c'
bucket_name = 'zyfzyfhaha'


def qiNiuAccess():

    # ������Ȩ����
    q = Auth(access_key, secret_key)
    return q

#ƴװ������Ϣ
def packageLocalInfo():

    #��ȡ�ļ�������Ҫ�ϴ����ļ�
    fileList = (os.listdir(fileDir))
    fileListLength = len(fileList)
    try:
        # ��ӡ�ļ����ڵ��ļ����б�
        if(fileListLength != 0):
            print ("�ļ����ڹ���%d���ļ����ֱ�Ϊ��" %fileListLength)
            for i in range(fileListLength):
                print (" %s" %fileList[i])

            # ƴװ�ϴ�����Ҫ�ı���·��
            localFileList = []
            for i in range(fileListLength):
                localFileList.append(fileDir + '\\' + fileList[i])

            #ƴװ�ϴ�����ţ�ƺ󱣴���ļ���
            keyList = []
            for i in range(fileListLength):
                keyList.append(prefix + fileList[i])
                keyListLength = len(keyList)
            print ("�ϴ�����ţ�Ƶ�%d���ļ����ֱ�Ϊ��" %keyListLength)
            for j in range(fileListLength):
                print (" %s" %keyList[j])
        else:
            print("����ļ��о�Ȼ�ǿյģ��ǻ�����ë����")
            os._exit(0)
    except:
        traceback.print_exc()
    return keyList, keyListLength, localFileList


def uploadPics(func1,func2):
    try:
        q = func1()
        resultTuple = func2()
        keyList = resultTuple[0]
        keyListLength = resultTuple[1]
        localFileList = resultTuple[2]

        #�����ϴ� Token
        tokenList = []
        for i in range(keyListLength):
            token = q.upload_token(bucket_name,keyList[i],3600)
            tokenList.append(token)

        #�ϴ�ͼƬ
        infoList = []
        for i in range(keyListLength):
            ret, info = put_file(tokenList[i],keyList[i],localFileList[i])
            infoList.append(info)
        print (infoList)
    except:
        traceback.print_exc()


if __name__ == '__main__':
    uploadPics(qiNiuAccess,packageLocalInfo)



