import re

def fun(s):
    # return True if s is a valid email, else return False

    print(f'teste: {s}')
    
    username, url = s.split('@')
    website, extension = url.split('.')

    print(username)
    print(url)
    print(website)
    print(extension)

    testEmail = re.compile('[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-zA-Z]+')

    # resposta do discussions
    # match = re.search(r'^[\w\d-]+\@[a-zA-Z0-9]+\.\w?\w?\w?$',s)

    print(testEmail.match(s))

    if testEmail.match(s):
        return True 
    else:
        return False


def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    # n = int(input())
    # emails = []
    # for _ in range(n):
    #     emails.append(input())
    emails = [
        'lara@hackerrank.com',
        'brian-23@hackerrank.com',
        'britts_54@hackerrank.com'
    ]

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)