import logging

# 创建日志器对象
logger = logging.getLogger()

# 设置日志器log级别
logger.setLevel(logging.INFO)


""" 因为处理器没有声明 也没有绑定到日志器，所以控制台输出走默认日志级别"""
# 日志信息输出
logger.debug("debug信息")
logger.info("info信息")
logger.warning("warning信息")
logger.error("error信息")
logger.critical("critical信息")
