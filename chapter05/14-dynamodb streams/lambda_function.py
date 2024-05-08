from __future__ import print_function
def lambda_handler(event, context):
    # イベントの各レコードを処理
    for record in event['Records']:
        # イベントの一意の識別子を表示
        print(record['eventID'])
        # イベントの種類（INSERT、MODIFY、または REMOVE）を表示
        print(record['eventName'])
    # 処理したレコードの総数を表示
    print('処理されたレコードの数：%s' % str(len(event['Records'])))