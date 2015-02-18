<html>
<head><title>test PHP</title></head>
<body>

<?php

$link = mysql_connect('music_info.db','user','pass');
if(!$link){
	die('接続失敗'.$sqliteerror);
}

print('接続に成功しました.<br>');

mysql_close($link);

print('切断しました.<br>');

?>

</body>
</hrml>