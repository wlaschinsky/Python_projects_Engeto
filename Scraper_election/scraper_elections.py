"""

projekt_3.py: třetí projekt do Engeto Online Python Akademie

author: Samuel Wlaschinsky

email: wlaschinsky.samuelr@gmail.com
email: samuel.wlaschinsky@daktela.com

discord: samuel_qa

"""

import sys
import bs4
import requests
import csv


# Globals variables
total_voters = []
total_attendance = []
total_valid_votes = []

# Function to download HTML
def download_html(url):
    """Downloads HTML from the given URL in argument and returns object."""
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to download data from {url}. Status code: {response.status_code}")
        return None
    print("DOWNLOADING DATA FROM URL:", url)
    return bs4.BeautifulSoup(response.text, "html.parser")

# Function to extract town names from <td> with class "overflow_name" by using the find_all method
def extract_town_names(html_soup):
    """Returns a list of towns from the HTML content."""
    town_names = []
    towns_search = html_soup.find_all("td", "overflow_name")
    for t in towns_search:
        town_names.append(t.text)
    return town_names

# Function to extract links for individual towns
def extract_town_links(html_soup):
    """Returns URLs for detailed results of individual towns."""
    town_urls = []
    link_search = html_soup.find_all("td", "cislo")
    for link_town in link_search:
        
        # Link_town.a searches for the first <a> tag (url) inside link_town
        if link_town.a:
            link_town = link_town.a["href"]
            town_urls.append(f"https://www.volby.cz/pls/ps2021/{link_town}")
    return town_urls

# Function to extract town IDs
def extract_town_ids(html_soup):
    """Returns the IDs of individual towns."""
    town_ids = []
    ids_search = html_soup.find_all("td", "cislo")
    for i in ids_search:
        town_ids.append(i.text)
    return town_ids

# Function to extract list of political parties
def extract_parties(html_soup):
    """Returns a list of political parties in the given district."""
    parties = []
    town_links = extract_town_links(html_soup)
    html_first_town = download_html(town_links[0])
    if html_first_town:
        party_search = html_first_town.find_all("td", "overflow_name")
        for party in party_search:
            parties.append(party.text)
    return parties

# Function to gather data about voters, attendance, and valid votes
def gather_voter_data():
    """Fills global variables with data about voters, attendance, and valid votes from each town."""
    town_links = extract_town_links(html_content)
    for link in town_links:
        html_town = download_html(link)
        if html_town:
            voters_search = html_town.find_all("td", headers="sa2")
            for v in voters_search:
                total_voters.append(v.text)
            attendance_search = html_town.find_all("td", headers="sa3")
            for a in attendance_search:
                total_attendance.append(a.text)
            valid_votes_search = html_town.find_all("td", headers="sa6")
            for valid in valid_votes_search:
                total_valid_votes.append(valid.text)

# Function to gather votes for political parties
def gather_party_votes():
    """Returns a list of lists with the percentage results of parties for each town."""
    party_votes = []
    town_links = extract_town_links(html_content)
    for link in town_links:
        html_town = download_html(link)
        if html_town:
            vote_search = html_town.find_all("td", "cislo", headers=["t1sb4", "t2sb4"])
            temp_votes = []
            for vote in vote_search:
                temp_votes.append(vote.text + ' %')
            party_votes.append(temp_votes)
    return party_votes

# Function to create rows for CSV
def create_csv_rows():
    """Creates the data structure for the CSV file."""
    rows = []
    
    # Collect voter data
    gather_voter_data()  
    town_names = extract_town_names(html_content)  
    town_ids = extract_town_ids(html_content)    
    party_votes = gather_party_votes() 

    # Combine data into one list of rows
    for town_id, town_name, voters, attendance, valid_votes, votes in zip(town_ids, town_names, total_voters, total_attendance, total_valid_votes, party_votes):
        rows.append([town_id, town_name, voters, attendance, valid_votes] + votes)
    return rows

# Function to save election results to CSV
def save_election_results(output_file):
    """Creates a CSV file with the election results."""
    
    # Try to save the data to a CSV file and catch any exceptions
    try:
        header = ['Town ID', 'Town Name', 'Registered Voters', 'Issued Ballots', 'Valid Votes']
        csv_rows = create_csv_rows()
        parties = extract_parties(html_content)

        # Add party names to the header
        header.extend(parties)

        print("SAVING DATA TO FILE:", output_file)
        with open(output_file, 'w', newline='') as f:
            writer = csv.writer(f)
            
            # Write the header to the CSV file
            writer.writerow(header) 
            
            # Write the data rows to the CSV file
            writer.writerows(csv_rows)   # Write the data rows to the CSV file
        print("FINISHED:", sys.argv[0])
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function to run the script and save the election results to a CSV file
"""Check if the script was called with the correct number of arguments. [0] = file, [1] = URL, [2] = output file name."""
if __name__ == '__main__':
    if len(sys.argv) == 3:
        url = sys.argv[1]
        output_file = sys.argv[2]
        html_content = download_html(url)
        if html_content:
            save_election_results(output_file)
    
    # If the script was called with the wrong number of arguments, print an error message
    else:
        print('Incorrect number of arguments. Expecting 2: URL and output file name.')
        sys.exit(1)
