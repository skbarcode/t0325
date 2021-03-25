from django.shortcuts import render
import time
# Create your views here.
class AutoSerialNumber(object):
    """创建OA单号"""

    def __init__(self):
        # J201906120001
        # self.fd_apply_no = ApplicationBasicFormModel.delete_objects.filter(fd_apply_no__contains="J").order_by(
        #     "-fd_apply_no").first().fd_apply_no
        self.fd_apply_no = "J20196120001"
        self.date_str = self.fd_apply_no[1: 9]  # 日期字符串
        self._serial_number = self.fd_apply_no[9:]  # 流水号字符串
        self._serial_number = 0  # 流水号

    @property
    def serial_number(self):
        return self._serial_number

    @serial_number.setter
    def serial_number(self, value):
        if isinstance(value, int):
            self._serial_number = value
        else:
            self._serial_number = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.serial_number += 1
        # 生成一个固定4位数的流水号
        return "{0:03d}".format(self.serial_number)

    def __call__(self, *args, **kwargs):
        # 返回生成序列号(日期加流水号)
        return "J" + self.date_str + next(self)

    # 时间格式化,最好是用定时器来调用该方法
    def timed_clear_serial_number(self):
        """用于每天定时清除流水号"""

        self.serial_number = 1
        self.date_str = time.strftime("%Y%m%d", time.localtime(time.time()))



a=AutoSerialNumber()
print(a(1))