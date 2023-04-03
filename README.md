# canis-app

This is a Flask deployment for the DistilBERT model fine-tuned on the dataset provided as part of the CANIS 2023 Hackathon. This model can classify news articles into fake or real based on articles pasted into the text box.


To run this flask application, simply clone this repository and run the "app.py" file. You can run using this following command: python app.py

Prerequisites:
You need to install pytorch and the transformers modules for this to work. This can be done by running the following commands:
1. pip install torch
2. pip install transformers

You can also use the requirements.txt file to install packages if any other packages are missing.


The dataset used for fine-tuning the DistilBERT model ican be found at this link: https://drive.google.com/file/d/1VzPLqc1wQZfzsdgLoWX-CL6rpm2dXMYm/view?usp=sharing. 

This dataset was created by adding labels to each row in the given datasets (1 for the true news dataset and 0 for the fake news dataset). The 2 datasets were then combined and shuffled. The resulting shuffled dataset was then used to fine-tune the DistilBERT model, and later deployed to a flask application.

The code for training the model can be found in the Model_Train.ipynb file.
