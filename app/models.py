from django.db import models


class Client(models.Model):
    name = models.CharField(verbose_name='收件方', max_length=64, unique=True)
    contact_person = models.CharField(verbose_name='联系人', max_length=12, blank=True, null=True)
    telephone = models.CharField(verbose_name='联系号码', unique=True, max_length=13)
    e_mail = models.EmailField(verbose_name='邮箱')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '客户信息'
        verbose_name = '客户信息'


class DeliveryDate(models.Model):
    name = models.CharField(verbose_name='交货时间', max_length=64, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '交货时间'
        verbose_name = '交货时间'


class DeliveryMethod(models.Model):
    name = models.CharField(verbose_name='交货方式', max_length=64, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '交货方式'
        verbose_name = '交货方式'


class PaymentTerms(models.Model):
    name = models.CharField(verbose_name='付款方式', max_length=64, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '付款方式'
        verbose_name = '付款方式'


class WarrantyPolicy(models.Model):
    name = models.CharField(verbose_name='保修政策', max_length=64, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '保修政策'
        verbose_name = '保修政策'


class ServicePolicy(models.Model):
    name = models.CharField(verbose_name='服务政策', max_length=64, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '服务政策'
        verbose_name = '服务政策'


class ValidPeriod(models.Model):
    name = models.CharField(verbose_name='有效期', max_length=64, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '有效期'
        verbose_name = '有效期'


class Unit(models.Model):
    name = models.CharField(verbose_name='单位', max_length=64, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '单位'
        verbose_name = '单位'


class Goods(models.Model):
    name = models.CharField(verbose_name='产品名称', max_length=64, unique=True)
    unit = models.ForeignKey(Unit, verbose_name='单位', on_delete=models.CASCADE)
    remarks = models.CharField(verbose_name='备注', max_length=64, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '产品名称'
        verbose_name = '产品名称'


class Quotation(models.Model):
    Qid = models.CharField(verbose_name='订单编号', unique=True, primary_key=True, max_length=13)
    date = models.DateField(verbose_name='日期', auto_now=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='client', verbose_name='客户信息',default='')
    goods = models.ForeignKey(verbose_name='产品名称', to=Goods, related_name='goods', on_delete=models.CASCADE,default='')
    unit = models.ForeignKey(to=Unit, related_name='unit', verbose_name='单位', on_delete=models.CASCADE,default='')
    qty = models.FloatField(verbose_name='数量', unique=True)
    price = models.FloatField(verbose_name='金额')
    amount = models.FloatField(verbose_name='金额')
    remarks = models.CharField(verbose_name='备注', blank=True, null=True, max_length=128)
    deliveryDate = models.ForeignKey(to='DeliveryDate', verbose_name='交货时间', on_delete=models.CASCADE,default='')
    deliveryMethod = models.ForeignKey(to='DeliveryMethod', verbose_name='交货方式', on_delete=models.CASCADE,default='')
    paymentTerms = models.ForeignKey(to='PaymentTerms', verbose_name='付款方式', on_delete=models.CASCADE,default='')
    warrantyPolicy = models.ForeignKey(to='WarrantyPolicy', verbose_name='保修政策', on_delete=models.CASCADE,default='')
    servicePolicy = models.ForeignKey(to='ServicePolicy', verbose_name='服务政策', on_delete=models.CASCADE,default='')
    validPeriod = models.ForeignKey(to='ValidPeriod', verbose_name='有效期', on_delete=models.CASCADE,default='')

    class Meta:
        verbose_name_plural = '报价单'
        verbose_name = '报价单'
