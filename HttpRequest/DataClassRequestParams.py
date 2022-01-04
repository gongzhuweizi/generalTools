#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：generalTools
@File ：DataClassRequestParams.py
@Author ：zhangyi
@Date ：2022/1/4 10:17 PM
'''
from dataclasses import dataclass
from typing import Union, Any


@dataclass
class DataClassRequestParams():
	params: Union[Any, None]
	data: Union[Any, None]
	headers: Union[Any, None]
	cookies: Union[Any, None]
	files: Union[Any, None]
	auth: Union[Any, None]
	timeout: Union[Any, None]
	allow_redirects: bool
	proxies: Union[Any, None]
	hooks: Union[Any, None]
	stream: Union[Any, None]
	verify: Union[Any, None]
	cert: Union[Any, None]
	json: Union[Any, None]
