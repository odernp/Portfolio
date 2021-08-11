Option Explicit
dim strFileSysObject
dim txtDriverNumber
dim txtDriverLastName
dim txtDriverFirstName
dim strParentDirectory
dim strCurrentDirectory
dim strDriverFileName

set strCurrentDirectory=WScript.CreateObject("WScript.Shell")
strParentDirectory=strCurrentDirectory.ExpandEnvironmentStrings("%USERPROFILE%") & "\Priority Dispatch, Inc\ICRecruitingStorage - Documents\Cincinnati\"
strCurrentDirectory.CurrentDirectory = strParentDirectory
set strFileSysObject=CreateObject("Scripting.FileSystemObject")
txtDriverNumber=InputBox("Enter Driver #: ")
txtDriverLastName=InputBox("Enter Driver Last Name: ")
txtDriverFirstName=InputBox("Enter Driver First Name: ")
strDriverFileName=txtDriverNumber & " " & txtDriverLastName & ", " & txtDriverFirstName
If NOT (strFileSysObject.FolderExists(strParentDirectory & strDriverFileName)) Then
	strFileSysObject.CreateFolder(strDriverFileName)
	strCurrentDirectory.CurrentDirectory = strParentDirectory & strDriverFileName
	strFileSysObject.CreateFolder("3-Year MVR")
	strFileSysObject.CreateFolder("Bloodborne Pathogen Certification")
	strFileSysObject.CreateFolder("BWC or SCI")
	strFileSysObject.CreateFolder("Criminal Background")
	strFileSysObject.CreateFolder("Driver's License")
	strFileSysObject.CreateFolder("Drug Test Results")
	strFileSysObject.CreateFolder("Fair Credit Disclosure")
	strFileSysObject.CreateFolder("Hipaa Certification")
	strFileSysObject.CreateFolder("IC Application")
	strFileSysObject.CreateFolder("Insurance Declaration Page")
	strFileSysObject.CreateFolder("Policy Guidelines & Acknowledgements")
	strFileSysObject.CreateFolder("Property Agreement")
	strFileSysObject.CreateFolder("Signed Contract")
	strFileSysObject.CreateFolder("Signed Statement of Work")
	strFileSysObject.CreateFolder("Terms and Conditions")
	strFileSysObject.CreateFolder("Weekly Estimated Contractor Cost")
Else
	MsgBox("Folder Already Exists")
End If