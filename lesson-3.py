#1 методами строк очистить текст от знаков препинания;
#################
print( '(1) методами строк очистить текст от знаков препинания;')
print()
str = '!!!Погружение в IT-профессию!!! подразумевает постоянный контакт с изучаемыми технологиями, выполнение практических заданий и общение с наставником. Для этого мы создали собственную среду обучения.'

str = str.replace(',', '').replace('.', '').replace(';','').replace('—','').replace('«','').replace('»','').replace('?','').replace('!','').replace('(','').replace(')','')
print(str)

print()

#################
#2 сформировать list со словами (split);

#################
# x_srt=re.split(' ', x_srt)
# print(x_srt)
#################
#3 привести все слова к нижнему регистру (map);
#################
# new_srt=list(map(lambda x: x.lower(), x_srt))
# print(new_srt)
#################
#4 получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте;
#################
# dict_new={}
# for index in range(len(new_srt)):
#     dict_new[new_srt[index]]=new_srt.count(new_srt[index])
# print(dict_new)
#################
#5 вывести 5 наиболее часто встречающихся слов (sort), вывести количество разных слов в тексте (set).
#################
# # max=0
# # # list1=list(dict_new.values())
# # # for index in range(len(dict_new)):
# # #    if list1[index] > max:
# # #        max=list1[index]
# # # print (max)
# list5=[]
# list6=[]
# list6 = [1 for i in range(5)]
# list5=list(sorted(dict_new.values(), reverse=True))
# for i in range(5):
#     list6[i]=list5[i]
# print( list6)
# print(len(set(dict_new)))
#################