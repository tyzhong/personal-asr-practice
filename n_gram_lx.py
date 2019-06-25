# coding=utf-8
import re
import pysnooper

with open('data.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()

# print(data[0])

pattern = re.compile(r'\(.*\)')
print(type(pattern))
data = [pattern.sub('', lines) for lines in data]
# print(data[0])

data = [line.replace('……', '。') for line in data if len(line) > 1]
# print(data[0])

'''判断是否为乱码，不是乱码返回True，是乱码返回False'''

def is_uchar(uchar):
    '''通过unicode编码进行判断'''
    '''判断是否为汉字'''
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    """判断是否为数字"""
    if uchar >= u'\u0030' and uchar <= u'u0039':
        return True
    '''判断是否为英文字母'''
    if (uchar >= u'\u0041' and uchar <= u'\u005a') or (uchar >= u'\u0061' and uchar <= u'\u007a'):
        return True
    if uchar in ('，', '。', '：', '？', '“', '”', '！', '；', '、', '《', '》', '——'):
        return True
    return False

#将每行list合成一个长的字符串,由之前的list格式变为string，同时去掉了全面的‘\ufeff’
data = ''.join(data)
data = [char for char in data if is_uchar(char)]
data = ''.join(data)
print(data[0:100])


def n_gram(data,n):
    d={}
    for i in range(len(data)-n):
        if data[i:len(data)-n] not in d:
            d[data[i:i+n]]={}
            d[data[i:i+n]][data[i+n]]=1
        else:
            if data[i+n] not in d[data[i:i+n][i:i+n]]:
                d[data[i:i+n][i:i+n]][data[i+n]]=1
            else:
                d[data[i:i+n]][data[i+n]]+=1
    return d

d=n_gram(data,3)
print(len(d))

# outputs ='地府里受'
# for i in range(100):
#     inputs=outputs[-3:]
#     next_word=sorted(d[inputs].items(),key=lambda x:x[1],reverse=True)[0][0]
#     outputs +=next_word
#
# print(outputs)


@pysnooper.snoop()
def debug_lx(d):
    outputs = '地府里受'
    for i in range(100):
        inputs = outputs[-3:]
        tmp_word=sorted(d[inputs].items(), key=lambda x: x[1], reverse=True)
        next_word = sorted(d[inputs].items(), key=lambda x: x[1], reverse=True)[0][0]
        outputs += next_word
    print(outputs)

debug_lx(d)



