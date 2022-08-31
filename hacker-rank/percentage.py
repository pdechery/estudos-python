'''
Find the average of specified dict item, which is a list

Example input:

Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60

'''

students_marks = {
    'Krishna':[67, 68.6, 69],
    'Arjun':[70, 98, 63],
    'Malika':[52, 56, 60]
}

aluno = students_marks['Malika']

average = sum(aluno)/len(aluno)

'''
a/b     division showing float result
a//b    division showing integer result
'''

if __name__ == '__main__':
    
    print("{:.2f}".format(average)) # 2 casas decimais