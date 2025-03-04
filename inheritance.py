from math import ceil

class Numbers:
    def __init__(self, mixlist):
        self.mixedlist = mixlist  

    def _num(self):
        odd = []
        even = []
        prime = []
        name = ["Odd", "Even", "Prime"]
        nums = [odd,even,prime]
        res = dict(zip(name,nums)) 

        for n in self.mixedlist:  
            if isinstance(n, int): 
                if n % 2 == 1:
                    odd.append(n)
                else:
                    even.append(n)

                if n > 1:
                    is_prime = True
                    if n == 2:  
                        prime.append(n)
                        continue
                    if n % 2 == 0: 
                        is_prime = False
                    else:
                        for x in range(3, ceil(n**0.5) + 1, 2):
                            if n % x == 0:
                                is_prime = False
                                break
                    if is_prime:
                        prime.append(n)

        print("Odd Numbers:", odd)
        print("Even Numbers:", even)
        print("Prime Numbers:", prime)
        print("The result is:", res)
class Text(Numbers):
    def __init__(self, mixlist):
        super().__init__(mixlist)
    
    def _txt(self):
        letter_counts = {}  

        for word in self.mixedlist:  
            if isinstance(word, str):  
                letter_count = {}
                
                
                for letter in word:
                    if letter in letter_count:
                        letter_count[letter] += 1
                    else:
                        letter_count[letter] = 1

                
                formatted_count = [{letter: count} for letter, count in letter_count.items()]
                
                letter_counts[word] = formatted_count
        
        print("\nLetter Count Dictionary:")
        print(letter_counts)

        # repeat = []
        # unique = []
        # for m in self.mixedlist:  
        #     if type(m) == str:
        #         print(m)
        #         for x in m:
        #             print(x)
        #             if x in unique:
        #                 unique.remove(x)
        #                 repeat.append(x)
        #                 # print("repeat:", repeat)
        #             else:
        #                 unique.append(x)
        #                 # print("Else part:", unique) 
        # print("repeat:", repeat)
        # print("Else part:", unique)   
mixList = [10, 12, "Apple", "Banana", 123, 2, 5, "Orange"]
x = Numbers(mixList)
y= Text(mixList)
y._txt()
x._num()
