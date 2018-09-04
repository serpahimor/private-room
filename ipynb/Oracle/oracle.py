#orcl类：是一个数据库
#login属性为xxxxx
#方法为execute，close
import pandas as pd
import cx_Oracle as oracle
class orcl(object):    
    def __init__(self,login='BLS/bls2016@116.62.196.255:1521/orcl11g.us.oracle.com'):
        self.db = oracle.connect(login, encoding = "UTF-8", nencoding = "UTF-8")
    def execute(self,sql="select * from ASSI1001"):
        cr = self.db.cursor()
        df=pd.DataFrame(cr.execute(sql).fetchall())
        df.columns=[i[0] for i in cr.description]
        return df
    def close(self):
        self.db.close()