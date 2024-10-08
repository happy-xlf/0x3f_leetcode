#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :demo.py
# @Time      :2024/09/15 18:06:39
# @Author    :Lifeng
# @Description :
from agentscope.agents import DialogAgent, UserAgent
import agentscope
from agentscope.pipelines.functional import sequentialpipeline

def create():
    # Load model configs
    agentscope.init(
        model_configs="./model_config.json",
        project="self_demo",
        save_api_invoke=True
        )

    # Create a dialog agent and a user agent
    dialog_agent = DialogAgent(name="dialog_agent",
                               sys_prompt="You are a helpful assistant.",
                               model_config_name="my_dashcope_chat_config")
    user_agent = UserAgent(name="user_agent")

    # Create a pipeline
    x = None
    while x is None or x.content != "exit":
        x = sequentialpipeline([dialog_agent, user_agent], x)

if __name__ == "__main__":
    create()