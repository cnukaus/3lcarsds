def collatz(high=1000):
    all_list=[]
    for i in range(1, high+1):
        global loop_list
        loop_list=[i]
        global loop_num
        loop_num=i
        while loop_num != 1:
            if bool(loop_num%2):
                loop_num = 3*loop_num
                loop_num += 1
                loop_list.append(loop_num)
                try:
                    num = num//2
                except BaseException:
                    num/=2
                loop_list.append(loop_num)
if __name__ == "__main__":
    pass