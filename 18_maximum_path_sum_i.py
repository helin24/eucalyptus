def max_sum(alist):
    triangle = {}
    size = len(alist)
    index = 0
    inserted_so_far = 0
    level = 1
    while index < size:
        triangle[index] = {'value':alist[index], 'distance':None, 'children':[]}
        if index + level < size:
            triangle[index]['children'] = [index + level, index + level + 1]
        inserted_so_far += 1
        index += 1
        if inserted_so_far == level:
            level += 1
            inserted_so_far = 0

    stack = [0]
    while stack:
        current_index = stack.pop()
        node = triangle[current_index]

        children = node['children']
        if children == []:
            node['distance'] = node['value']
            continue
        else:
            left = triangle[children[0]]
            right = triangle[children[1]]

            if left['distance'] == None or right['distance'] == None:
                stack.append(current_index)
                stack.extend(children)
            else:
                node['distance'] = max(left['distance'], right['distance']) + node['value']



    return triangle[0]['distance']
                

        
        


print max_sum([75,95,64,17,47,82,18,35,87,10,20,4,82,47,65,19,1,23,75,3,34,88,2,77,73,7,63,67,99,65,4,28,6,16,70,92,41,41,26,56,83,40,80,70,33,41,48,72,33,47,32,37,16,94,29,53,71,44,65,25,43,91,52,97,51,14,70,11,33,28,77,73,17,78,39,68,17,57,91,71,52,38,17,14,91,43,58,50,27,29,48,63,66,4,68,89,53,67,30,73,16,69,87,40,31,4,62,98,27,23,9,70,98,73,93,38,53,60,4,23])

