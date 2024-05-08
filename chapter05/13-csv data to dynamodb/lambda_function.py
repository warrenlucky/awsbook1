import json
import boto3
import csv
from io import StringIO

print('Loading function')
# AWSサービスの初期化
s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('データをインポートするDynamoDBテーブル名に置き換える')
def lambda_handler(event, context):
    # イベントからオブジェクトを取得し、その内容タイプを表示する
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    response = s3.get_object(Bucket=bucket, Key=key)
    data = response['Body'].read().decode('utf-8')
    # CSVデータの解析
    csv_data = csv.reader(StringIO(data))
    for row in csv_data:
        if len(row) == 3:  # 各行が3つの列のデータを持っているかを確認
            try:
                # データをDynamoDBに書き込む
                table.put_item(
                    Item={
                        'id': row[0],
                        'name': row[1],
                        'age': row[2]
                    }
                )
            except Exception as e:
                print('Error:', str(e))  # エラーメッセージを出力する
        else:
            print('Invalid data row:', row)  # 無効なデータ行を出力する