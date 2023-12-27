
def index_all(data: list, value: int) -> list:
  indexes = []
  for i, item in enumerate(data):
    if isinstance(item, list):
      for index in index_all(item, value):
         indexes.append([i] + index)
    elif item == value:
        indexes.append([i])
  return indexes

      
test_list = [[[1,2,3],2,[1,3]],[1,2,3]]

print(index_all(test_list, 2))
