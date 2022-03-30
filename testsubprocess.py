import subprocess
import pandas as pd

if __name__=='__main__':
    ## basic
   # subprocess.run(["ls","-l"])
   # for i in [2,5,6,8]:
     #   subprocess.run(["python", "python_script_101.py", "9", "--x", "5", "--yval", f"{i}"])
        
    #pro = subprocess.Popen(["ls","-l"],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #out, err = pro.communicate()
    #print(out)
    
    ##HW ให้ print เฉพาะ ตัวเลขผลลัพธ์ของการคูณ
    for i in [2,5,6,8]:
        pro1 = subprocess.Popen(["python", "python_script_101.py", "9", "--x", "2", "--yval", f"{i}"],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out1, err = pro1.communicate()
        print(str(out1)[29:31])