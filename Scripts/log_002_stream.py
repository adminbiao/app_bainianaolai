import logging

# 实例化logger
logger = logging.getLogger()

# 设置日志器级别
logger.setLevel(logging.ERROR)

# 实例化控制台处理器对象
sh = logging.StreamHandler()

# 将处理器对象 添加到 日志器对象
logger.addHandler(sh)

# 输出信息
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")