import yaml
def load_yaml(path):
    f = open(path, encoding="utf-8") # 打开文件
    s = f.read() # 读取文件内容
    data = yaml.safe_load(s)
    return data