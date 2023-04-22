# ID Card Generator 

## Introduction
This is a simple Flask application for generating ID Cards in PDF format. It takes in user details and creates an ID Card with the provided information.

## Requirements
- Flask
- Pillow
- OpenCV
- Matplotlib

## Installation
1. Clone this repository.
2. Install the required packages using the following command: 
```
pip install flask pillow opencv-python matplotlib
```
3. Run the application using the command:
```
python app.py
```

## Usage
1. Open your web browser and go to http://localhost:34/.
2. Enter the required details (name, employee ID, designation, mandal, and SC Value).
3. Click on the `Submit` button to generate the ID Card in PDF format.

## How it works
1. The user enters their details in the web form and clicks on the `Submit` button.
2. The Flask application receives the details and calls the `id` function.
3. The `id` function generates an ID Card image using OpenCV and the user's details.
4. The ID Card image is saved in the `static` folder.
5. The `pdf` function converts the ID Card image to PDF format using Pillow.
6. The PDF is saved in the `static` folder.
7. The `index.html` file displays the generated PDF to the user.

## User-Interface

1. Home Page View
![home](https://github.com/nani-stark-3000/ID-Card-Generator/blob/a1afcaa9d55549c417438ce8fe9c280846d89ec8/ScreenShots/Initial%20View.png)

2. Data Filled View
![fill](https://github.com/nani-stark-3000/ID-Card-Generator/blob/a1afcaa9d55549c417438ce8fe9c280846d89ec8/ScreenShots/Data%20Filled%20View.png)

3. Generated View
![generated](https://github.com/nani-stark-3000/ID-Card-Generator/blob/a1afcaa9d55549c417438ce8fe9c280846d89ec8/ScreenShots/Generated%20View.png)

## Credits
This project was created by [Narendra Neeraj].
