#Pokebot hack with slight mods
#Shoutout to Tom The Botter, j-e-k, tejado, and countless others who helped to build most of this code base.

Requirements
	Install latest python and pip
	Google maps api key
	PTC or gmail account that has gone through the tutorial
    Visual C Compiler

Install instructions

	1) Install python 2.7. https://www.python.org/download/releases/2.7/
	2) Install pip by following these instructions: https://pip.pypa.io/en/stable/installing/
	3) Get a Google Direction API Key
		Follow these instructions up until step 4. Don’t proceed to step 5.
		https://github.com/AHAAAAAAA/PokemonGo-Map/wiki/Google-Maps-API:-a-brief-guide-to-your-own-key

	For OSX
		1) Move the entire bot folder into your Documents
		2) Open Terminal
		3) Enter the command “cd Documents/Pokebot\ with\ mods/“
		4) Run the command “pip install -r requirements.txt”
		5) Open config.json
		6) Enter your username, password, Google API key, and the location you want to bot in.
			- if you are using a gmail account, enter the info into the first block. For PTC, second block
			- for location, use GPS coordinates. Go to Google Maps and drop the arrow on your location for coords.
		7) Save config.json
		8) Go back to your terminal and navigate to the Pokebot folder
		9) Run the command “python pokebot.py -i 0” if your account is gmail. Run “python pokebot.py -i 1” if you have a PTC

	Windows
        1) Install the Visual C Compiler.
        2) Open Command Prompt
        3) Navigate to the Pokebot folder
        4) Run "pip install -r requirements.txt"5) Open config.json
        6) Enter your username, password, Google API key, and the location you want to bot in.
            - if you are using a gmail account, enter the info into the first block. For PTC, second block
            - for location, use GPS coordinates. Go to Google Maps and drop the arrow on your location for coords.
        7) Save config.json
        8) Go back to command prompt and run the command “python pokebot.py -i 0” if your account is gmail. Run “python pokebot.py -i 1” if you have a PTC
		

If anything doesn’t work, email me at anshmathur00@gmail.com

TODO
	Better transferring
	Maybe replace the heartbeat API with something faster