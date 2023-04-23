from typing import List

class Sort_methods:
    def __init__(self,list:List):
        self.list = list

    def selection_sort(self):
        un_sorted_list = self.list
        un_sorted_list.append(0)

        for i in range(len(un_sorted_list)-1):
            max_value = max(un_sorted_list[:-1-i])
            un_sorted_list[-2-i],un_sorted_list[un_sorted_list.index(max_value)] = max_value,un_sorted_list[-2-i]

        sorted_list = un_sorted_list[:-1]

        return sorted_list

    def bubble_sort(self):
        un_sorted_list = self.list
        un_sorted_list.append(0)

        for i in range(len(un_sorted_list)):
            for j in range(len(un_sorted_list[:-1-i])):
                now = un_sorted_list[0]

        sorted_list = un_sorted_list[:-1]

        return sorted_list

    def insertion_sort(self):
        un_sorted_list = self.list
        sorted_list = [un_sorted_list[0]]

        for i in range(1,len(un_sorted_list)):
            key = un_sorted_list[i]

            for j in range(i):
                if un_sorted_list[i-j-1] > key :
                    un_sorted_list[i-j-1], un_sorted_list[i-j] = un_sorted_list[i-j], un_sorted_list[i-j-1]

        return un_sorted_list

    def insertion_sort(self):
        un_sorted_list = self.list
        sorted_list = [un_sorted_list[0]]

        for i in range(1,len(un_sorted_list)):
            key = un_sorted_list[i]

            for j in range(i):
                if un_sorted_list[i-j-1] > key :
                    un_sorted_list[i-j-1], un_sorted_list[i-j] = un_sorted_list[i-j], un_sorted_list[i-j-1]

        return un_sorted_list














            
            
            
            