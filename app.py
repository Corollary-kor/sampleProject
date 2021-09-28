#!/usr/bin/env python3
from aws_cdk import core as cdk
from my_pipeline.my_pipeline_stack import MyPipelineStack

app = cdk.App()
MyPipelineStack(app, "MyPipelineStack", 
    env=cdk.Environment(account="782621889128", region="us-west-2")
)

app.synth()