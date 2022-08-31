'''
Find a String

https://www.hackerrank.com/challenges/find-a-string

'''

def count_substring(string, sub_string):

    size = len(sub_string)

    result = list()

    for i in range(len(string)):
        
        f = string.find(sub_string,i)

        if f >= 0:
            result.append(f)

    return len(set(result))

if __name__ == '__main__':
    
    #string = input().strip()
    #sub_string = input().strip()

    string,sub_string = 'ininini','ini'
    
    count = count_substring(string, sub_string)
    print(count)