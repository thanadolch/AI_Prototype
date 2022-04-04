# AI_Prototype

นาย ธนดล ชัยเนตร 613020240-5

### anaconda environment
    conda install                   ติดตั้งpackage ที่ต้องการ
    conda create -n  python         สร้าง environment
    conda activate                  เรียกใช้ environment
    conda deactivate                เลิกใช้งาน environment
    conda info --envs               มีvirtual environment อะไรบ้าง
### command line
    ls          ตรวจเช็คไฟล์ในrootต่างๆ
    ls -l       แสดงข้อมูลของไฟล์อย่างละเอียด
    clear       เคลียร์ คำสั่งต่างๆที่แสดงบน terminal
    cd          เลือก path ที่ต้องการเข้าถึง
    mkdir       สร้างโฟล์เดอร์
    rm          ลบไฟล์
    rm -R       ลบทุกไฟล์ที่อยู่ในโฟล์เดอร์นั้น
    code        คำสั่งเพื่อเปิดไฟล์ด้วย visual studio code
    screen -S   สร้างหน้าต่างเพิ่มขึ้นอีก 1 หน้า
    screen -R   ย้อนกลับไปในหน้า screen นั้น ๆ
    ctrl+A+D    ออกจากหน้า screen
    screen -R   กลับเข้าไปใน screen ที่สร้างไว้

### เนื้อหาในคอร์สเรียน
#### Flask เป็น Package ที่ใช้สำหรับพัฒนาเว็บแอปพลิเคชันและเรียนCookie
* ### Flask file : [[code]](https://github.com/thanadolch/AI_Prototype/blob/main/Flask.py)
* ### Home.html file : [[code]](https://github.com/thanadolch/AI_Prototype/blob/main/templates/home.html)
* ### csv file : [[code]](https://github.com/thanadolch/AI_Prototype/blob/main/db.csv)
* ### Test Requests [[code]](https://github.com/thanadolch/AI_Prototype/blob/main/reqyest.py)
* ### Subprocess : [[code]](https://github.com/thanadolch/AI_Prototype/blob/main/testsubprocess.py)
* ### Python Argparse : [[code]](https://github.com/thanadolch/AI_Prototype/blob/main/python_script_101.py)
* ### Cloud DB & Cloud AI [[code]](https://github.com/thanadolch/AI_Prototype/blob/main/Cloud_DB_and_Ai.ipynb)
## Neural Network with Tensorflow [[code]](https://github.com/thanadolch/AI_Prototype/blob/main/tensorflow(network).ipynb)
 การสร้าง Neural Network ด้วย Tensorflow Sequential API:
        
         Sequentail - สามารถสร้างได้ง่าย ไม่มีความซับซ้อน แต่ network จะวิ่งเป็นเส้นตรง
        
         Functional - สร้างได้ยากกว่า Sequentail  ได้ network ที่สามารถปรับแต่งเส้นทางให้มีความซับซ้อนได้
        
         Subclassing - สร้างได้ยาก โดยในส่วนนี้ไม่ได้เรียนในคอร์ส
  Download and prepare the CIFAR10 dataset: 
               
         https://www.kaggle.com/datasets/wordroid/cifar10-object-recognition-in-images-zip-file


