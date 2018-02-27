
from django.db import connection
def dictfetchall(cursor):
    "将游标返回的结果保存到一个字典对象中"
    desc = cursor.description
    print(desc)
    retult =  [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]
    # retult_dict = dict(retult)
    return retult

'''执行django原始sql语句  并返回一个数组对象'''
def executeQuery(sql,param=[]):
        cursor = connection.cursor()  # 获得一个游标(cursor)对象
        if len(param):
            cursor.execute(sql,param)
        else:
            cursor.execute(sql)
        data_list = cursor.fetchall()
        # print (rawData) #((1, 'php', 0, 0), (2, 'python', 0, 0), (3, 'java', 0, 0))
        col_names = [desc[0] for desc in cursor.description]
        # print (col_names) #['id', 'category_name', 'sort', 'status']

        result = []#[{'id': 1, 'category_name': 'php', 'sort': 0, 'status': 0}, {'id': 2, 'category_name': 'python', 'sort': 0, 'status': 0}, {'id': 3, 'category_name': 'java', 'sort': 0, 'status': 0}]
        for row in data_list:
            objDict = {}
            # 把每一行的数据遍历出来放到Dict中
            for index, value in enumerate(row):
                # print (index, col_names[index], value)
                objDict[col_names[index]] = value

            result.append(objDict)

        # i = 0
        # result = {}
        # for data in data_list:
        #     data_dict = {}
        #     # print(data)
        #     for key, value in enumerate(data):
        #         data_dict[col_names[key]] = value
        #         # print(key, col_names[key], value)
        #     result[i] = data_dict
        #     i += 1

        # if len(result):
        #     result_dict = result[0]
        # else:
        #     result_dict = {}
        # print (result)

        return result