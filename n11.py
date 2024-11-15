def find_intersection(lists):
  if not lists:
    return []
  result =set(lists[0])
  for lst in lists[1:]:
    result.intersection_update(lst)
  return list(result)

lists =[[1,2,3], [2,3,4], [3,4,5]]
intersection=find_intersection(lists)
print(intersection)