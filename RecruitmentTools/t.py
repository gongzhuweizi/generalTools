#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：generalTools
@File ：t.py
@Author ：zhangyi
@Date ：2022/6/1 1:35 PM
'''
import asyncio

async def count(n):
# async相当于go的goroutine
    print("One")
    await asyncio.sleep(n)
    print("Two")
    return n

async def main():
    print("Starting...")
    a =  await count(1)

    print(f"{a} &  End.")

asyncio.run(main())
