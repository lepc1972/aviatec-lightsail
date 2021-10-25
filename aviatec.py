from flask import Flask, render_template, request
import boto3
import getpass

app = Flask(__name__)


@app.route('/')
def get_recommendations1():
    
    aws_access_key_id = ''
    aws_secret_access_key = ''
    region = 'us-east-1'

    personalizeRt = boto3.client('personalize-runtime', region_name='us-east-1')

    response = personalizeRt.get_recommendations(
    campaignArn='arn:aws:personalize:us-east-1:155853001258:campaign/my-aviatec-campaign-hotels-1',
    userId='89',
    numResults=10
)
    return(response)

    return("Recommended items")
    for item in response['itemList']:
        return(item['itemId'])

@app.route('/1')
def get_recommendations2():
    aws_access_key_id = ''
    aws_secret_access_key = ''
    region = 'us-east-1'

    personalizeRt = boto3.client('personalize-runtime', region_name='us-east-1')

    response = personalizeRt.get_recommendations(
    campaignArn='arn:aws:personalize:us-east-1:155853001258:campaign/my-aviatec-campaign-hotels-2',
    itemId='72',
    numResults=10
)
    return(response)

    return("Recommended items")
    for item in response['itemList']:
        return(item['itemId'])


@app.route('/2')
def get_recommendations3():
    aws_access_key_id = ''
    aws_secret_access_key = ''
    region = 'us-east-1'

    personalizeRt = boto3.client('personalize-runtime', region_name='us-east-1')

    response = personalizeRt.get_recommendations(
    campaignArn='arn:aws:personalize:us-east-1:155853001258:campaign/my-aviatec-campaign-hotels3',
    itemId='15',
    numResults=15
)
    return(response)

    return("Recommended items")
    for item in response['itemList']:
        return(item['itemId'])

@app.route('/3')
def get_recommendations4():
    aws_access_key_id = ''
    aws_secret_access_key = ''
    region = 'us-east-1'

    personalizeRt = boto3.client('personalize-runtime', region_name='us-east-1')

    response = personalizeRt.get_recommendations(
    campaignArn='arn:aws:personalize:us-east-1:155853001258:campaign/my-aviatec-campaign-hotels-4',
    userId='72',
    numResults=10
)
    return(response)

    return("Recommended items")
    for item in response['itemList']:
        return(item['itemId'])


if __name__ == '__main__':
    app.run('0.0.0.0','8080', debug=True)
