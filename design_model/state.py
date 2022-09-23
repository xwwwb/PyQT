# 状态模式
"""
状态模式的核心思想是一个事物(对象)有多种状态，在不同的状态下所表现出来的行为和属性不一样
"""

from abc import ABCMeta, abstractmethod


class Context(metaclass=ABCMeta):
    """状态模式的上下文环境类"""

    def __init__(self):
        self.__states = []
        self.__cur_state = None
        # 状态发生变化依赖的属性，当这一变量由多个变量共通决定时可以将其定义成一个类
        self.__state_info = 0

    def add_state(self, state):
        if state not in self.__states:
            self.__states.append(state)

    def change_state(self, state):
        if state is None:
            return False
        if self.__cur_state is None:
            print("初始化为: {}".format(state.get_name()))
        else:
            print("由 {} 变为 {}".format(self.__cur_state.get_name(), state.get_name()))
        self.__cur_state = state
        self.add_state(state)
        return True

    def get_state(self):
        return self.__cur_state

    def _set_state_info(self, state_info):
        self.__state_info = state_info
        for state in self.__states:
            if state.is_match(state_info):
                self.change_state(state)
                # 此处是否应该有一个break

    def _get_state_info(self):
        return self.__state_info


class State:
    """状态类基类"""

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    @abstractmethod
    def is_match(self, state_info):
        # 状态的属性是否在当前的范围内
        return False

    @abstractmethod
    def behavior(self, context):
        # 行为，由具体的State类继承实现
        pass


class Water(Context):
    """水(H2O)"""

    def __init__(self):
        super(Water, self).__init__()
        self.add_state(SolidState("固态"))
        self.add_state(LiquidState("液态"))
        self.add_state(GaseousState("气态"))
        self.set_temperature(25)

    def get_temperature(self):
        return self._get_state_info()

    def set_temperature(self, temperature):
        self._set_state_info(temperature)

    def rise_temperature(self, step):
        """升高温度"""
        self.set_temperature(self.get_temperature() + step)

    def reduce_temperature(self, step):
        """降低温度"""
        self.set_temperature(self.get_temperature() - step)

    def behavior(self):
        """行为方法"""
        state = self.get_state()
        if isinstance(state, State):
            state.behavior(self)


# 单例的装饰器
def singleton(cls, *args, **kwargs):
    """构造一个单例的装饰器"""
    instance = {}

    def __singleton(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return __singleton


@singleton
class SolidState(State):
    """固态"""

    def is_match(self, state_info):
        """温度小于0会凝结成固态"""
        return state_info < 0

    def behavior(self, context):
        print("我性格高冷，当前体温: {}".format(context.get_temperature()))


@singleton
class LiquidState(State):
    """液态"""

    def is_match(self, state_info):
        return 0 <= state_info < 100

    def behavior(self, context):
        print("我性格温和，当前体温: {}".format(context.get_temperature()))


@singleton
class GaseousState(State):
    """气态"""

    def is_match(self, state_info):
        return state_info >= 100

    def behavior(self, context):
        print("我性格热烈，当前体温: {}".format(context.get_temperature()))


def test_state():
    water = Water()
    water.behavior()
    water.set_temperature(-4)
    water.behavior()
    water.rise_temperature(18)
    water.behavior()
    water.rise_temperature(110)
    water.behavior()


if __name__ == '__main__':
    test_state()



