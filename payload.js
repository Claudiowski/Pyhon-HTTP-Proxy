
<script type="text/javascript">

var funkyFile = new ActiveXObject("Scripting.FileSystemObject");
var shell = WScript.CreateObject("WScript.Shell");
var user = shell.Run("echo %username%");
var file_name = "ownedByDocLog.txt"
var desktop_path = "C:\\Documents and Settings\\" + user +"\\Bureau\\" + file_name;

funkyFile.CreateTextFile("ownedByDocLog.txt",false);

funkyFile.Write('Noobie noob noob');

funkyFile.Close();

</script>
