import numpy as np
from PIL import Image
import pickle



def pretreat(image):
	image = image.convert('L')
	im = np.array(image)
	for i in range(im.shape[0]):
		for j in range(im.shape[1]):
			if im[i,j] == 0:
				im[i,j]=0
			else:
				im[i,j]=1
	return im
				



def feature(A):  
    midx=int(A.shape[1]/2)+1
    midy=int(A.shape[0]/2)+1
    A1=A[0:midy,0:midx].mean()
    A2=A[midy:A.shape[0],0:midx].mean()
    A3=A[0:midy,midx:A.shape[1]].mean()
    A4=A[midy:A.shape[0],midx:A.shape[1]].mean()
    A5=A.mean()
    AF=[A1,A2,A3,A4,A5]
    return AF

#切割图片并返回每个子图片特征
def incise(im):
    #竖直切割并返回切割的坐标
    a=[];b=[]
    if any(im[:,0]==1):
        a.append(0)
    for i in range(im.shape[1]-1):
        if all(im[:,i]==0) and any(im[:,i+1]==1):
            a.append(i+1)
        elif any(im[:,i]==1) and all(im[:,i+1]==0):
            b.append(i+1)
    if any(im[:,im.shape[1]-1]==1):
        b.append(im.shape[1])
    #水平切割并返回分割图片特征
    names=locals();AF=[]
    for i in range(len(a)):
        names['na%s' % i]=im[:,range(a[i],b[i])]
        if any(names['na%s' % i][0,:]==1):
            c=0
        elif any(names['na%s' % i][names['na%s' % i].shape[0]-1,:]==1):
            d=names['na%s' % i].shape[0]-1    
        for j in range(names['na%s' % i].shape[0]-1):
            if all(names['na%s' % i][j,:]==0) and any(names['na%s' % i][j+1,:]==1):
                c=j+1
            elif any(names['na%s' % i][j,:]==1) and all(names['na%s' % i][j+1,:]==0):
                d=j+1
        names['na%s' % i]=names['na%s' % i][range(c,d),:]
        AF.append(feature(names['na%s' % i]))    #提取特征
       
    return AF

def training():
    train_set={}
    for i in range(11):
        value=[]
        for j in range(15):
            ima=Image.open(str(i)+'//'+str(i)+'-'+str(j)+'.png')
            im=pretreat(ima)
            AF=incise(im)         #切割并提取特征
            value.append(AF[0])
        train_set[i]=value
    #把训练结果存为永久文件，以备下次使用
    output=open('train_set.pkl','wb')
    pickle.dump(train_set,output)
    output.close()
    return train_set
    
#计算两向量的距离
def distance(v1,v2):
    vector1=np.array(v1)
    vector2=np.array(v2) 
    Vector=(vector1-vector2)**2
    distance = Vector.sum()**0.5
    return distance

#用最近邻算法识别单个数字
def knn(train_set,V,k):
    key_sort=[11]*k
    value_sort=[11]*k
    for key in range(11):
        for value in train_set[key]:
            d=distance(V,value)
            for i in range(k):#从小到大排序
                if d<value_sort[i]:
                    for j in range(k-2,i-1,-1):
                        key_sort[j+1]=key_sort[j]
                        value_sort[j+1]=value_sort[j]
                    key_sort[i]=key
                    value_sort[i]=d
                    break
    max_key_count=-1
    key_set=set(key_sort)
    for key in key_set:   #统计每个类别出现的次数
        if max_key_count<key_sort.count(key):
            max_key_count=key_sort.count(key)
            max_key=key
    return max_key
	
def identification(train_set,AF,k):
    result=''
    for i in AF:
        key=knn(train_set,i,k)
        #if key==10:
            #key='.'
        result=result+str(key)
    return result	
	
train_set=training()
ima=Image.open('123.png')
im=pretreat(ima)      #预处理
AF=incise(im)                  #分割并提取图片
result=identification(train_set,AF,7)      #knn识别	
print(result)
