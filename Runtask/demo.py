from DataBaseInfo.MysqlInfo.MysqlTools import MysqlCurd
from datetime import datetime

# 获取当前时间
current_time = datetime.now()
# 格式化当前时间
end_run_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
start_run_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
update_sql_success = F"update   data_oms  set  是否已完成 =1 ,填报开始时间 = '{start_run_time}',填报结束时间 = '{end_run_time}' where   日期='2024=01=19' and 电场名称='金燕风电场'"

# MC.update(update_sql_success)
new_nanfang = F'../DataBaseInfo/MysqlInfo/new_nanfang.yml'
NEWMC = MysqlCurd(new_nanfang)
print(NEWMC.query_sql())
NEWMC.update(update_sql_success)