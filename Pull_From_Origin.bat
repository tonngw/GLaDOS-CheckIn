@echo off

git remote add upstream https://github.com/ChenAi140/GLaDOS-CheckIn.git
git remote set-url upstream https://github.com/ChenAi140/GLaDOS-CheckIn.git
git fetch upstream
echo ��ȡ������ɣ�

echo ��ʼ�ϲ�...
git checkout main
git merge upstream/main

echo �ϲ���ɣ���ʼpush��

git push
echo push���!

pause