# Election Results Scraper

## Project Description

This script downloads and processes the results of the 2021 parliamentary elections in the Czech Republic for a specified region. The results are processed and saved into a CSV file. The script collects results for all municipalities in the given region, including information on registered voters, turnout, and the results of individual political parties.

The data is retrieved based on the URL provided by the user as an argument when running the script.

## Library and Virtual Environment Installation

Steps to set up a virtual environment and install dependencies:

1. **Create and activate a virtual environment**:

   ```bash
   python -m venv myenv (myenv=name of the virtual environment)
   source myenv/bin/activate

2. **The required libraries are installed using the requirements.txt file included in the project.**
    ```bash
    pip3 install -r requirements.txt

3. **After completing the work, deactivate the virtual environment:**
    ```bash 
    deactivate

4. **To remove the virtual environment, use the command:**
    ```bash
    rm -rf myenv

## Running Script

* The script requires two arguments to run properly:

    * The URL of the region for which you want to download the results (e.g., results for the Louny region). You can choose the region from [this link](https://www.volby.cz/pls/ps2021/ps3?xjazyk=CZ), click on the "X" next to the region, and use the URL of the resulting page.
      
    * The name of the output file in .csv format where the results will be saved. If the file does not exist, the script will create it with the specified name.

* Example of running the script:
    ```bash
    python scraper_elections.py  "https://www.volby.cz/pls/ps2021/ps32?xjazyk=CZ&xkraj=6&xnumnuts=4204" "vysledky_louny".csv

* The script will download the results for the Louny region from the provided URL, and the results will be saved in the vysledky_louny.csv file.

## Script Execution

* Downloading data:

    ```bash
    DOWNLOADING DATA FROM URL: https://www.volby.cz/pls/ps2021/ps311?xjazyk=CZ&xkraj=6&xobec=565997&xvyber=4204

* Saving data:

    ```bash
    SAVING DATA TO FILE: vysledky_louny.csv


* Completion:

    ```bash
    FINISHED: scraper_elections.py


## Output example

    ```bash
    Town ID,Town Name,Registered Voters,Issued Ballots,Valid Votes,Strana zelených,Švýcarská demokracie,VOLNÝ blok,Svoboda a př. demokracie (SPD),Česká str.sociálně demokrat.,ALIANCE NÁRODNÍCH SIL,Trikolora Svobodní Soukromníci,Aliance pro budoucnost,Hnutí Prameny,PŘÍSAHA Roberta Šlachty,"SPOLU – ODS, KDU-ČSL, TOP 09",Urza.cz: Nechceme vaše hlasy,Koruna Česká (monarch.strana),PIRÁTI a STAROSTOVÉ,Komunistická str.Čech a Moravy,ANO 2011,Otevřeme ČR normálnímu životu

    565997,Bitozeves,358,195,194,"0,00 %","0,00 %","0,51 %","13,40 %","4,12 %","0,51 %","1,54 %","0,00 %","0,00 %","5,15 %","17,01 %","0,00 %","0,00 %","6,18 %","4,12 %","46,90 %","0,51 %"

    566004,Blatno,411,289,287,"1,04 %","0,00 %","0,00 %","11,49 %","2,09 %","0,00 %","2,43 %","0,00 %","0,00 %","5,57 %","12,54 %","0,00 %","0,00 %","10,10 %","10,80 %","42,85 %","1,04 %"

    566012,Blažim,215,125,125,"0,00 %","0,00 %","2,40 %","8,00 %","5,60 %","0,80 %","4,80 %","0,00 %","0,00 %","4,00 %","20,00 %","0,00 %","0,00 %","12,00 %","4,00 %","37,60 %","0,80 %"

    566021,Blšany,806,495,494,"1,21 %","0,20 %","2,63 %","10,12 %","2,63 %","0,00 %","1,01 %","0,00 %","0,20 %","5,06 %","13,36 %","0,00 %","0,00 %","10,72 %","3,64 %","48,58 %","0,60 %"

