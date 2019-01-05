import asyncio
import time

# @asyncio.coroutine
# def hello():
#     print("Hello world!")
#     # 异步调用asyncio.sleep(1):
#     r = yield from asyncio.sleep(1)
#     print("Hello again!")
#
# # 获取EventLoop:
# loop = asyncio.get_event_loop()
# # 执行coroutine
# loop.run_until_complete(hello())
# loop.close()


@asyncio.coroutine
def test():
    """
    测试
    :return:
    """
    print('start')
    asyncio.sleep(3)
    print('end')

if __name__ == '__main__':
    task_list = [test(), test()]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(task_list))
    loop.close()
