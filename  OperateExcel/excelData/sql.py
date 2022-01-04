# -*-coding:utf-8 -*-
"""
@Author: zhangyi
@Time: 2021/12/7 3:48 下午
@File: sql.py
@IDE: PyCharm
"""
#查询企业库中重复企业。按照企业名称和行业名称，得到相同行业、相同企业的信息
set_qiye = '''
SELECT
	zlc.company_name,zl.name
	FROM
	zy_lable_company  zlc
	RIGHT JOIN
	zy_lable zl
	on zlc.lable_id=zl.id
	WHERE
	company_name IN ( SELECT company_name FROM zy_lable_company GROUP BY company_name HAVING count( company_name ) >= 2 )
	ORDER BY
	company_name
'''
#查询去重后的企业id
qiye_id =  '''
select id,company_name,company_logo from zy_lable_company WHERE company_name ='%s'
'''
