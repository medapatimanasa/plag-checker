Database link in sqlite format can be accessed from here :- https://drive.google.com/drive/folders/1rUTwUeupTpr19kNZkKNGacoefrmbl1wp?usp=sharing

## 1. Click on the "Fork" button in the upper-right corner of the page.

  <img align="center" width = "300" src = "https://docs.github.com/assets/cb-40742/mw-1440/images/help/repository/fork-button.webp" alt="fork image"/>

## 2.Clone the Forked Repository:
  #### Go to your GitHub account, open the forked repository, click on the code button and then click the copy to clipboard icon
![image](https://github.com/Surya-Abhinai/INTEL_QUEST-Plagiarism-Checker-/assets/124990558/7f0cd92a-893d-4860-ae47-364bc7fd3416)
  #### Use the git clone command to clone your forked repository to your local machine. Replace   <repository-url> with the URL of your forked repository.
  ```
  git clone <repository-url>
```

# Getting started with the project
Firstly, initialize a virtual environment in your local system, using the following command (after changing to the cloned repo directory): 
```
python3 -m venv .
```
In order to activate the virtual environment run the following command: 
```
source bin/activate
```
Following this, the dependencies can be installed by running the following command in the command line interface: 
```
pip install -r requirements.txt
```
Following this , Install the database from the link provided above and add that to your virtual environment.

Finally, the flask app can be launched by running the following command in the terminal: 
```
python main.py
```

# Project Overview 

**Data Extraction (Extract.py):** Metadata and XML content from JSON files are extracted, including title, number, authors, abstract, and main text. HTML tags, equations, and special characters are removed for clean text representation and they are stored in Qdrant vector database collection named "Research_papers" with vector configuration specifying cosine distance and on-disk storage.

**Text Extraction (Extract_User.py):** Upon file upload (PDF/DOCX/TXT), text is automatically extracted for further processing.

**Semantic Search (Search.py):** Utilizes Qdrant and Sentence Transformers to conduct semantic searches on a collection of research papers. Papers are represented as high-dimensional vectors for efficient search.

**Similarity Score Retrieval (Fetch_Score.py):** Encodes input text queries and searches the Qdrant collection for similar papers. Retrieves similarity scores and corresponding paper numbers.

**Text Chunking and Coloring:** Uploaded text is split into chunks of lines. Each line is compared against the Qdrant database, and based on similarity scores:

If similarity > ```0.65```: Text is colored red, indicating high similarity, and displays the similar paper ID.
If ```0.5``` ≤ similarity ≤ ```0.65```: Text is colored blue, indicating moderate similarity, and displays the similar paper ID.
If similarity < ```0.5```: Text remains unchanged, as similarity is too low for meaningful comparison.

**Workflow Integration:** Upon file upload, a copy is stored locally. The file path is then sent to the Output class, which retrieves the text. The text is split into sentences, and each sentence is passed to Fetch_Score for similarity score retrieval. Finally, text coloring is applied based on similarity scores, and the result is displayed to the user.

![image](https://github.com/Surya-Abhinai/INTEL_QUEST-Plagiarism-Checker-/assets/124990558/9dd913ee-8da1-4426-a804-5913e734baa2)

![image](https://github.com/Surya-Abhinai/INTEL_QUEST-Plagiarism-Checker-/assets/124990558/be992b30-2265-4f1d-ba02-56aecb1f23a1)
