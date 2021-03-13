import logging.handlers  # 导包注意

# 实例化日志器
logger = logging.getLogger()

# 日志级别
logger.setLevel(logging.INFO)

# 创建文件处理器
trfh = logging.handlers.TimedRotatingFileHandler(filename="./abc.log", when="midnight", interval=1,
                                                 backupCount=7, encoding="utf-8")

# 处理器添加日志级别 会覆盖掉 日志器设置日志级别
trfh.setLevel(logging.ERROR)

# 处理器 添加到 日志器
logger.addHandler(trfh)

# 信息输出
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("错误日志")
logging.critical("critical")
