def loop_backwards():
    def backwards(times):
        num = 1
        for i in range(times):
            if num%3 == 1:
                num-=1
                try:
                    num//=3
                except BaseException:
                    print("B 1")
                    num/=3
                    print("A 1")
            else:
                num*=2
        return num
    try:
        SAVE_DATA_FILE="bwds_cltz_conject_max.txt"
        i=0 ## i for iterations
        def existing(file_name):
            if type(file_name) == str:
                try:
                    file_name = open(file_name, "r")
                    file_name.close()
                except BaseException:
                    return False
            else:
                 raise BaseException("???")
            
        if not existing(SAVE_DATA_FILE):
            while True:
                i+=1
                with open(SAVE_DATA_FILE, "a") as data_file:
                    data_file.write(str(backwards(i)))
    except BaseException as msg:
        print("Err2")
        print(msg)
loop_backwards()