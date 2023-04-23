import binary_tree
import binary_tree
import make_list
import quick_sort
import sort_method

un_sorted_list = make_list.make_random_list(1,20,7)
#un_sorted_list = [20, 8, 7, 2, 17]
print(un_sorted_list,end='\n\n')

method = sort_method.Sort_methods(un_sorted_list)

#print(f'selection_sort:{method.selection_sort()}')
print(f'insertion_sort:{method.insertion_sort()}')