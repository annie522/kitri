# # compare data
# max_dict_z = dict_z[max(dict_z, key=lambda i: dict_z[i])]
# predict_list = []
# true_list = []
# o_x_list = []
# for one_predict in predictions:
#     predict_list.append(dict_z.keys()[dict_z.values().index(max_dict_z - one_predict)])  # 얘가 우리 머신러닝이 예측한 진단명
#
# for one_batch in y_batch:
#     true_list.append(dict_z.keys()[dict_z.values().index(
#         max_dict_z - one_batch.tolist().index(1))])  # tolist == 쿼리를 즉시 평가하고 반환된 쿼리결과 포함
#
# for num in range(len(predict_list)):
#     if predict_list[num] == true_list[num]:
#         o_x_list.append("O")
#     else:
#         o_x_list.append("X")

dic = {1:'a'}
print (dic)
dic_k = (dic.keys())
print ('1',dic_k)
dic_values = dic.values()
print (dic_values)
print ((list(dic_values))[0])
dic_values_list = list(dic_values)
print (dic_values_list[0])
dic_values_index = (dic_values_list.index('a'))
print (dic_values_index)
