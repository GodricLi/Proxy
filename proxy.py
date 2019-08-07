# _*_ coding=utf-8 _*


from abc import abstractmethod, ABCMeta


class Subject(metaclass=ABCMeta):
    @abstractmethod
    def get_content(self):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


# 真实代理
class RealSubject(Subject):
    """
    读取文件，写入文件
    """
    def __init__(self, filename):
        self.filename = filename
        print("Start reading file:")
        with open(filename, 'r', encoding='utf-8') as f:
            self.content = f.read()

    def get_content(self):
        return self.content

    def set_content(self, content):
        with open(self.filename,'w',encoding='utf-8') as f:
            f.write(content)


# 虚代理
class VirtualProxy(Subject):
    """
    刚开始不加载文件内容，只显示模糊的图像。选中文件后进行文件的加载
    """
    def __init__(self, filename):
        self.filename = filename
        self.sub = None

    def get_content(self):
        if not self.sub:
            self.sub = RealSubject(self.filename)
        return self.sub.get_content()

    def set_content(self, content):
        if not self.sub:
            self.sub = RealSubject(self.filename)
        return self.sub.set_content(content)


# 保护代理
class ProjectProxy(Subject):
    """
    限制操作权限
    """
    def __init__(self, filename):
        self.sub = RealSubject(filename)

    def get_content(self):
        return self.sub.get_content()

    def set_content(self, content):
        return "无权限"


# real = RealSubject('test.txt')    # 真实代理实例化时就会读取文件内容
virtual = VirtualProxy('test.txt')
virtual.get_content()               # 虚代理在调用方法后才会读取文件内容
con = ProjectProxy('test.txt')
print(con.get_content())
print(con.set_content('666'))