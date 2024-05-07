// Lambda 関数ハンドラーのエクスポート
export const handler = function(event, context, callback) {
    // 受信したイベントオブジェクトを出力し、JSON.stringify を使用してフォーマットされた出力を行う
    console.log('Received event:', JSON.stringify(event, null, 2));
    // レスポンスオブジェクトを作成し、初期のステータスコードを 200、Content-Type を任意のタイプに設定する
    var res ={
        "statusCode": 200,
        "headers": {
            "Content-Type": "*/*"
        }
    };
    // デフォルトの挨拶語は 'World'
    var greeter = 'World';
    // イベントオブジェクトに greeter プロパティが含まれ、かつその値が空でないかどうかをチェックする
    if (event.greeter && event.greeter!== "") {
        greeter = event.greeter;
    } 
    // もしイベントオブジェクトに body プロパティが含まれ、かつその値が空でない場合
    else if (event.body && event.body !== "") {
        // イベントオブジェクトの body プロパティを JSON オブジェクトとして解析する
        var body = JSON.parse(event.body);
        // もし body オブジェクトに greeter プロパティが含まれ、かつその値が空でない場合
        if (body.greeter && body.greeter !== "") {
            greeter = body.greeter;
        }
    } 
    // もしイベントオブジェクトに queryStringParameters プロパティが含まれ、かつその中に greeter プロパティが含まれ、かつその値が空でない場合
    else if (event.queryStringParameters && event.queryStringParameters.greeter && event.queryStringParameters.greeter !== "") {
        greeter = event.queryStringParameters.greeter;
    } 
    // もしイベントオブジェクトに multiValueHeaders プロパティが含まれ、かつその中に greeter プロパティが含まれ、かつその値が空でない場合
    else if (event.multiValueHeaders && event.multiValueHeaders.greeter && event.multiValueHeaders.greeter != "") {
        // multiValueHeaders の greeter プロパティの値を " and " で連結する
        greeter = event.multiValueHeaders.greeter.join(" and ");
    } 
    // もしイベントオブジェクトに headers プロパティが含まれ、かつその中に greeter プロパティが含まれ、かつその値が空でない場合
    else if (event.headers && event.headers.greeter && event.headers.greeter != "") {
        greeter = event.headers.greeter;
    } 
    // レスポンスオブジェクトの body プロパティを挨拶語に 'Hello, ' を追加した文字列に設定する
    res.body = "Hello, " + greeter + "!";
    // コールバック関数を呼び出し、レスポンスオブジェクトとエラーを null で返す
    callback(null, res);
};