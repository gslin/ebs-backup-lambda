# ebs-backup-lambda

This package will create snapshots to backup EBS automatically.  Only EBS volumes with `DailyBackup` tag will be backuped.

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
