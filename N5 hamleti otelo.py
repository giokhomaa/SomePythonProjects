# import re  # re მოდული ტექსტიდან აშორებს სასურველ ნიშნებს ან ასოებს...
#
# punctuations = '[!?,]'  ###
#
# f1 = open('1.txt', 'r')
# book1 = f1.read()
# bk1 = book1.lower()
# bk1 = re.sub('[!?,.-:;$#"]', '', bk1)   # ვწერთ თუ რომელი სიმბოლოების მოშორება გვინდა, რათა გავიგოთ თუ რამდენი უნიკალური სიტყვაა ტექსტებში
# b1 = set(bk1.split())   # set-ის დამსახურებით განმეორებულ სიტყვებს მხოლოდ ერთხელ ბეჭდავს
# print(b1)
# print(len(b1))
#
# f2 = open('2.txt', 'r')
# book2 = f2.read()
# bk2 = book2.lower()
# bk2 = re.sub(punctuations, '', bk2)
# b2 = set(bk2.split())
# print(b2)
# print(len(b2))
#
# print("saerto unikaluri sityvebi: ", len(b1 | b2))  # b1 და b2 ში გაერთიანებული სიტყვების უნიკალურ სიტყვებს ითვლის, ანუ 7
# print("saerto sityvebi: ", len(b1 & b2))  # თვლის თუ რამდენი საერთო სიტყვაა ორივე ტექსტში
# print(b1-b2, len(b1 - b2))    # პირველი ფაილის 3 სიტყვა არ გვხვდბა მეორე ფაილში
# print(b2-b1, len(b2 - b1))    # მეორე ფაილის 2 სიტყვა არ გვხვდება მეორე ფაილში
# print(len(b1 ^ b2))    # საერთო რაოდენობა იმ სიტყვების რომლებიც არ გვხვდება ერთი-მეორეში
#
# f1.close()
# f2.close()


import re

punctuatuons = '[!?,.-:;$#"]'

f1 = open('hamleta.txt', 'r')
book1 = f1.read()
bk1 = book1.lower()
bk1 = re.sub(punctuatuons, '', bk1)
b1 = set(bk1.split())    # strip ფუნქცია აბზაცებს აშორებს
print('unikaluri sityvata saerto raodenoba hamletshi: ', len(b1))


f2 = open('oteloi.txt', 'r')
book2 = f2.read()
bk2 = book2.lower()
bk2 = re.sub(punctuatuons, '', bk2)
b2 = set(bk2.split())    # strip ფუნქცია აბზაცებს აშორებს
print('unikaluri sityvata saerto raodenoba oteloshi: ', len(b2))

print("saerto unikaluri sityvebi: ", len(b1 | b2))
print('saerto sityvebi: ', len(b1 & b2))
print('sityvebi romlebic ar aris me-2-shi: ', len(b1 - b2))
print('sityvebi romlebic ar aris pirvelshi: ', len(b2 - b1))
print('simetriuli sxvaoba: ', len(b1 ^ b2))
print('sul hamletshi aris: ', len(book1), 'sityva')
print('sul oteloshi aris: ', len(book2), 'sityva')

f1.close()
f2.close()






















