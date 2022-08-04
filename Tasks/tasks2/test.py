def file_name(file_list):
    result=max(len(i) for i in file_list)
    final=[]
    for i in file_list:
        if len(i) > len(set(i)):
            print('В названии файла есть повторяющиеся символы')
            break
        else:
            for i in file_list:
                while len(i) != result:
                    i+='_'
                final.append(i)
            return final


file_list = ['qwef', 'asdfgh', 'qwe', 'zxcvgh']
