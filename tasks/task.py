from typing import Any, Tuple, List

def get_pairs(lst: List[Any]) -> List[Tuple[Any, Any]]:
    # TODO: Add your code here
    new_list =[]
    if len(lst) <= 1:
        return []
    else:
        for i in range(0, len(lst) - 1):
            new_l = []
            new_l.append(lst[i])
            new_l.append(lst[i+1])
            new_list.append(tuple(new_l))

    return new_list



