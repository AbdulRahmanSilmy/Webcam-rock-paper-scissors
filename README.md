# rock-paper-scissors
Play rock-paper-scissors through a webcam against a computer. Made possible with an image classifier. The model I used can be found [here.](https://drive.google.com/file/d/1sei12pat2sIh3FhN1PESCNiJ_l-MOr_f/view?usp=sharing)

## Steps

- Collect and label images per class.
- Use train_test_split module to seperate images to train and test files based on predefined ratio. 
- Train Image Classification model using transfer learning with Xception model in google colab.
- Deploy model with webcam using OpenCV
- Create rock-paper-scissor UI with OpenCV

## Gameplay

Run the play.py script to start the game. A video demo of the game can be found [here.](https://drive.google.com/file/d/1REm3BGTBYxXaEfUXW5ilFTou9CF9fcJK/view?usp=sharing)

<img src="https://github.com/AbdulRahmanSilmy/rock-paper-scissors/blob/main/gameplay_image.jpg" width="650" height="400" />
