{\rtf1\ansi\ansicpg1252\cocoartf1561\cocoasubrtf610
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
{\*\listtable{\list\listtemplateid1\listhybrid{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{disc\}}{\leveltext\leveltemplateid1\'01\uc0\u8226 ;}{\levelnumbers;}\fi-360\li720\lin720 }{\listname ;}\listid1}}
{\*\listoverridetable{\listoverride\listid1\listoverridecount0\ls1}}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 Movies Games Web App\
\
I\'92m using The Movie DB to source my data because it is robust, breaks down their data into manageable APIs and there is no limit on the API requests I can make. \
\
I\'92ve created a pipeline to fill a MySQL database from TMDB through a series of API requests. I make an api request on an actor\'92s name and take the response to get their actor id number. I then make another API request to get all of the movies they are in. In a Jupiter notebook, I clean the data by adding \'93actor name\'94 and \'93actor id number\'94 columns to the movies table as well as pull out the genres from the list and create a second genre table. I insert these data frames directly into the mysql database that I have created for this project. I am currently filling the database and will refine my method so I can do the entire thing in one python program. \
\
Next, I would like to create a movies game app that can have some interactive games where users are presented with two actors to guess which one has been first billed in more movies. At this point, I think I will use Flask and Bootstrap as Frameworks and will be supported by MySQL.\
\
Future steps would include:\
\pard\tx220\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\li720\fi-720\pardirnatural\partightenfactor0
\ls1\ilvl0\cf0 {\listtext	\uc0\u8226 	}Expanding to have users log in and keep track of wins and losses\
{\listtext	\uc0\u8226 	}Add additional games including games where users guess who has been in more movies, how many movies have two actors been in, and whats an actor\'92s most popular genre. \
{\listtext	\uc0\u8226 	}Develop a pipeline for updating the database with new releases\
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0
\cf0 \
}