import numpy as np

def find_nn_1d_array(array_for_search, num_neighbors_desired):

        test_list_iterator = array_for_search.copy()

        test_list_mod = array_for_search.copy()

        neighbor_storage_list = []

        neighbor_eval_score = 999_999_999
                
        for number in test_list_iterator:
                
                neighbor_nil = test_list_mod[min(range(len(test_list_mod)), key = lambda i: abs(test_list_mod[i] - number))]
                
                neighbor_storage_list.append(neighbor_nil)

                test_list_mod.remove(neighbor_nil)
        
                for num_neighbor in range(num_neighbors_desired):
                
                        neighbor = test_list_mod[min(range(len(test_list_mod)), key = lambda i: abs(test_list_mod[i] - number))]
                                
                        neighbor_storage_list.append(neighbor)
                                
                        test_list_mod.remove(neighbor)

                neighbor_storage_list.sort()
                
                if neighbor_eval_score >= abs(sum(np.diff(neighbor_storage_list))):
                                
                        neighbor_eval_score = abs(sum(np.diff(neighbor_storage_list)))
                                                        
                test_list_mod = array_for_search.copy()
                        
                neighbor_storage_list = []

        return neighbor_eval_score

test_list = [0.1, 0.73, 2.01, 0.08, 1.49, 0.24, 0.35]
test_num_desired_neighbors = 3
print(find_nn_1d_array(test_list, test_num_desired_neighbors))



import numpy as np
def find_nn_in_list_1D(list_for_search, num_neighbors_desired):

        list_iterator = list_for_search.copy()

        list_mod = list_for_search.copy()

        neighbor_storage_list = []

        neighbor_eval_score = 999_999_999
                
        for number in list_iterator:
                
                neighbor_nil = list_mod[min(range(len(list_mod)), key = lambda i: abs(list_mod[i] - number))]
                
                neighbor_storage_list.append(neighbor_nil)

                list_mod.remove(neighbor_nil)
        
                for num_neighbor in range(num_neighbors_desired):
                
                        neighbor = list_mod[min(range(len(list_mod)), key = lambda i: abs(list_mod[i] - number))]
                                
                        neighbor_storage_list.append(neighbor)
                                
                        list_mod.remove(neighbor)
                
                neighbor_storage_list.sort()

                if neighbor_eval_score > abs(sum(np.diff(neighbor_storage_list))):
                                
                        neighbor_eval_score = abs(sum(np.diff(neighbor_storage_list)))
                        
                        nearest_neighbors_list = neighbor_storage_list.copy()
                                                        
                list_mod = list_for_search.copy()
                        
                neighbor_storage_list = []

        return nearest_neighbors_list

test_list = [1, 8, 14, 15, 17, 100, 35]
test_num_desired_neighbors = 2
print(find_nn_in_list_1D(test_list, test_num_desired_neighbors))


import numpy as np

N = 3
X = np.array([1, 8, 14, 15, 17, 100, 35]).astype(np.float32)

d = np.abs(X[None, :] - X[:, None])
np.fill_diagonal(d, np.inf)

min_array = d.min(0)

par = np.argpartition(min_array, N)

print((X[par[:N]]))


lst = [1, 8, 14, 15, 17, 100, 35]

#Make pairs and remove duplicates using a set
lst_pairs = set([tuple(sorted((x, y))) for x in lst for y in lst if x != y])

#Make a dictionary mapping a pair to distance
dist_dict = {k: k[1] - k[0] for k in lst_pairs}

#extract the top 3 by distance
nearest_n = sorted(dist_dict, key=lambda x: dist_dict[x])[:3]

#unpack the pairs to unique points
nearest_n_pts = set([pt for pair in nearest_n for pt in pair])
print(nearest_n_pts)