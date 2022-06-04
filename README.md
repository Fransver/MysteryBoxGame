# Mystery Box Camera Game 

<img src="https://s3.us-east-2.amazonaws.com/surdek/media/blog/_1200xAUTO_fit_center-center_90_none/mysterious-box-agile.jpg" width="600">

### Introduction
Within this code-project I've build a game that uses multiple python and C++-oriënted libraries. They work together to create an awesome game where users must play together to crack a code. This is how it works. 

1. A user opens the game and a Tkinter GUI appears. This GUI holds difficulty settings, an Explain button and a Quit button. The design is simple and easy to understand for all ages. 
2. When a user selects a difficulty setting. The game immediatly starts by starting the camera. A player will see his own hands detected by the algorithm from mediapipe. The tracking of the fingers, corresponds with a increment of risen fingers. The number of risen fingers will give an output-number that will be shown in the feed.
3. When a user wants to capture the output, he/she can press V or the Arduino-button to send the attempt to the algorithm. If the attempt is correct, the number will be shown in the empy code-list, showing in the feed. If it is not correct, a text will be shown that it is not what we are looking for. 
4. If a player cracks all the numbers of the asked code, the game will be over and will be celebrated by a success message. When the code isn't cracked Within the given time, a fail-screen will appear with the option to try again. 

### 04-06-2022 REDME update

In the last update I've refactored my code following a 
feedback-input in my Portfolio from my teacher.
- Renaming classes more to their function instead of module names. 
- Cutting classes that can be easily replaced with an internal type.
(LevelTimer, Score)
- Deleted states CameraGame and replaced with one game. Acting on the difficulty setting from the timer.
- Make a relative path for the photo in the GUI. 
- make seperate function count dictionary so unit-test is possible 

### 25-05-2022 README update     
In the last update I've added the following things:
- Additional Unit-Tests 
- Color-update GUI

### 06-05-2022 README update
In the last update I've added:
- Explain Button
- Timer class problem solved
- Multiple difficulty settings. 

### 26-04-2022 README update
- Classes build complete
- Design by: Game Design Pattern
- Tkinter class starting Screen. 

