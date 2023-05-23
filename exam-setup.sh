#zip -r question-resources.zip /home/labuser/Desktop/Project/*
#cd /home/labuser/Desktop/Project/
#git clone https://github.com/agskalsp/maycycle.git
cd /home/labuser/Desktop/Project/maycycle/quessolution/
cp -r /home/labuser/Desktop/Project/* /home/labuser/Desktop/Project/maycycle/quessolution/
git status
git add .
#git commit -am "Question and Resources Added"
git commit -am "update setup.sh"
git push https://ghp_@PRmO@0XJkp@zA5YXj2@miNwc3j@d7WfqOt@1z82@Ok@github.com/agskalsp/maycycle.git
git status