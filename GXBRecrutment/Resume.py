#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：generalTools
@File ：Resume.py
@Author ：zhangyi
@Date ：2022/6/3 1:01 AM
"""
from gevent import monkey

monkey.patch_all()
import gevent
from gevent.queue import Queue
import json
from typing import Dict, Set, List, Any
import yaml
from HttpRequest.HttpRequest import HttpRequest
from OperationMySQL.MySQL import OperationMySQL
import random


class Resume:
	def __init__(
			self,
			envInfoConfigPath: str,
			careerMySQLObject: OperationMySQL.OperationMySQL,
			baseMySQLObject: OperationMySQL.OperationMySQL
	):
		self.__envInfoConfigPath = envInfoConfigPath
		self.__careerMySQLObject = careerMySQLObject
		self.__baseMySQLObject = baseMySQLObject
		self.__careerConnect = self.__careerMySQLObject.get_mysql_connect()
		self.__baseConnect = self.__baseMySQLObject.get_mysql_connect()
		self.__env = 'dev'
		self.__envInfoConfig = self.load_yaml_data(envInfoConfigPath)
		self.__token = None
		self.__studentInfo = None

	"""
	静态方法,加载yaml文件
	"""

	@staticmethod
	def load_yaml_data(
			yaml_path
	) -> Dict:
		with open(yaml_path, 'r') as f:
			data = yaml.load(f, Loader=yaml.FullLoader)
			return data

	"""
	数据库查出来结果取随机值
	"""

	@classmethod
	def random_value(
			cls,
			listSet: [Set, List],
			num: int
	):
		return random.sample(listSet, num)

	"""
	配置访问环境
	"""

	def set_env(
			self,
			env: str
	) -> None:
		envs = ['dev', 'dev01', 'alpha', 'bata', 'pro']
		if env in envs:
			self.__env = env
		else:
			print('配置环境错误，退出')
			exit(123)

	"""
	获取用户token
	"""

	def get_token(
			self,
			studentInfo: Dict
	) -> None:
		self.__studentInfo = studentInfo
		t = HttpRequest()
		t.set_header(self.__envInfoConfig['headers'])
		t.set_url(self.__envInfoConfig[self.__env]['requestDomain'] + self.__envInfoConfig['interfaceRequestPath'][
			'get_token'])
		t.set_params(
			studentInfo
		)
		try:
			reponsee = t.send_http_request('get')
			reponseJson = t.analysis_reponse_json_data(reponsee)
			self.__token = reponseJson['result']['token']
		except Exception as e:
			print("请求失败" + str(e))
			exit(123)

	"""
	学生基本信息，学生头像
	"""

	def __get_student_pic(
			self,
	) -> str:
		pic_list = [
			"https://wx-dev-image.oss-cn-beijing.aliyuncs.com/%E7%99%BE%E6%97%A5%E6%8B%9B%E8%81%98%E6%B5%8B%E8%AF%95%E5%8F%AF%E5%88%A0%E9%99%A4/10.jpg",
			"https://wx-dev-image.oss-cn-beijing.aliyuncs.com/%E7%99%BE%E6%97%A5%E6%8B%9B%E8%81%98%E6%B5%8B%E8%AF%95%E5%8F%AF%E5%88%A0%E9%99%A4/11.jpg",
			"https://wx-dev-image.oss-cn-beijing.aliyuncs.com/%E7%99%BE%E6%97%A5%E6%8B%9B%E8%81%98%E6%B5%8B%E8%AF%95%E5%8F%AF%E5%88%A0%E9%99%A4/12.jpg",
			"https://wx-dev-image.oss-cn-beijing.aliyuncs.com/%E7%99%BE%E6%97%A5%E6%8B%9B%E8%81%98%E6%B5%8B%E8%AF%95%E5%8F%AF%E5%88%A0%E9%99%A4/13.jpg",
			"https://wx-dev-image.oss-cn-beijing.aliyuncs.com/%E7%99%BE%E6%97%A5%E6%8B%9B%E8%81%98%E6%B5%8B%E8%AF%95%E5%8F%AF%E5%88%A0%E9%99%A4/14.jpg",
			"https://wx-dev-image.oss-cn-beijing.aliyuncs.com/%E7%99%BE%E6%97%A5%E6%8B%9B%E8%81%98%E6%B5%8B%E8%AF%95%E5%8F%AF%E5%88%A0%E9%99%A4/15.jpg",
			"https://wx-dev-image.oss-cn-beijing.aliyuncs.com/%E7%99%BE%E6%97%A5%E6%8B%9B%E8%81%98%E6%B5%8B%E8%AF%95%E5%8F%AF%E5%88%A0%E9%99%A4/16.jpg",
			"https://wx-dev-image.oss-cn-beijing.aliyuncs.com/%E7%99%BE%E6%97%A5%E6%8B%9B%E8%81%98%E6%B5%8B%E8%AF%95%E5%8F%AF%E5%88%A0%E9%99%A4/1jpeg.jpeg",
			"https://wx-dev-image.oss-cn-beijing.aliyuncs.com/%E7%99%BE%E6%97%A5%E6%8B%9B%E8%81%98%E6%B5%8B%E8%AF%95%E5%8F%AF%E5%88%A0%E9%99%A4/2.jpg",
			"https://wx-dev-image.oss-cn-beijing.aliyuncs.com/%E7%99%BE%E6%97%A5%E6%8B%9B%E8%81%98%E6%B5%8B%E8%AF%95%E5%8F%AF%E5%88%A0%E9%99%A4/3.jpg",
			"https://wx-dev-image.oss-cn-beijing.aliyuncs.com/%E7%99%BE%E6%97%A5%E6%8B%9B%E8%81%98%E6%B5%8B%E8%AF%95%E5%8F%AF%E5%88%A0%E9%99%A4/4.jpg",
			"https://wx-dev-image.oss-cn-beijing.aliyuncs.com/%E7%99%BE%E6%97%A5%E6%8B%9B%E8%81%98%E6%B5%8B%E8%AF%95%E5%8F%AF%E5%88%A0%E9%99%A4/5.jpg",
			"https://wx-dev-image.oss-cn-beijing.aliyuncs.com/%E7%99%BE%E6%97%A5%E6%8B%9B%E8%81%98%E6%B5%8B%E8%AF%95%E5%8F%AF%E5%88%A0%E9%99%A4/6.jpg",
			"https://wx-dev-image.oss-cn-beijing.aliyuncs.com/%E7%99%BE%E6%97%A5%E6%8B%9B%E8%81%98%E6%B5%8B%E8%AF%95%E5%8F%AF%E5%88%A0%E9%99%A4/7.jpg",
			"https://wx-dev-image.oss-cn-beijing.aliyuncs.com/%E7%99%BE%E6%97%A5%E6%8B%9B%E8%81%98%E6%B5%8B%E8%AF%95%E5%8F%AF%E5%88%A0%E9%99%A4/8.jpg",
			"https://wx-dev-image.oss-cn-beijing.aliyuncs.com/%E7%99%BE%E6%97%A5%E6%8B%9B%E8%81%98%E6%B5%8B%E8%AF%95%E5%8F%AF%E5%88%A0%E9%99%A4/9.jpg",
		]
		pic = self.random_value(pic_list, 1)[0]
		return pic

	"""
	学生基本信息，工作名字
	"""

	def __get_job_name(
			self,

	) -> str:
		xList = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许',
				 '何', '吕', '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜', '戚', '谢', '邹', '喻', '柏', '水', '窦', '章']
		m = str(random.randrange(4, 10)) + ''.join(str(random.choice(range(10))) for _ in range(4))
		x = self.random_value(xList, 1)[0]
		name = x + m
		return name

	"""
	随机取一个获取学校信息，包含学校id和学校名称
	"""

	def __get_school_info(
			self
	) -> Dict:
		schoolInfoDict = dict()
		self.__baseMySQLObject.set_mysql_sql("select id,name from es_school")
		schoolInfoSet = self.random_value(self.__baseMySQLObject.execute_only_sql('select', self.__baseConnect), 1)
		schoolInfoDict['schoolId'] = schoolInfoSet[0][0]
		schoolInfoDict['schoolName'] = schoolInfoSet[0][1]
		return schoolInfoDict

	"""
	入学年份
	"""

	def __get_graduation_year(
			self,

	) -> str:
		graduationYearList = ['2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
		return self.random_value(graduationYearList, 1)[0]

	"""
	手机号，随机生成13开头的
	"""

	def __get_job_phone(
			self
	) -> str:
		jobPhone = '13' + str(random.randrange(4, 10)) + ''.join(str(random.choice(range(10))) for _ in range(8))
		return jobPhone

	"""
	邮箱，随机生成
	"""

	def __get_email(
			self,
	) -> str:
		email = str(random.randrange(4, 10)) + ''.join(str(random.choice(range(10))) for _ in range(8)) + '@qq.com'
		return email

	"""
	性别，男女随机取
	"""

	def __get_job_sex(
			self,
	) -> str:
		jobSexList = ['0', '1']
		jobSex = self.random_value(jobSexList, 1)[0]
		return jobSex

	"""
	生日
	"""

	def __get_birth_day(
			self,
	) -> str:
		birthDay = ["1999-01-11", "2000-01-11", "2001-01-11", "2002-01-11", "2003-01-11", "2004-01-11", "2005-01-11"]
		return self.random_value(birthDay, 1)[0]

	"""
	籍贯
	"""

	def __get_native_place(
			self,
	) -> str:
		self.__baseMySQLObject.set_mysql_sql("select id,name from es_school")
		self.__baseMySQLObject.set_mysql_sql("select name from es_region where layer=1")
		nativePlaceSet = self.random_value(self.__baseMySQLObject.execute_only_sql('select', self.__baseConnect), 1)
		return nativePlaceSet[0][0]

	"""
	政治面貌
	"""

	def __get_political_status(
			self,
	) -> int:
		politicalStatusList = [0, 1, 2]
		politicalStatus = self.random_value(politicalStatusList, 1)
		return politicalStatus[0]

	"""
	身高
	"""

	def __get_height(
			self,
	) -> Any:
		heightList = [140, 145, 150, 155, 160, 170, 175, 178, 180, 181, 182, 185, 190, 194, 200]
		height = self.random_value(heightList, 1)
		return height[0]

	"""
	容貌
	"""

	def __get_appearance(
			self,
	) -> int:
		appearanceList = [0, 1, 2]
		appearance = self.random_value(appearanceList, 1)
		return appearance[0]

	"""
	查询求职意向信息，获取求职意向id
	"""

	def __get_intention_id(
			self,
	) -> [bool, str]:
		t = HttpRequest()
		headers = self.__envInfoConfig['headers']
		headers['t'] = self.__token
		t.set_header(headers)
		t.set_url(self.__envInfoConfig[self.__env]['requestDomain'] + self.__envInfoConfig['interfaceRequestPath'][
			'intentionQuery'])
		reponse = t.send_http_request('get')
		reponseJson = t.analysis_reponse_json_data(reponse)
		if 'result' in reponseJson:
			return reponseJson['result']['id']
		else:
			return False

	"""
	获取一项
	"""

	def get_salary_flag(
			self,
	):
		pass

	"""
	获取意向职位id列表
	"""

	def __get_post_ids(
			self,
	) -> List:
		self.__careerMySQLObject.set_mysql_sql("select id from common_post where level=3 and deleted=0")
		idList = self.random_value(self.__careerMySQLObject.execute_only_sql('select', self.__careerConnect), 5)
		postIdsList = list()
		for id in idList:
			self.__careerMySQLObject.set_mysql_sql("select pid from common_post where id =%d and deleted=0" % id[0])
			pid = self.random_value(self.__careerMySQLObject.execute_only_sql('select', self.__careerConnect), 1)
			self.__careerMySQLObject.set_mysql_sql("select pid from common_post where id =%d and deleted=0 " % pid[0])
			ppid = self.random_value(self.__careerMySQLObject.execute_only_sql('select', self.__careerConnect), 1)
			postIdsList.append([ppid[0][0], pid[0][0], id[0]])
		return postIdsList

	"""
	获取意向行业id列表
	"""

	def __get_industry_ids(
			self,
	) -> List:
		self.__careerMySQLObject.set_mysql_sql("select id from common_industry")
		idList = self.random_value(self.__careerMySQLObject.execute_only_sql('select', self.__careerConnect), 5)
		industryIdList = [x[0] for x in idList]
		return industryIdList

	"""
	获取意向职能id列表
	"""

	def __get_functions_ids(
			self,
	) -> List:
		self.__baseMySQLObject.set_mysql_sql("select id from es_function_detail ")
		idList = self.random_value(self.__baseMySQLObject.execute_only_sql('select', self.__baseConnect), 5)
		functionsIds = list()
		for id in idList:
			self.__baseMySQLObject.set_mysql_sql("select pid from es_function_detail where id =%d" % id[0])
			pid = self.random_value(self.__baseMySQLObject.execute_only_sql('select', self.__baseConnect), 1)
			functionsIds.append([pid[0][0], id[0]])
		return functionsIds

	"""
	获取意向工作区域
	"""

	def __get_expected_areas(
			self,
	) -> List:
		self.__baseMySQLObject.set_mysql_sql("select id,lft,rgt,code from es_region where layer = 2 ")
		idList = self.random_value(self.__baseMySQLObject.execute_only_sql('select', self.__baseConnect), 5)
		expectedAreas = list()
		for id in idList:
			self.__baseMySQLObject.set_mysql_sql(
				"select code,name from es_region where layer = 1  and lft<= %d  and  rgt>= %d " % (id[1], id[2]))
			pcode = self.random_value(self.__baseMySQLObject.execute_only_sql('select', self.__baseConnect), 1)
			expectedAreas.append([pcode[0][0], id[3]])
		return expectedAreas

	"""
	是否有薪资区间
	"""

	def __get_salary_flag(
			self,
	) -> bool:
		salaryFlagList = [True, False]
		alaryFlag = self.random_value(salaryFlagList, 1)
		return alaryFlag[0]

	"""
	最少薪酬金额
	"""

	def __get_salary_min(
			self,
	) -> float:
		salaryMinList = [2000.00, 3000.00, 4000.00, 5000, 00, 6000.00]
		salaryMin = self.random_value(salaryMinList, 1)[0]
		return salaryMin

	"""
	最大薪酬金额
	"""

	def __get_salary_max(
			self,
	) -> float:
		salaryMaxList = [6000.00, 7000.00, 8000.00, 9000, 00, 10000.00]
		salaryMax = self.random_value(salaryMaxList, 1)[0]
		return salaryMax

	"""
	获取公司性质
	"""

	def __get_company_natures(
			self,
	) -> List:
		companyNaturesList = [1, 2, 3, 4]
		num = random.randint(0, 3)
		companyNatures = self.random_value(companyNaturesList, num)
		return companyNatures

	"""
	获取公司规模
	"""

	def __get_company_scale(
			self,
	) -> int:
		companyScaleList = [1, 2, 3, 4, 5]
		companyScale = self.random_value(companyScaleList, 1)[0]
		return companyScale

	"""
	获取学校类型
	"""

	def __get_school_type(
			self,
	) -> int:
		schoolTypeList = [1, 2, 3, 4, 5, 6]
		schoolType = self.random_value(schoolTypeList, 1)[0]
		return schoolType

	"""
	获取学历层次
	"""

	def __get_edu_Level(
			self,
	) -> int:
		eduLevelList = [1, 2, 3, 4, 5, 6]
		eduLevel = self.random_value(eduLevelList, 1)[0]
		return eduLevel

	"""
	获取有无学习成绩
	"""

	def __get_grade_flag(
			self,
	) -> bool:
		gradeFlagList = [True, False]
		gradeFlag = self.random_value(gradeFlagList, 1)[0]
		return gradeFlag

	"""
	获取有无学积分排名
	"""

	def __get_credit_rank(
			self,
	) -> int:
		creditRankList = [0, 1, 2]
		creditRank = self.random_value(creditRankList, 1)[0]
		return creditRank

	"""
	获取奖学金
	"""

	def __get_scholarship(
			self,
	):
		scholarshipList = [0, 1, 2, 3, 4, 5]
		scholarship = self.random_value(scholarshipList, 1)[0]
		return scholarship

	"""
	获取学术科研
	"""

	def __get_academic_research_flag(
			self,
	) -> bool:
		academicResearchFlagList = [True, False]
		academicResearchFlag = self.random_value(academicResearchFlagList, 1)[0]
		return academicResearchFlag

	"""
	获取外语水平
	"""

	def __get_foreign_language_flag(
			self,
	) -> bool:
		foreignLanguageFlagList = [True, False]
		foreignLanguageFlag = self.random_value(foreignLanguageFlagList, 1)[0]
		return foreignLanguageFlag

	"""
	获取职业技能
	"""

	def __get_professional_skills(
			self,
	) -> str:
		professionalSkills = "职业技能" + str(random.randint(0, 1000))
		return professionalSkills

	"""
	获取社团职务
	"""

	def __get_association_position(
			self,
	) -> int:
		associationPositionList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
		associationPosition = self.random_value(associationPositionList, 1)[0]
		return associationPosition

	"""
	思维能力
	"""

	def __get_thinking_ability(
			self,
	) -> int:
		thinkingAbilityList = [0, 1, 2]
		thinkingAbility = self.random_value(thinkingAbilityList, 1)[0]
		return thinkingAbility

	"""
	人格魅力
	"""

	def __get_charisma(
			self,
	) -> int:
		charismaList = [0, 1, 2]
		charisma = self.random_value(charismaList, 1)[0]
		return charisma

	"""
	获取一级学科
	"""

	def __get_subject_id(
			self,
			eduLevel: int

	) -> List:
		yList = [1, 2]
		bList = [3, 4]
		zList = [5, 6]
		if eduLevel in yList:
			self.__baseMySQLObject.set_mysql_sql("select id from es_subject where type= 1 and layer=2 and deleted=0")
		elif eduLevel in bList:
			self.__baseMySQLObject.set_mysql_sql("select id from es_subject where type= 2 and layer=2 and deleted=0")
		elif eduLevel in zList:
			self.__baseMySQLObject.set_mysql_sql("select id from es_subject where type= 3 and layer=2 and deleted=0")

		id = self.random_value(self.__baseMySQLObject.execute_only_sql('select', self.__baseConnect), 1)[0][0]

		self.__baseMySQLObject.set_mysql_sql("select pid from es_subject where  id=%s and deleted=0" % id)
		pid = self.random_value(self.__baseMySQLObject.execute_only_sql('select', self.__baseConnect), 1)[0][0]
		subjectId = [[pid, id]]
		return subjectId

	"""
	获取专业
	"""

	def __get_profession_subject_id(
			self,
			eduLevel: int

	) -> List:
		yList = [1, 2]
		bList = [3, 4]
		zList = [5, 6]
		if eduLevel in yList:
			self.__baseMySQLObject.set_mysql_sql("select id from es_subject where type= 1 and layer=3 and deleted = 0")
		elif eduLevel in bList:
			self.__baseMySQLObject.set_mysql_sql("select id from es_subject where type= 2 and layer=3 and deleted = 0")
		elif eduLevel in zList:
			self.__baseMySQLObject.set_mysql_sql("select id from es_subject where type= 3 and layer=3 and deleted = 0")

		id = self.random_value(self.__baseMySQLObject.execute_only_sql('select', self.__baseConnect), 1)[0][0]
		self.__baseMySQLObject.set_mysql_sql("select pid from es_subject where  id=%s and deleted=0" % id)
		pid = self.random_value(self.__baseMySQLObject.execute_only_sql('select', self.__baseConnect), 1)[0][0]
		self.__baseMySQLObject.set_mysql_sql("select pid from es_subject where  id=%s and deleted=0" % pid)
		ppid = self.random_value(self.__baseMySQLObject.execute_only_sql('select', self.__baseConnect), 1)[0][0]
		professionSubjectId = [[ppid, pid, id, ]]
		return professionSubjectId

	"""
	获取擅长的学科
	"""

	def __get_good_atSubject_ids(
			self,
			eduLevel: int
	) -> List:
		yList = [1, 2]
		bList = [3, 4]
		zList = [5, 6]
		if eduLevel in yList:
			self.__baseMySQLObject.set_mysql_sql("select id from es_subject where type= 1 and layer=1 and deleted=0")
		elif eduLevel in bList:
			self.__baseMySQLObject.set_mysql_sql("select id from es_subject where type= 2 and layer=1 and deleted=0")
		elif eduLevel in zList:
			self.__baseMySQLObject.set_mysql_sql("select id from es_subject where type= 3 and layer=1 and deleted=0")
		sqlResult = self.__baseMySQLObject.execute_only_sql('select', self.__baseConnect)
		subjectCount = len(sqlResult)
		num = random.randint(1, subjectCount)
		goodAtSubjectIdsList = self.random_value(sqlResult, num)
		goodAtSubjectIds = [[x[0]] for x in goodAtSubjectIdsList]
		return goodAtSubjectIds

	"""
	获取学术论文
	"""

	def __get_academic_level_ids(
			self,
	) -> List:
		academicLevelIds = list()

		self.__careerMySQLObject.set_mysql_sql(
			"select id from b_recruitment_extension_level WHERE type =1 and (source = 0 or source=1) and `code` = 'X4-1' and pid=0")
		for x in self.__careerMySQLObject.execute_only_sql('select', self.__careerConnect):
			self.__careerMySQLObject.set_mysql_sql(
				"select id from b_recruitment_extension_level WHERE type =1 and (source = 0 or source=1) and `code` = 'X4-1' and pid = %s " %
				x[0])
			academicLevelId = \
				self.random_value(self.__careerMySQLObject.execute_only_sql('select', self.__careerConnect), 1)[0][0]
			academicLevelIds.append([x[0], academicLevelId])
		return academicLevelIds

	"""
	获取科研成果
	"""

	def __get_research_level_ids(
			self,
	) -> List:
		researchLevelIds = list()

		self.__careerMySQLObject.set_mysql_sql(
			"select id from b_recruitment_extension_level WHERE type =2 and (source = 0 or source=1) and `code` = 'X4-2' and pid=0")
		for x in self.__careerMySQLObject.execute_only_sql('select', self.__careerConnect):
			self.__careerMySQLObject.set_mysql_sql(
				"select id from b_recruitment_extension_level WHERE type =2 and (source = 0 or source=1) and `code` = 'X4-2' and pid = %s " %
				x[0])
			researchLevelId = \
				self.random_value(self.__careerMySQLObject.execute_only_sql('select', self.__careerConnect), 1)[0][0]
			researchLevelIds.append([x[0], researchLevelId])
		return researchLevelIds

	"""
	获取性格特征
	"""

	def __get_character_trraits_level_ids(
			self,
	) -> List:
		characterTraitsLevelIds = list()
		self.__careerMySQLObject.set_mysql_sql(
			"select id from b_recruitment_extension_level WHERE type =4 and (source = 0 or source=1)  and pid=0")
		for x in self.__careerMySQLObject.execute_only_sql('select', self.__careerConnect):
			self.__careerMySQLObject.set_mysql_sql(
				"select id from b_recruitment_extension_level WHERE type =4 and (source = 0 or source=1)  and pid = %s " %
				x[0])
			characterTraitsLevelId = \
				self.random_value(self.__careerMySQLObject.execute_only_sql('select', self.__careerConnect), 1)[0][0]
			characterTraitsLevelIds.append([x[0], characterTraitsLevelId])
		return characterTraitsLevelIds

	"""
	获取心理能量
	"""

	def __get_psychological_power_level_ids(
			self,
	) -> List:
		psychologicalPowerLevelIds = list()
		self.__careerMySQLObject.set_mysql_sql(
			"select id from b_recruitment_extension_level WHERE type =5 and (source = 0 or source=1)  and pid=0")
		for x in self.__careerMySQLObject.execute_only_sql('select', self.__careerConnect):
			self.__careerMySQLObject.set_mysql_sql(
				"select id from b_recruitment_extension_level WHERE type =5 and (source = 0 or source=1)  and pid = %s " %
				x[0])
			psychologicalPowerLevelId = \
				self.random_value(self.__careerMySQLObject.execute_only_sql('select', self.__careerConnect), 1)[0][0]
			psychologicalPowerLevelIds.append([x[0], psychologicalPowerLevelId])
		return psychologicalPowerLevelIds

	"""
	获取语言表达能力
	"""

	def __get_expression_level_ids(
			self,
	) -> List:
		expressionLevelIds = list()
		self.__careerMySQLObject.set_mysql_db('es_career')
		self.__careerMySQLObject.set_mysql_sql(
			"select id from b_recruitment_extension_level WHERE type =6 and (source = 0 or source=1)  and pid=0")
		for x in self.__careerMySQLObject.execute_only_sql('select', self.__careerConnect):
			self.__careerMySQLObject.set_mysql_sql(
				"select id from b_recruitment_extension_level WHERE type =6 and (source = 0 or source=1)  and pid = %s " %
				x[0])
			expressionLevelId = \
				self.random_value(self.__careerMySQLObject.execute_only_sql('select', self.__careerConnect), 1)[0][0]
			expressionLevelIds.append([x[0], expressionLevelId])
		return expressionLevelIds

	"""
	获取负责任务执行和领导能力
	"""

	def __get_execution_leadership_level_ids(
			self,
	) -> List:
		executionLeadershipLevelIds = list()
		self.__careerMySQLObject.set_mysql_sql(
			"select id from b_recruitment_extension_level WHERE type =7 and (source = 0 or source=1)  and pid=0")
		for x in self.__careerMySQLObject.execute_only_sql('select', self.__careerConnect):
			self.__careerMySQLObject.set_mysql_sql(
				"select id,name from b_recruitment_extension_level WHERE type =7 and (source = 0 or source=1)  and pid = %s " %
				x[0])
			executionLeadershipLevelInfo = self.__careerMySQLObject.execute_only_sql('select', self.__careerConnect)
			for y in executionLeadershipLevelInfo:
				if y[1] == "无":
					executionLeadershipLevelIds.append([x[0], executionLeadershipLevelInfo[0][0]])
					continue
				self.__careerMySQLObject.set_mysql_sql(
					"select id from b_recruitment_extension_level WHERE type =7 and (source = 0 or source=1)  and pid = %s " %
					y[0])
				executionLeadershipLevelId = self.random_value(
					self.__careerMySQLObject.execute_only_sql('select', self.__careerConnect), 1)
				executionLeadershipLevelIds.append(
					[x[0], executionLeadershipLevelInfo[0][0], executionLeadershipLevelId[0][0]])
		return executionLeadershipLevelIds

	"""
	获取英语水平
	"""

	def __get_english_level_ids(
			self,
			type: int
	) -> List:
		englishLevelIds = list()
		self.__careerMySQLObject.set_mysql_sql(
			"select id from b_recruitment_extension_level WHERE type =%d and (source = 0 or source=1)  and pid=0" % type)
		for x in self.__careerMySQLObject.execute_only_sql('select', self.__careerConnect):
			self.__careerMySQLObject.set_mysql_sql(
				"select id from b_recruitment_extension_level WHERE type =%d and (source = 0 or source=1)  and pid=%s" % (
					type, x[0]))
			englishLevelId = self.__careerMySQLObject.execute_only_sql('select', self.__careerConnect)
			for y in englishLevelId:
				self.__careerMySQLObject.set_mysql_sql(
					"select id from b_recruitment_extension_level WHERE type =%d and (source = 0 or source=1)  and pid=%s" % (
						type, y[0]))
				englishLevelIdStatus = self.random_value(
					self.__careerMySQLObject.execute_only_sql('select', self.__careerConnect), 1)
				englishLevelIds.append([x[0], y[0], englishLevelIdStatus[0][0]])
		return englishLevelIds

	def __get_ability_id(
			self,
	) -> [bool, str]:
		t = HttpRequest()
		headers = self.__envInfoConfig['headers']
		headers['t'] = self.__token
		t.set_header(headers)
		t.set_url(self.__envInfoConfig[self.__env]['requestDomain'] + self.__envInfoConfig['interfaceRequestPath'][
			'abilityQuery'])
		reponsee = t.send_http_request('get')
		reponseJson = t.analysis_reponse_json_data(reponsee)
		if 'result' in reponseJson:
			return reponseJson['result']['id']
		else:
			return False

	"""
	学生基本信息，第一阶段
	"""

	def setupOne(
			self,
	):
		studentBaseInfo = dict()
		studentBaseInfo['studentPic'] = self.__get_student_pic()
		studentBaseInfo['jobName'] = self.__get_job_name()
		studentBaseInfo['schoolId'] = self.__get_school_info()['schoolId']
		studentBaseInfo['schoolName'] = self.__get_school_info()['schoolName']
		studentBaseInfo['graduationYear'] = self.__get_graduation_year()
		studentBaseInfo['jobPhone'] = self.__get_job_phone()
		studentBaseInfo['email'] = self.__get_email()
		studentBaseInfo['jobSex'] = self.__get_job_sex()
		studentBaseInfo['birthDay'] = self.__get_birth_day()
		studentBaseInfo['nativePlaceSet'] = self.__get_native_place()
		studentBaseInfo['politicalStatus'] = self.__get_political_status()
		studentBaseInfo['height'] = self.__get_height()
		studentBaseInfo['appearance'] = self.__get_appearance()
		t = HttpRequest()
		headers = self.__envInfoConfig['headers']
		headers['t'] = self.__token
		t.set_header(headers)
		t.set_data(json.dumps(studentBaseInfo))
		t.set_url(self.__envInfoConfig[self.__env]['requestDomain'] + self.__envInfoConfig['interfaceRequestPath'][
			'addOrEditStudentBaseInfo'])
		reponsee = t.send_http_request('post')
		reponseJson = t.analysis_reponse_json_data(reponsee)
		returnCode = reponseJson['status']
		if returnCode == 200:
			print("用户" + self.__studentInfo['phone'] + '  第一阶段学生基本信息录入成功！')
		else:
			print("用户" + self.__studentInfo['phone'] + '  第一阶段学生基本信息录入失败！')

	"""
	学生求职意向信息，第二阶段
	"""

	def setupTwo(
			self,
	):
		studentIntentionInfo = dict()
		intention_id = self.__get_intention_id()
		if intention_id:
			studentIntentionInfo['id'] = intention_id
		else:
			studentIntentionInfo['id'] = 0
		studentIntentionInfo['postIds'] = self.__get_post_ids()
		studentIntentionInfo['industryIds'] = self.__get_industry_ids()
		studentIntentionInfo['functions'] = self.__get_functions_ids()
		studentIntentionInfo['expectedAreas'] = self.__get_expected_areas()
		studentIntentionInfo['futureAreas'] = self.__get_expected_areas()
		studentIntentionInfo['salaryFlag'] = self.__get_salary_flag()
		studentIntentionInfo['salaryMin'] = self.__get_salary_min()
		studentIntentionInfo['salaryMax'] = self.__get_salary_max()
		studentIntentionInfo['companyNatures'] = self.__get_company_natures()
		studentIntentionInfo['companyScale'] = self.__get_company_scale()

		t = HttpRequest()
		headers = self.__envInfoConfig['headers']
		headers['t'] = self.__token
		t.set_header(headers)
		t.set_data(json.dumps(studentIntentionInfo))
		t.set_url(self.__envInfoConfig[self.__env]['requestDomain'] + self.__envInfoConfig['interfaceRequestPath'][
			'addOrEditStudentIntentionInfo'])
		reponsee = t.send_http_request('post')
		reponseJson = t.analysis_reponse_json_data(reponsee)
		returnCode = reponseJson['status']
		if returnCode == 200:
			print("用户" + self.__studentInfo['phone'] + '  第二阶段学生求职意向信息录入成功！')
		else:
			print("用户" + self.__studentInfo['phone'] + '  第二阶段学生求职意向信息录入失败！')

	"""
	学生求职能力与资历信息，第三阶段
	"""

	def setupThree(
			self,
	):
		studentAbilityInfo = dict()
		ability_id = self.__get_ability_id()
		if ability_id:
			studentAbilityInfo['id'] = ability_id
		else:
			studentAbilityInfo['id'] = 0
		studentAbilityInfo['schoolType'] = self.__get_school_type()
		studentAbilityInfo['eduLevel'] = self.__get_edu_Level()
		studentAbilityInfo['gradeFlag'] = self.__get_grade_flag()
		studentAbilityInfo['creditRank'] = self.__get_credit_rank()
		studentAbilityInfo['scholarship'] = self.__get_scholarship()
		studentAbilityInfo['academicResearchFlag'] = self.__get_academic_research_flag()
		studentAbilityInfo['foreignLanguageFlag'] = self.__get_foreign_language_flag()
		studentAbilityInfo['professionalSkills'] = self.__get_professional_skills()
		studentAbilityInfo['associationPosition'] = self.__get_association_position()
		studentAbilityInfo['thinkingAbility'] = self.__get_thinking_ability()
		studentAbilityInfo['charisma'] = self.__get_charisma()
		studentAbilityInfo['subjectId'] = self.__get_subject_id(studentAbilityInfo['eduLevel'])
		studentAbilityInfo['professionSubjectId'] = self.__get_profession_subject_id(studentAbilityInfo['eduLevel'])
		studentAbilityInfo['goodAtSubjectIds'] = self.__get_good_atSubject_ids(studentAbilityInfo['eduLevel'])
		studentAbilityInfo['likeSubjectIds'] = self.__get_good_atSubject_ids(studentAbilityInfo['eduLevel'])
		studentAbilityInfo['academicLevelIds'] = self.__get_academic_level_ids()
		studentAbilityInfo['researchLevelIds'] = self.__get_research_level_ids()
		studentAbilityInfo['characterTraitsLevelIds'] = self.__get_character_trraits_level_ids()
		studentAbilityInfo['psychologicalPowerLevelIds'] = self.__get_psychological_power_level_ids()
		studentAbilityInfo['expressionLevelIds'] = self.__get_expression_level_ids()
		studentAbilityInfo['executionLeadershipLevelIds'] = self.__get_execution_leadership_level_ids()
		studentAbilityInfo['englishLevelIds'] = self.__get_english_level_ids(8)
		studentAbilityInfo['frenchLevelIds'] = self.__get_english_level_ids(9)
		studentAbilityInfo['germanLevelIds'] = self.__get_english_level_ids(10)
		studentAbilityInfo['japaneseLevelIds'] = self.__get_english_level_ids(11)
		studentAbilityInfo['spanishLevelIds'] = self.__get_english_level_ids(12)
		studentAbilityInfo['russianLevelIds'] = self.__get_english_level_ids(13)
		studentAbilityInfo['koreanLevelIds'] = self.__get_english_level_ids(14)
		studentAbilityInfo['otherLanguageDtoList'] = [
			{
				"otherLanguage": "泰语",
				"readWriteAbility": "优秀",
				"listenSpeakAbility": "良好",
				"testName": "泰语八级",
				"testResult": "700"
			}
		]
		t = HttpRequest()
		headers = self.__envInfoConfig['headers']
		headers['t'] = self.__token
		t.set_header(headers)
		t.set_data(json.dumps(studentAbilityInfo))
		t.set_url(self.__envInfoConfig[self.__env]['requestDomain'] + self.__envInfoConfig['interfaceRequestPath'][
			'addOrEditStudentabilityInfo'])
		reponsee = t.send_http_request('post')
		reponseJson = t.analysis_reponse_json_data(reponsee)
		returnCode = reponseJson['status']
		if returnCode == 200:
			print("用户" + self.__studentInfo['phone'] + '  第三阶段求职能力与资历信息录入成功！')
		else:
			print("用户" + self.__studentInfo['phone'] + '  第三阶段求职能力与资历信息录入失败！')
		self.__careerConnect.close()
		self.__baseConnect.close()


"""
简历录入配置信息
"""


def student_resume(
		student_info: Dict,
		envInfoConfigPath: str,
		careerMySQLObject: OperationMySQL,
		baseMySQLObject: OperationMySQL,
		env
):
	resumeObject = Resume(envInfoConfigPath, careerMySQLObject, baseMySQLObject)
	resumeObject.set_env(env)
	resumeObject.get_token(student_info)
	resumeObject.setupOne()
	resumeObject.setupTwo()
	resumeObject.setupThree()


"""
存队列
"""


def put_queue(
		student_info_queue: Queue
) -> None:
	dataInfoDict = Resume.load_yaml_data("data/userInfo.yaml")
	for student_info in dataInfoDict:
		student_info_queue.put_nowait(student_info)


"""
取队列
"""


def get_queue(
		student_info_queue: Queue,
		envInfoConfigPath: str,
		careerMySQLObject: OperationMySQL,
		baseMySQLObject: OperationMySQL,
		env: str
) -> None:
	while not student_info_queue.empty():
		student_info = student_info_queue.get_nowait()
		student_resume(student_info, envInfoConfigPath, careerMySQLObject, baseMySQLObject, env)


"""
异步队列运行
"""


def run(
		taskslimit: int = None,
		env: str = ''
) -> None:
	print("创建异步队列中......")
	student_info_queue = Queue()
	put_queue(student_info_queue)
	print("创建异步队列完成")
	envInfoConfigPath = "config/config.yaml"
	config = Resume.load_yaml_data(envInfoConfigPath)
	dbHost = config[env]['mysql']['mysqlHost']
	dbUsername = config[env]['mysql']['mysqlUsername']
	dbPassword = config[env]['mysql']['mysqlPassword']
	print("创建career数据库对象连接中......")
	careerMySQLObject = OperationMySQL.OperationMySQL(dbHost, dbUsername, dbPassword)
	careerMySQLObject.set_mysql_db('es_career')
	print("创建career数据库对象完成")
	print("创建base数据库对象连接中......")
	baseMySQLObject = OperationMySQL.OperationMySQL(dbHost, dbUsername, dbPassword)
	baseMySQLObject.set_mysql_db("es_base")
	print("创建base数据库对象完成")
	taskList = []
	print("创建异步任务中......")
	for x in range(taskslimit):
		# 循环几次，相当于开了几个并发任务
		task = gevent.spawn(get_queue, student_info_queue, envInfoConfigPath, careerMySQLObject, baseMySQLObject,
							env)
		taskList.append(task)
	print("创建异步任务完成")
	gevent.joinall(taskList)  # 使用协程来执行
