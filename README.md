# Mystery Box Camera Game 

<img src="https://s3.us-east-2.amazonaws.com/surdek/media/blog/_1200xAUTO_fit_center-center_90_none/mysterious-box-agile.jpg" width="600">

### Introduction
Within this code-project I've build a game that uses multiple python and C++-oriënted libraries. They work together to create an awesome game where users must play together to crack a code. This is how it works. 

1. A user opens the game and a Tkinter GUI appears. This GUI holds difficulty settings, an Explain button and a Quit button. The design is simple and easy to understand for all ages. 
2. When a user selects a difficulty setting. The game immediatly starts by starting the camera. A player will see his own hands detected by the algorithm from mediapipe. The tracking of the fingers, corresponds with a increment of risen fingers. The number of risen fingers will give an output-number that will be shown in the feed.
3. When a user wants to capture the output, he/she can press V or the Arduino-button to send the attempt to the algorithm. If the attempt is correct, the number will be shown in the empy code-list, showing in the feed. If it is not correct, a text will be shown that it is not what we are looking for. 
4. If a player cracks all the numbers of the asked code, the game will be over and will be celebrated by a success message. When the code isn't cracked Within the given time, a fail-screen will appear with the option to try again. 

### CI/CD 

Within my project I wanted to learn more about Continious Integration and deployment and its strengths. I knew nothing about these concepts but studied the sources here on Git, together with a project-colleague. Together we tried to figure out wat CI/CD is and how it can benefit our project. The main source that I used for the research was [GITLAB CI/CD](https://docs.gitlab.com/ee/ci/). This source provided everything from the basics to project specific tutorials and tips. Also, the tutorial video wihtin the gitlab-section helped me understand the different concepts of building CI/CD pipelines. In my own code repository, these where the main steps for completing a working CI/CD-pipeline:
1. Setting up .yml 
With Gitlabs own CI/CD auto-functions, I succeeded in setting up a .yml template with ease. The template provided some explanation in the function of the .yml file and where its for. Immediatly after saving the document, the standard pipelines where running en failing. I didn't knew why it failed, but the failing-info provided the reason. I didn't have a suited gitlab-runner. This was my first step. 
2. Gitlab-runner
After finding the correct location for a suited gitlab-runner, I installed it on my work-laptop. With administration-rights I could start the runner en register my first runner. The third time was the charm and I understood where the first two failed (incorrect image names). After successfull installation, the second problem was visable in the pipeline: "Virtual Machine"
3. Docker
When I failed in setting up a virtual environment in a terminal, my project-colleague pointed me in the direction of Docker as a common used option. The Gitlab-tutorial provided a lot of information about docker, but it was somewhat overwelming. I tried to search for a step-by-step program for setting up a basic container and found the [correct page](https://docs.gitlab.com/ee/ci/docker/using_docker_images.html). I installed the Docker application and run into some BIOS-setting problems. My laptop blocked the use of this virtual machine and I allowed acces within the BIOS. After this, the Docker application was running smoothe and the registration of the container within the terminal was succeeded. I know had a working runner, with a correct Docker container registred. 
4. Build jobs 
The last step was connecting my unit-tests to the .yml file. For this I had to create a requirements.txt file for installing the needed moudels for the app. This was also new for me. I searched and found an easy option with "PIP-FREEZE". This created a .txt for me with all installed requirements. It was a large file and I knew that not all requirements where needed (some where installed when trying different libraries). I decided to delete the requirements, uninstall all libraries and start from scratch. After some time I got my application running again with the requirements cut by tenfold. 

## Conclusion
After completing this whole process of learning unfamilliar concepts in CI/CD I know now how to set up Continious Integration wihtin a repository. I understand the power of automating the process to prevent merge-conflicts and sticking to a projects syntax. I learned about setting up a testing-device with a runner, a docker virtual machine and collect the necessary requirements. All combbined in a easy to follow .yml file. 
This process was formed at the end of the semester but was a big learning-curve to take. I am glad to have taken on this challenge and will use the knowledge for all my future projects that can benefit from CI/CD. 

### 04-06-2022 README update

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

