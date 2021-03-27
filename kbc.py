# print("\t***************************************************")
# print("\t\t\tWelcome to KBC game!!\n")
# print("\t\tI hope you will enjoy playing the game")
# print("\t***************************************************")
# print()
# print()
# question_list = ["Q1.What is the capital of India?", "Q2.Where is Navgurukul?", "Q3.Where is Taj Mahal situated in India?", "Q4.The value of π (Pai) was first given by?", "Q5.Delhi became capital of India in?"]
# option_list = [["1.Delhi", "2.Bengal", "3.Bihar", "4.Chennai"], ["1.Himachal Pradesh", "2.Mumbai", "3.UP", "4.Goa"], ["1.Agra", "2.Pungab", "3.Haryana", "4.Pondicherry"], ["1.Einstein", "2.Aryabhatt", "3.Newton", "4.Abdul Kalam"], ["1.1910", "2.1912","3.1911", "4.1915"]]
# answers = [1,1,1,2,3]
# wr=[2,3,4,1,2]
# s=0
# l=0
# t=True
# for i in range(len(question_list)):
# 	print(question_list[i])
# 	for j in option_list[i]:
# 		print(j)
# 	print()
# 	r=input('do you want 50-50 lifeline ;; yes/no  ')
# 	if r=='y':
# 		print(wr[s],answers[l])
# 		s+=1
# 		l+=1
# 	elif r=="n":
# 		print("please trying doing the question:  ")
# 	else:
# 		print("yes or no choose ker\n")
# 	ans = int(input("Choose your answers: "))
# 	print()
# 	if ans==answers[i]:
# 		print("\t\tCongratulations!you entered the right answers!!")
# 		print()
# 	else:
# 		print("\t\tOpp!you entered the wrong answers")
# 		print()
# 		t=False
# 		break
# if t==True:
# 	print("congratulations for attempting all the questions!!")