# canis-app

To run this flask application, simply clone this repository and run the "app.py" file. You can run using this following command: python app.py

Prerequisites:
You need to install pytorch and the transformers modules for this to work. This can be done by running the following commands:
1. pip install torch
2. pip install transformers

You can also use the requirements.txt file to install packages if any other packages are missing.


The dataset used for fine-tuning the DistilBERT model is in the /dataset directory of this repository. This dataset was created by adding labels to each row in the given datasets (1 for the true news dataset and 0 for the fake news dataset). Then the 2 datasets were combined and shuffled. The resulting shuffled dataset was then used to fine-tune the DistilBERT model, and later deployed to a flask application.
