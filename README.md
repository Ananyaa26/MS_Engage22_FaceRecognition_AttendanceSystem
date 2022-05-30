# MS Enage 2022 Face Recognition Attendance System
####  This project is made under Microsoft Engage 2022 Program.
####  Attendance Tool via Face Recognition is a Python Tkinter GUI based Opencv Project which stores variety of details of students and records their attendance on real time basis in a CSV file directly.
#### Use of Haarcascade Classifier and LBPH Algorithm has been used to capture,train,detect and recognize the images.

       
## Features Of the Project

  ####  → Loging Security System (Username & Password)
  ####  → Home Page
  ####  → Student Database System (Save, Take Photo Samples, Reset, Clear) 
  #### →  Train Photo Samples 
  #### → The Photos are saved in a Separate folder.
  ####  →  Take Attendance with Face Detection 
  ####  → Attendance Report (Excel file & MySql database) 
  ####  → Developer Page


## ==========Brief Description of all the Pages=============
## Login Window 

#### The login window comprises of two entries and three buttons.
#### On entering the mentioned username and password it will direct to the main page.
#### Leaving the fields empty or entering the wrong info will lead to error message.This ensures Authentication of the system

![Screenshot 2022-05-28 181622](https://user-images.githubusercontent.com/89255668/170838702-570a1e9b-a194-43cb-98b6-95ed8a69634a.jpg)

## Main Page

#### 6 buttons have been incorporated on the main page leading to different sections of the project.
#### These are as follows:
      1) Details
      2) Face Recognizer
      3) Attendance
      4) Train Data
      5) Photos
      6) Helpdesk

![Screenshot 2022-05-23 165806](https://user-images.githubusercontent.com/89255668/170838711-cdb07d75-5836-49a7-afd4-d613b9c3496f.jpg)

## Details
#### This page is the form which stores the personal information and details of student.
#### The records that can be saved are :
      # Entry Fields
      
      Student ID
      Name
      Enrollment No.
      Gender
      Date of Birth 
      Phone No.
      Email ID
      
      # Combo Buttons
      
      Department Name
      Course Name
      Current Year
      Current Semester
      
 #### The *Take Photo* button will capture 100 images and store them
 #### Reset the data button clears all the entries.
 #### This page is made by creating various frames for different sections and using the grid feature of tkinter to locate them on the page.
 #### You can check the data being saved simultaneously on Mysql Workbench
      
![Screenshot 2022-05-29 124243](https://user-images.githubusercontent.com/89255668/170856747-7bdbe409-e94c-4cb8-b4e6-a1655d9a0695.jpg)

### Mysql Workbench

![Screenshot 2022-05-29 124319](https://user-images.githubusercontent.com/89255668/170858697-2fcf8137-3bfb-4c80-bded-79a9187b82f0.jpg)


## Train Data and LBPH Algorithm
  ### Reason to Choose LBPH Algorithm
  
1)  LBPH is one of the easiest face recognition algorithms.
2)  It can represent local features in the images.
3)  It is possible to get great results (mainly in a controlled environment).
4)  It is robust against monotonic gray scale transformations.
5)  It is provided by the OpenCV library (Open Source Computer Vision Library).
  ### Working of the Algorithm
  
![image](https://user-images.githubusercontent.com/89255668/170859765-78ccf3e9-44a0-48a9-a555-753b78353e74.png)


  1)  As we have an image in grayscale, each histogram (from each grid) will contain only 256 positions (0~255) representing the occurrences of each pixel intensity.
  2)  Then, we need to concatenate each histogram to create a new and bigger histogram. 
  3)  Supposing we have 8x8 grids, we will have 8x8x256=16.384 positions in the final histogram. 
  4)  The final histogram represents the characteristics of the image original image.
  5)   Each histogram created is used to represent each image from the training dataset. 
  6)   For a given input image, we perform the steps again for this new image and creates a histogram which represents the image.
  7)   So to find the image that matches the input image we just compare two histograms and return the image with the closest histogram.
 

![image align="middle"](https://user-images.githubusercontent.com/89255668/170858938-c32421d7-94e8-42bf-8ec6-2d08717582e4.png)


### This is how the window looks while training the images.


![Screenshot 2022-05-29 001118](https://user-images.githubusercontent.com/89255668/170838774-7ef55766-c2f9-4448-8c66-2723ff5bb983.jpg)

## Face Detection 

### The Flow Chart of How the Face Detection Works using HaarCascade Classifier

<img width="600" alt="1-Figure1-1" src="https://user-images.githubusercontent.com/89255668/170859525-99e04581-6231-4139-bb81-1b789f017cbf.png">


### This page detect faces and recognize them with the help from the stored database.

![Screenshot 2022-05-27 013236](https://user-images.githubusercontent.com/89255668/170838784-0b88f28a-b08e-43c3-b89e-0d595344fee5.jpg)

## Attendance Record Page

  #### Importing the CSV file will display the attendance record in a tabular manner.
  #### Date and Time is is also recorded on real time basis.
  #### Reseting of data option available.
  #### The file can be exported to another CSV file on the desktop.



![Screenshot 2022-05-29 123435](https://user-images.githubusercontent.com/89255668/170856478-be3efd84-f652-4ee1-adf6-f65e563fdeee.jpg)


## Helpdesk

#### Details of developer.
![Screenshot 2022-05-27 051749](https://user-images.githubusercontent.com/89255668/170838801-eedc6278-637e-46ed-a5b9-0a2457f32f82.jpg)

## Video Demo Of the project

### The *video demo* of my project is [here](https://youtu.be/omjgzgBX_v8)

## Installation Commands Required

     pip install PIL
     pip install mysql-connector-python
     pip uninstall opencv-python
     pip3 install opencv-contrib-python
     pip install numpy
     
## Instructions to run

  1) Clone the repository
  2) Install Python 3
  3) Run the installation commands
  4) Login details: Username="Ananyaa" ; Password ="Test@12"
  5) Create a mysql schema name = "face_recognizer" and table name="details"
  6) The various column names are-dep,Course,Year,Semester,ID,Enrollment,Name,Gender,Phone,Email,DOB,Photo
  7) Mysql details: host = "localhost" ; username="root" ; password = "Sanskrit@12" ; database = "face_recognizer";

## Resources 

### [LBPH ALGORITHM](https://towardsdatascience.com/face-recognition-how-lbph-works-90ec258c3d6b)
### [Haarcascade Classifier](https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html)
### [Python Tkinter Playlist](https://youtu.be/mYVS7QjNjvg)

## Scope of the Project

####  Add additional feature of chatbox on helpdesk button
####  Work on Update and Search button on Details Page
  







