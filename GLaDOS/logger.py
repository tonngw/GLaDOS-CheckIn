import logging


# 创建logger对象
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)  # log等级总开关

formatter = logging.Formatter("[%(process)d] [%(levelname)s]: %(asctime)s ---> %(message)s")

# 控制台handler
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO) # log等级的开关
stream_handler.setFormatter(formatter)


# 添加到logger
logger.addHandler(stream_handler)
