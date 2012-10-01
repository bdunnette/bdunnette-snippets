REM Uninstall All NS Agents

"C:\Program Files (x86)\Altiris\Altiris Agent\AeXAgentUtil.exe" /UninstallAgents
"C:\Program Files (x86)\Altiris\Altiris Agent\AeXAgentUtil.exe" /ResetGuid
"C:\Program Files (x86)\Altiris\Altiris Agent\AeXAgentUtil.exe" /Clean
RD "C:\Program Files (x86)\Altiris\Altiris Agent" /s /q
sc delete AltirisACSvc
sc delete Aclient
sc delete "Altiris Deployment Agent"
