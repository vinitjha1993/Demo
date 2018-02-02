import sys
import boto3

import boto3
ec2 = boto3.resource('ec2')
ids = ['i-0aa1baef974ac30a9']
ec2.instances.filter(InstanceIds=ids).stop()
