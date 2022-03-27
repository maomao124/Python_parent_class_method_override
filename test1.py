"""
 * Project name(项目名称)：Python父类方法重写
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/27 
 * Time(创建时间)： 13:10
 * Version(版本): 1.0
 * Description(描述)： 
 """


class Bird:
    # 鸟有翅膀
    def isWing(self):
        print("鸟有翅膀")

    # 鸟会飞
    def fly(self):
        print("鸟会飞")


class Ostrich(Bird):
    # 重写Bird类的fly()方法
    def fly(self):
        print("鸵鸟不会飞")


if __name__ == '__main__':
    # 创建Ostrich对象
    ostrich = Ostrich()
    # 调用 Ostrich 类中重写的 fly() 类方法
    ostrich.fly()
    ostrich.isWing()

    # 调用 Bird 类中的 fly() 方法
    Bird.fly(ostrich)
