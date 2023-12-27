import ast

def save_dic(dic: dict, path: str) -> bool:
  with open(path, 'w') as f:
    f.write(str(dic))
    return True

def load_dic(path: str) -> dict:
  with open(path, 'r') as f:
    dic = ast.literal_eval(f.read())
    return dic if isinstance(dic, dict) else False

target_dic = {1: 'a', 2: 'b', 3: 'c'}
path = './dict.txt'

save_dic(target_dic, path)
print(load_dic(path))