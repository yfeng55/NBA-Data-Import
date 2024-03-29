import sys
import json
import urllib2
from bs4 import BeautifulSoup
import re
import os.path
import time


##### function for resolving names #####
def matchNames(player_name):

	playername = player_name.split(' ')[1][0:5] + player_name.split(' ')[0][0:2] + "01"
	
	if(player_name == 'jeff ayres'):
		playername = 'pendeje02'
	elif(player_name == 'harrison barnes'):
		playername = 'barneha02'
	elif(player_name== 'matt barnes'):
		playername = 'barnema02'
	elif(player_name == 'bojan bogdanovic'):
		playername = 'bogdabo02'
	elif(player_name == 'anthony brown'):
		playername = 'brownan02'
	elif(player_name == 'markel brown'):
		playername = 'brownma02'
	elif(player_name == 'clint capela'):
		playername = 'capelca01'
	elif(player_name == 'anthony davis'):
		playername = 'davisan02'
	elif(player_name == 'mike dunleavy'):
		playername = 'dunlemi02'
	elif(player_name == 'danny green'):
		playername = 'greenda02'
	elif(player_name == 'jeff green'):
		playername = 'greenje02'
	elif(player_name == 'pj hairston'):
		playername = 'hairspj02'
	elif(player_name == 'jordan hamilton'):
		playername = 'hamiljo02'
	elif(player_name == 'tim hardaway'):
		playername = 'hardati02'
	elif(player_name == 'tobias harris'):
		playername = 'harrito02'
	elif(player_name == 'gerald henderson'):
		playername = 'hendege02'
	elif(player_name == 'john holland'):
		playername = 'hollajo02'
	elif(player[6] == 'christapher_johnson'):
		playername = 'johnsch04'
	elif(player_name == 'joe johnson'):
		playername = 'johnsjo02'
	elif(player_name == 'stanley johnson'):
		playername = 'johnsst04'
	elif(player_name == 'dahntay jones'):
		playername = 'jonesda02'
	elif(player_name == 'james jones'):
		playername = 'jonesja02'
	elif(player_name == 'brandon knight'):
		playername = 'knighbr03'
	elif(player_name == 'david lee'):
		playername = 'leeda02'
	elif(player_name == 'kevin martin'):
		playername = 'martike02'
	elif(player_name == 'wesley matthews'):
		playername = 'matthwe02'
	elif(player_name == 'andre miller'):
		playername = 'millean02'
	elif(player_name == 'markieff morris'):
		playername = 'morrima02'
	elif(player_name == 'marcus morris'):
		playername = 'morrima03'
	elif(player_name == 'xavier munford'):
		playername = 'munfoxa02'
	elif(player_name == 'larry nance'):
		playername = 'nancela02'
	elif(player_name == 'willie reed'):
		playername = 'reedwi02'
	elif(player_name == 'andre roberson'):
		playername = 'roberan03'
	elif(player_name == 'glenn robinson'):
		playername = 'robingl02'
	elif(player_name == 'jakarr sampson'):
		playername = 'sampsja02'
	elif(player_name == 'jonathon simmons'):
		playername = 'simmojo02'
	elif(player_name == 'greg smith'):
		playername = 'smithgr02'
	elif(player_name == 'jason smith'):
		playername = 'smithja02'
	elif(player_name == 'josh smith'):
		playername = 'smithjo03'
	elif(player_name == 'isaiah thomas'):
		playername = 'thomais02'
	elif(player_name == 'jason thompson'):
		playername = 'thompja02'
	elif(player_name == 'kemba walker'):
		playername = 'walkeke02'
	elif(player_name == 'alan williams'):
		playername = 'willial03'
	elif(player_name == 'lou williams'):
		playername = 'willilo02'
	elif(player_name == 'marcus williams'):
		playername = 'willima04'
	elif(player_name == 'marvin williams'):
		playername = 'willima02'
	elif(player_name == 'mo williams'):
		playername = 'willima01'
	elif(player_name == 'metta world peace'):
		playername = 'artesro01'
	elif(player_name == 'brandan wright'):
		playername = 'wrighbr03'

	return playername;

