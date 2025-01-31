def ONE_E(receive_dict,size):
    receive_dict=list(set(receive_dict))
    data = {"Words": {}, "Bits": {}} 
    dict_data = {}

    for item in receive_dict:
        key = item[0]  
        value = int(item[1:]) 
        if key not in dict_data:
            dict_data[key] = [] 

        dict_data[key].append(value)

    for key in dict_data:
        dict_data[key].sort()
    #print("---------------------",dict_data)
    send_dict={}
    if(size!=0):  
        for key in dict_data:
            while dict_data[key]:  
                start = min(dict_data[key])
                end = start + size - 1
            #------------Satrt-Logic----------------
                X=dict_data[key]
                count = 0
                found = None
                result = []
                for i in range(end, start - 1, -1):
                    if i in X:
                        found = i
                        break

                if found is None:
                    found=0

                for i in range(start, found + 1):
                    if(count!=size):
                        count += 1
                        result.append(i)
            #------------End-Logic----------------
                #print(f"Result: {result}, Count: {count}")
                X[:] = [x for x in X if x not in result]  
                send_dict[key+str(start)]=count


        for key, value in send_dict.items():
            category = key[0]  
            #For Words
            if category in {'D','W','A'}:
                data["Words"].setdefault(category, {})[key] = value
            #For Bits
            elif category in {'X','Y','M'}:
                data["Bits"].setdefault(category, {})[key] = value
            else:
                print(f"ERROR:Unknown category {key}, please specify = {key[0]} is Words or Bits in code!")
        
    return data
