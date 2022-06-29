names = input(": ")
dic = {
    "moja":"one","mbili":"two","tatu":"three","nne":"four","tano":"five","sita":"six","saba":"seven","nane":"eight","tisa":"nine","sifuri":"zero"
}
names = names.split(" ")
tran = ""
for i in names:
	if i in dic:
		tran += " " + dic[i]
	else:
		tran += i

print(tran)
