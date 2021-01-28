import json
data = {
    "name": ["jerry",'nickname'],
    "age": 26,
    "gender":"famale"
}
data1 = json.dumps(data) # 转换成字符串
print(data1,type(json.dumps(data)))

data2 = json.loads(data1) # 把字符串转换成json
print(data2, type(data2))

# json.dump() 把数据类型转换成字符串 并存储在文件中
# json.load(file_strem) 把文件打开
