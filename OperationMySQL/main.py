# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from MySQL import OperationMySQL
if __name__ == '__main__':
	test = OperationMySQL.OperationMySQL(
		host='127.0.0.1',
		user='root',
		password='',
		db='op',
	)
	test.set_mysql_sql("insert INTO ops_aliyunkey (accessKe,accessKeySecret,keyType) VALUES('23423433','234324324234',1)")
	test.execute_only_sql('insert')

