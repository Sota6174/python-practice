# クラス
class Child(object):
    def __init__(self, name):
        self.name = name
        print("インスタンスの初期化")

    def say_hello(self):
        print("hello ", self.name)


# 継承(サブクラス)
class JapaneseChild(Child):
    def __init__(self, name):
        super().__init__(name)  # 親クラスのコンストラクタを呼び出し

    def say_hello(self):    # 親クラスのsay_hello()をオーバーライド
        print("おはよう ", self.name)


japanese_child = JapaneseChild("太郎")
japanese_child.say_hello()
