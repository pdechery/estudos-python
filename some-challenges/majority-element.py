class Solution:
    @staticmethod
    def majorityElement(nums: list[int]) -> int:
        
        maj = len(nums) // 2
        resp = 0

        report = dict()
        for i in nums:
            if not report.get(i):
                report[i] = 0
            report[i] += 1

        for x in report.keys():
            if report[x] > maj:
                resp = x
                break

        return x

   
    @staticmethod
    def addExclamation(text: str) -> str:
        
        string_list = [i for i in text]

        for i in range(len(string_list)):
            if string_list[i] == "!":
                if string_list[i] != string_list[i-1]:
                    string_list.insert(i,"!")

        return ''.join(string_list)


    @staticmethod
    def keyword_values(b=0,c=1,d=2):
        return b,c,d
 

nums = [2,2,1,1,1,2,2]
text = "crazy! just crazy!!!"
#print(f'nums {nums}')
#s = Solution().majorityElement(nums)
s = Solution().addExclamation(text)
#s = Solution().keyword_values('a',2,3)
print(f'resposta: {s}')
