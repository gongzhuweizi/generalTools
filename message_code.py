#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：generalTools
@File ：message_code.py
@Author ：zhangyi
@Date ：2022/7/4 7:26 PM
'''
from aliyunsdkcore import client
from aliyunsdkafs.request.v20180112 import AnalyzeNvcRequest
from aliyunsdkcore.profile import region_provider
region_provider.modify_point('afs', 'cn-hangzhou', 'afs.aliyuncs.com')
# YOUR ACCESS_KEY、YOUR ACCESS_SECRET请替换成您的阿里云accesskey id和secret
clt = client.AcsClient('LTAI5tL546ogUkBFLdrupGt3', 'yPcPEaH1v8Nh8o4rvscF4wnWG6Qvez', 'cn-hangzhou')
request = AnalyzeNvcRequest.AnalyzeNvcRequest()
# 前端获取
request.set_Data("%7B%22a%22%3A%22FFFF0N0000000000ACFC%22%2C%22c%22%3A%221656934726149%3A0.9209547946931977%22%2C%22d%22%3A%22nvc_register_h5%22%2C%22h%22%3A%7B%22key1%22%3A%22code0%22%2C%22nvcCode%22%3A400%2C%22umidToken%22%3A%22T2gAD_YZ75umdWwbqLaZmOrpwm-G4G5TrA3Rxr2XsueCu05rk5RDrOQbY2LQpW83fEI%3D%22%7D%2C%22j%22%3A%7B%22test%22%3A1%7D%2C%22b%22%3A%22140%23wSODXOobzzFc4zo2254uwpSrc%2FfJVvhYf9lvEECByyBfcW6NBjzznbLXS%2Fy5HWvvMOKtNwpU%2FH7HoIJmRCMbKFyOlp1zzqcpVKHPSQzxKoPmO6Etzzrb22U3l61oSfz5FS%2FqUb2x2oa3V3gqzLSx4mr%2F7SvZrI7Zbh1coiHm9XLG3fgGPW8m6xplmihOoLul%2FsUD3X%2BGZ5TUOUMWliHMSgdhDYn65TLr4%2FuIvJ4l7bZ04v6ub9eWlMPKRL4OzVHCBSvKKAFDvUVvPW2XDAkIcWu6wJwfsBopRW0VrHj%2FMI9jEUjX5AMU739xBKvbCzi6Iu%2FqV%2FSfs6BffN8rzGgz9aORYQdYh7I6cbasrQYCRB44sVagvEHHAoXJYvGahq6Ltq3Iaqve4BeAGKy9VmZBAh%2FnjgkCXycplupeieMKc6KhJDMNLP9wOibZ8bVix3AnhoWzVXryaFqvqTewI1Rx%2FW40m%2FYQcKpPegCdCgUZyKG7fsGseWU44mprut73OcUsUPQbufE4EAGZ2VYjfcw8JgOOwYxThE6Jw0LZ0L9OO6%2B5JvFRAoj6w%2FaU9Iax23xelYv4WB6BD1EtmmUFNbLN7x6gV8DBevs2CrTW%2Fn0Sv0U9x5Ki7UDpv2nqbi8uKJS6GvT9LNZ9RYM%2BCYn%2BXYe6jhcW3X30olZ7yl0BhOfUgTnKMsg93Ei9AGr9%2B81zNAOQo0eOPnlMJislmtvDnMi%2Fwr9B2dNZ2B%2BN8u%2Fz%2Bz%2FxdnHt89n24PyRxicdnHOqjaxV1TBMCKEmUt8JLCKDYfQQSLee0DHkQu9XrO5blgC0mpeDiu%2FE79FkV%2BIaCjWcSnAzxaKz74%2BKP%2F%2BTPakBS0QY7g58RL%2B%2BpFEnWB5AIhztnBAWXqU05v81bHVrO7vRqNrsIT40vXdTG6avU0qW4uesmxDq7LFSFWGEt8t1XjCZbqEqec5YD3%2FAjYRlYhexRLfpkec3Sk2numq5OZSmAu5u48zYKMdZk832DPFzf2OEGhcuSqDUEISpkXUHFCef5wxx0IQNfzgYKyy5afFAjWAz3HRL7UIvfiqVvoXMqM1hIdqFbfhDWA67Gs5K%2F54lmrZmG14WhUJ2RJLCCkIhasKuqyD9QkFCt%2BmN6MiSeZXIvX4D3WJxU5BGXCjKp5ev8gSxbfXuTI7gPDQtIQyYMMr7M11sg63JMFgeTGdPaB5wRF%3D%3D%22%2C%22e%22%3A%22TAWVcEzG9v5FmjPihItGJiGeUsSELmB0cSUs00hHLGHPbs73V5pIs2uCDz9klg-QaI-4VKxA2I59p2hiNXwz9qlR4NYbu64QmJ2-YZUqDfbpWS8emKQ2rGNjAlZMl8YrJLRNyDimjECWquFccEOvHFrchas5B7uEGM54lg5oFsLuTW8srUlVMzm64vI7-8lEqqgvgQ7m3hg8VVeQtP6jnw%22%2C%22i%22%3Atrue%7D")
#必填参数：从前端获取getNVCVal函数的值
request.set_ScoreJsonStr('{"200":"PASS","400":"NC","600":"SC","700":"LC","800":"BLOCK"}');

result = clt.do_action(request)
print(result)
