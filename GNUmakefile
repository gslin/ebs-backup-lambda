#
-include GNUmakefile.local

#
NAME?=		ebs-backup
ROLE?=		Role-Lambda-EBS-Backup

#
ifdef PROFILE
export AWS_DEFAULT_PROFILE=${PROFILE}
else
export AWS_DEFAULT_PROFILE=default
endif

ifdef REGION
export AWS_DEFAULT_REGION=${REGION}
else
export AWS_DEFAULT_REGION=us-east-1
endif

#
.PHONY:		setup-lambda setup-role

setup-lambda: ${NAME}.zip
	aws lambda create-function --function ${NAME} --runtime python3.6 --role "arn:aws:iam::${ACCOUNT_ID}:role/${ROLE}" --handler ${NAME}.lambda_handler --function-name ${NAME} --zip-file fileb://${NAME}.zip --timeout 60 --memory-size 128 || true

setup-role:
	aws iam create-role --role-name "${ROLE}" --assume-role-policy-document '{"Version":"2012-10-17","Statement":{"Effect":"Allow","Principal":{"Service":"lambda.amazonaws.com"},"Action":"sts:AssumeRole"}}' || true
	aws iam attach-role-policy --role-name "${ROLE}" --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole || true
