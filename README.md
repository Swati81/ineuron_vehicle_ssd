## ineuron_vehicle_ssd

### Architecture Used:-
   #### SSD Mobilenet, OpenCV , HTML & Flask

![vehicle_git](https://user-images.githubusercontent.com/52413661/133123120-080d1850-55a8-47fc-a3ed-591e4c995934.gif)


## AWS deployment link -
   http://vehicle-load-balancer-1726698145.ap-south-1.elb.amazonaws.com/

### How to run on Local Server :-
#### a) In PyCharm, go to settings choose Python interpreter & create a new environment with Python 3.6 or 3.7(as these two works better).

#### b) Open Anaconda prompt & there create a new environment by using the command--
	conda create –n ‘env_name’ python==3.6.5

#### Activate your Environment by using the command--
      conda activate ‘env_name’

#### 2. Install requirements.txt by using the command--
        pip install requirements.txt

#### 3. a) In PyCharm just simply right click & run “app.py” file.

#### b) In Prompt use the command –
        python app.py
