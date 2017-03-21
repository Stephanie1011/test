# -*- coding=UTF-8 -*-
if __name__ == '__main__':
	f = open("test.txt","r", encoding="UTF-8")
	b = f.readline().strip()
	a = "鹤"
	if a==b:
		print("good1")
	b = f.readline().strip()
	c = "鶴"
	if (b==c):
		print("good2")
	f.close()
