#orcl类：是一个数据库
#login属性为xxxxx
#方法为execute，close
import pandas as pd
import cx_Oracle as oracle
class orcl(object):    
    def __init__(self,login='BLS/bls2016@116.62.196.255:1521/orcl11g.us.oracle.com'):
        self.db = oracle.connect(login, encoding = "UTF-8", nencoding = "UTF-8")
    def execute(self,database,col='*'):
        cr = self.db.cursor()
        sql="select {} from {}".format(col,database)
        print('|>',sql)
        print('-'*10)
        df=pd.DataFrame(cr.execute(sql).fetchall())
        try:
            df.columns=[i[0] for i in cr.description]
            print(df.head(1))
            print('-'*10)
            return df
        except Exception as e:
            print('Export data is not success. \nCause reason:\n{}\nPlease try it again!'.format(e))
    def close(self):
        self.db.close()