def calculate_structure_sum(data_structure):
    sum = 0
    for elements in data_structure:
        if isinstance (elements, dict):
            index_els = elements.items()
            for index in index_els:
                for id_index in index:
                    if isinstance(id_index,int):
                        sum = id_index+sum
        for element in elements:
            if isinstance (element, int):
                sum = element + sum
            if isinstance (element, str):
                sum = len(element) + sum
            if isinstance (element, dict):
                index_el = element.items()
                for index in index_el:
                    for id_index in index:
                        if isinstance (id_index,int):
                            sum = id_index + sum
                        if isinstance (id_index, str):
                            sum = len(id_index) + sum
            if isinstance (element, list):
                for index_el in element:
                    if isinstance (index_el, set):
                        for params_index_el in index_el:
                            for par_params_index_el in params_index_el:
                                if isinstance (par_params_index_el, int):
                                    sum = par_params_index_el + sum
                                if isinstance (par_params_index_el, str):
                                    sum = len(par_params_index_el) + sum
                                if isinstance (par_params_index_el, tuple):
                                    for id_par_params_index_el in par_params_index_el:
                                        if isinstance (id_par_params_index_el, str):
                                            sum = len(id_par_params_index_el) + sum
                                        if isinstance (id_par_params_index_el, int):
                                            sum = id_par_params_index_el + sum
    return sum
data_structure = ([1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}]))
result = calculate_structure_sum(data_structure)
print(result)
