import pandas as pd
import cx_Oracle as oracle
df_budan_reason=pd.read_excel(r'C:\Users\d\mes\data\补单原因.xls')
df_time=pd.read_excel('data/华广订单时间统计.xls')
df_huaguang_order_num=pd.read_excel('data/华广下单数量.xls')
df_yuanfang_order_num=pd.read_excel('data/园方下单数量.xls')
df_yuanfang_order_num.merge(df_huaguang_order_num).dropna()