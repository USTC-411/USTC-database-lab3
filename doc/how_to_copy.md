# 搬砖流程

> 后续如果有其他待补充的话会以git形式更新

1. 在和``model.py`` 同级的``form.py``中增加和模型对应的两张表（以myClass为例）  
    > 这个两个表格的作用在于自动检查输入以及简化代码
   1. myClass
   2. myClass_modify
2. 在``urls.py``中配置对应的路由
3. 复制粘贴并修改``ManageClass.html``
4. 复制粘贴并修改``class.py``
