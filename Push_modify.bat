@echo off

set date_time=%date:~0,-3% %time:~0,-3%
echo %date_time% >> modify.txt
echo д����ɣ�

git add modify.txt
git commit -m "�ű�һ������ʱ��"
echo ��ʼpush...
git push
echo push���!

pause