##### end matchNames() function #####


##### function to format name #####
def formatName(name):

	player_name = None;

	# remove "jr" from any player names
	if(name[-3:] == 'jr.'):
		player_name = name[:-4]

	# remove special chars from player names
	player_name = re.sub('[!@#$-.]', '', name)

	return player_name

##### end formatName() function


# get user provided arguments
endyr = sys.argv[1][5:]
doAll = True

if(len(sys.argv) > 2):
	name = sys.argv[2].split('_')[0] + ' ' + sys.argv[2].split('_')[1]
	doAll = False
else:
	name = None



# user agent header for all http requests -- set to mozilla firefox browser
request_headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

# loop through each year specified in the range
while (int(sys.argv[1][2:4]) < int(endyr)) and doAll:

	season = '20'+str(int(endyr)-1)+'-'+str(endyr)

	# get activeplayers list from the activeplayers_file (stored locally)
	with open('../data-local/activeplayers/activeplayers_' + season + '.json') as activeplayers_file:
		activeplayers = json.load(activeplayers_file)


	# loop through all players in the activeplayers file
	for player in activeplayers['resultSets'][0]['rowSet']:


		player_id = player[0]
		player_name = player[2].lower()
		player_start = str(int(player[4])+1)
		player_end = player[5]

		# get a list of years between start and end (inclusive)
		player_yearrange = range(int(player_start), int(player_end)+1)


		# check if file already exists in filesystem for this player
		if not os.path.isfile("../data-local/gamelogs/" + str(player_id) + ".json"):

			player_name = formatName(player_name)

			# hard coded player name cases
			if(player_name == 'nene'):
				player_name = 'nene hilario'
			elif(player_name == 'jose juan barea'):
				player_name = 'josejuan barea'
			elif(player_name == 'luc mbah a moute'):
				player_name = 'luc mbahamoute'
			elif(player_name == 'james michael mcadoo'):
				player_name = 'jamesmichael mcadoo'
			
			playername = matchNames(player_name)
			

			# parse arguments
			displayname = player_name.split(' ')[0].title() + " " + player_name.split(' ')[1].title()
			season_endyr = '20'+str(endyr)

			print("\nPLAYERNAME: " + playername)
			print("RANGE: " + player_start + "-" + player_end)


			# output object
			output = {}
			output['player_name'] = displayname
			output['player_id'] = player_id
			output['seasons_played'] = player_yearrange


			# iterate through all seasons that the current player has played in
			for currentyear in player_yearrange:

				datekey = str(currentyear-1) + "-" + str(currentyear)[-2:]
				output[datekey] = []

				# (1) construct request url
				request_url = "http://www.basketball-reference.com/players/" + playername[0] + "/" + playername + "/gamelog/" + str(currentyear) + "/";
				print("--> downloading... " + request_url)
				request = urllib2.Request(request_url, headers=request_headers)

				# (2) download page as HTML file
				response = urllib2.urlopen(request)
				content = response.read()

				# (3) extract table from HTML document 
				# content = BeautifulSoup(content)
				content = BeautifulSoup(content, "html.parser")

				table = content.find("table", {"class":"sortable row_summable stats_table"})
				try:
  					rows = table.find_all("tr");
				except AttributeError: 
  					print('Player did not play for ' + datekey + ' season')
  					rows = ''


				# (4) iterate over rows and get cell values
				print("length: " + str(len(rows)) + "\n")

				
				for row in rows:

					# get cells in the row
					cells = row.find_all("td")
					game_arr = []

					if(cells and len(cells) > 9):
						try:
							for i in range(0,30):
								cellvalue = cells[i].get_text()
								game_arr.append(cellvalue)
						except:
							for i in range(0,29):
								cellvalue = cells[i].get_text()
								game_arr.append(cellvalue)

					elif(cells and len(cells) == 9):
						for i in range(0,9):
							cellvalue = cells[i].get_text()
							game_arr.append(cellvalue)

					output[datekey].append(game_arr)


			# write output to a json file
			with open('../data-local/gamelogs/' + str(player_id) + '.json', 'w') as outfile:
				json.dump(output, outfile)

			# wait for 2 seconds before fetching the next player
			time.sleep(2)
			print('(waiting for 2 seconds before fetching next player...)')


		else:
			print("FILE ALREADY EXISTS FOR " + str(player_id) + ", SKIPPING")


	endyr = int(endyr) - 1


