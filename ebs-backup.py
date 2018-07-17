#!/usr/bin/env python3

import boto3
import time

def lambda_handler(event, context):
    ec2 = boto3.resource('ec2')
    volumes = ec2.volumes.filter(Filters=[{'Name': 'tag:DailyBackup', 'Values': ['1']}])

    for volume in volumes:
        for tag in volume.tags:
            if 'Name' == tag['Key']:
                name = tag['Value']

        if name is None:
            continue

        now = time.strftime('%Y%m%d-%H%M%S')

        desc = 'Snapshoted from %s (%s, %s)' % (name, volume.id, now)
        snapshot = volume.create_snapshot(Description=desc)

        snap_name = '%s-snapshot-%s' % (name, now)

        snapshot.create_tags(Tags=[{
            'Key': 'Name',
            'Value': snap_name
        }])
