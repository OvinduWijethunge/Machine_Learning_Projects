# youtube-sinhala-spam-comments-filter-deployement
4th year research project deployment

<p align=center>
<img src="https://img.shields.io/badge/Type-classification-blue"/> 
<img src="https://img.shields.io/badge/Python-3.8-brightgreen"/>
<p/>
<br>
<p align=center>
  
</p>
<br>
<br>
• This is my sub module of fourth year research project, my task is identify spam comments in contents and filter spam commnets and make a legitimate comments file for next step of project, basically here i am
      
      1. download youtube comments (youtube data API)
      2. download youtube content as a text (youtube dll library)
      3. features extraction from data, extracted features are below
         1. comments - comments similerity
         2. comments - content similerity
         3. comments length
         4. number of sentences in a comment
         5. number of words in comment
         6. stop words ratio in a comment
         7. black word ratio in a comment
         8. post - comment time gap (my novelty)
         9. links availability in a comment
         10. phone numbers availability in a comment
         11. punctuatin marks ratio in a comments
         12. periods sequence availability of a comment (my novelty)
      4. feed my extracted features to the chosen model
      5. get predictions
      6. make a legitimate comments file for pass the next step of big project
      7. make a spam comments file for my use (for future enhancement of project) 
 


• If you want to check the algorithems ,models which used for implemented the model and see the accuracy matrix just Click the link mentioned below:<br />
Link: _https://github.com/OvinduWijethunge/Machine_Learning_Projects_

<hr>


### If you are willing to check project in flask API


### Prerequisites
You must have Scikit Learn, Pandas (for Machine Leraning Model) and Flask (for API) installed.

### Project Structure
This project has six major parts :
1. model.pkl - This is our built model for predict values.
2. app.py - This contains Flask APIs that youtube video id through GUI or API calls.
3. static - This uses for store css files and some gifs for while presenting.
4. templates - This folder contains the HTML template to allow user to enter required detail and displays the predicted output.
5. .py files - basically various functions that help for feauture extractions.
6. .xlsx/.csv files are the intermidiate and final outputs of workflow.


### Running the project in FLASK
type python app.py for start your server  (make sure you are in correct directly)
then copy the given url and paste it in your browser.
then input valid inputs and predict car price.