#Downloads gamelogs for one player
if not (doAll):
	season = '20'+str(int(endyr)-1)+'-'+str(endyr)

	# get activeplayers list from the activeplayers_file (stored locally)
	with open('../data-local/activeplayers/activeplayers_' + season + '.json') as activeplayers_file:
		activeplayers = json.load(activeplayers_file)


	# loop through all players in the activeplayers file
	for player in activeplayers['resultSets'][0]['rowSet']:

		player_id = player[0]
		player_name = player[2].lower()
		player_start = str(int(player[4])+1)
		player_end = player[5]

		# get a list of years between start and end (inclusive)
		player_yearrange = range(int(player_start), int(player_end)+1)

		# check if file already exists in filesystem for this player
		if not os.path.isfile("../data-local/gamelogs/" + str(player_id) + ".json") and name == player_name:

			player_name = formatName(player_name)

			# hard coded player name cases
			if(player_name == 'nene'):
				player_name = 'nene hilario'
			elif(player_name == 'jose juan barea'):
				player_name = 'josejuan barea'
			elif(player_name == 'luc mbah a moute'):
				player_name = 'luc mbahamoute'
			elif(player_name == 'james michael mcadoo'):
				player_name = 'jamesmichael mcadoo'
			
			playername = matchNames(player_name)
			

			# parse arguments
			displayname = player_name.split(' ')[0].title() + " " + player_name.split(' ')[1].title()
			season_endyr = '20'+str(endyr)

			print("\nPLAYERNAME: " + playername)
			print("RANGE: " + player_start + "-" + player_end)


			# output object
			output = {}
			output['player_name'] = displayname
			output['player_id'] = player_id
			output['seasons_played'] = player_yearrange


			# iterate through all seasons that the current player has played in
			for currentyear in player_yearrange:

				datekey = str(currentyear-1) + "-" + str(currentyear)[-2:]
				output[datekey] = []

				# (1) construct request url
				request_url = "http://www.basketball-reference.com/players/" + playername[0] + "/" + playername + "/gamelog/" + str(currentyear) + "/";
				print("--> downloading... " + request_url)
				request = urllib2.Request(request_url, headers=request_headers)

				# (2) download page as HTML file
				response = urllib2.urlopen(request)
				content = response.read()

				# (3) extract table from HTML document 
				# content = BeautifulSoup(content)
				content = BeautifulSoup(content, "html.parser")

				table = content.find("table", {"class":"sortable row_summable stats_table"})
				try:
  					rows = table.find_all("tr");
				except AttributeError: 
  					print('Player did not play for ' + datekey + ' season')
  					rows = ''


				# (4) iterate over rows and get cell values
				print("length: " + str(len(rows)) + "\n")

				
				for row in rows:

					# get cells in the row
					cells = row.find_all("td")
					game_arr = []
					if(cells and len(cells) > 9):
						try:
							for i in range(0,30):
								cellvalue = cells[i].get_text()
								game_arr.append(cellvalue)
						except:
							for i in range(0,29):
								cellvalue = cells[i].get_text()
								game_arr.append(cellvalue)

					elif(cells and len(cells) == 9):
						for i in range(0,9):
							cellvalue = cells[i].get_text()
							game_arr.append(cellvalue)

					output[datekey].append(game_arr)


			# write output to a json file
			with open('../data-local/gamelogs/' + str(player_id) + '.json', 'w') as outfile:
				json.dump(output, outfile)
