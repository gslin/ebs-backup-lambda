# ebs-backup-lambda

This package will create snapshots to backup EBS automatically.  Only EBS volumes with `DailyBackup` tag will be backuped.

## Requirements

You will need to install AWS CLI and GNU Make to setup and update this package.

## Installation

You need to setup `GNUmakefile.local` first, you can reference `GNUmakefile.local.sample`:

    ACCOUNT_ID=x
    PROFILE=x
    REGION=x

We have put AWS-related setuping commands into GNUmakefile, so you can use the following simple commands to initialize:

    make setup-role
    make setup-lambda
    make setup-cron

## Update

We have put AWS-related updating commands into GNUmakefile, so you can use the following simple commands to update:

    make deploy

## Clean

Usually you don't need to cleanup, but if you want/need to do it, use the following commands:

    make clean

## Others

If you are in us-east-1, us-west-2, or eu-west-1, then you won't need this package.  You can just use "Lifecycle Management for Amazon EBS Snapshots" function:

* https://aws.amazon.com/blogs/aws/new-lifecycle-management-for-amazon-ebs-snapshots/

This will reduce lambda service's cost (although this one is quite cheap) and management cost (which will be much higher).
