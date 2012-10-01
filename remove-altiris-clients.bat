REM Uninstall All NS Agents
REM Based on comments here: http://www.symantec.com/connect/forums/how-can-i-uninstall-altiris-agent-workstation#comment-7727

"C:\Program Files (x86)\Altiris\Altiris Agent\AeXAgentUtil.exe" /UninstallAgents
"C:\Program Files (x86)\Altiris\Altiris Agent\AeXAgentUtil.exe" /ResetGuid
"C:\Program Files (x86)\Altiris\Altiris Agent\AeXAgentUtil.exe" /Clean
RD "C:\Program Files (x86)\Altiris\Altiris Agent" /s /q
sc delete AltirisACSvc
sc delete Aclient
sc delete "Altiris Deployment Agent"
