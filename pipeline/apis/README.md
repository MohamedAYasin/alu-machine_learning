![dany](https://github.com/user-attachments/assets/14386cdd-57c1-4552-b860-8f79367afd08)

# Resources
## Read or watch:

[Requests package](https://docs.python-requests.org/en/latest/)

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General

- How to use the Python package requests
- How to make HTTP GET request
- How to handle rate limit
- How to handle pagination
- How to fetch JSON resources
- How to manipulate data from an external service

## Tasks

`0. Can I join?`

mandatory
Score: 100.0% (Checks completed: 100.0%)

By using the `Swapi API,` create a method that returns the list of ships that can hold a given number of passengers:

- Prototype: def availableShips(passengerCount):
- Don’t forget the pagination
- If no ship available, return an empty list.
  
`bob@dylan:~$ cat 0-main.py
#!/usr/bin/env python3
"""
Test file
"""
availableShips = __import__('0-passengers').availableShips
ships = availableShips(4)
for ship in ships:
    print(ship)

bob@dylan:~$ ./0-main.py
CR90 corvette
Sentinel-class landing craft
Death Star
Millennium Falcon
Executor
Rebel transport
Slave 1
Imperial shuttle
EF76 Nebulon-B escort frigate
Calamari Cruiser
Republic Cruiser
Droid control ship
Scimitar
J-type diplomatic barge
AA-9 Coruscant freighter
Republic Assault ship
Solar Sailer
Trade Federation cruiser
Theta-class T-2c shuttle
Republic attack cruiser
bob@dylan:~$
Repo:`

- GitHub repository: `alu-machine_learning`
- Directory: `pipeline/apis`
- File: `0-passengers.py`
 
5/5 pts
1. Where I am?
mandatory
Score: 100.0% (Checks completed: 100.0%)
By using the Swapi API, create a method that returns the list of names of the home planets of all sentient species.

Prototype: def sentientPlanets():
Don’t forget the pagination
bob@dylan:~$ cat 1-main.py
#!/usr/bin/env python3
"""
Test file
"""
sentientPlanets = __import__('1-sentience').sentientPlanets
planets = sentientPlanets()
for planet in planets:
    print(planet)

bob@dylan:~$ ./1-main.py
Endor
Naboo
Coruscant
Kamino
Geonosis
Utapau
Kashyyyk
Cato Neimoidia
Rodia
Nal Hutta
unknown
Trandosha
Mon Cala
Sullust
Toydaria
Malastare
Ryloth
Aleen Minor
Vulpter
Troiken
Tund
Cerea
Glee Anselm
Iridonia
Tholoth
Iktotch
Quermia
Dorin
Champala
Mirial
Zolan
Ojom
Skako
Muunilinst
Shili
Kalee
bob@dylan:~$
Repo:

GitHub repository: alu-machine_learning
Directory: pipeline/apis
File: 1-sentience.py
 
4/4 pts
2. Rate me is you can!
mandatory
Score: 100.0% (Checks completed: 100.0%)
By using the GitHub API, write a script that prints the location of a specific user:

The user is passed as first argument of the script with the full API URL, example: ./2-user_location.py https://api.github.com/users/holbertonschool
If the user doesn’t exist, print Not found
If the status code is 403, print Reset in X min where X is the number of minutes from now and the value of X-Ratelimit-Reset
Your code should not be executed when the file is imported (you should use if __name__ == '__main__':)
bob@dylan:~$ ./2-user_location.py https://api.github.com/users/holbertonschool
San Francisco, CA
bob@dylan:~$
bob@dylan:~$ ./2-user_location.py https://api.github.com/users/holberton_ho_no
Not found
bob@dylan:~$
... after a lot of request... 60 exactly...
bob@dylan:~$
bob@dylan:~$ ./2-user_location.py https://api.github.com/users/holbertonschool
Reset in 16 min
bob@dylan:~$ 
Tips: Playing with an API that has a Rate limit is challenging, mainly because you don’t have the control on when the quota will be reset - we really encourage you to analyze the API a much as you can before coding and be able to “mock the API response”

Repo:

GitHub repository: alu-machine_learning
Directory: pipeline/apis
File: 2-user_location.py
 
6/6 pts
3. What will be next?
mandatory
Score: 100.0% (Checks completed: 100.0%)
By using the (unofficial) SpaceX API, write a script that displays the upcoming launch with these information:

Name of the launch
The date (in local time)
The rocket name
The name (with the locality) of the launchpad
Format: <launch name> (<date>) <rocket name> - <launchpad name> (<launchpad locality>)

The “upcoming launch” is the one which is the soonest from now, in UTC (we encourage you to use the date_unix for sorting it) - and if 2 launches have the same date, use the first one in the API result.

Your code should not be executed when the file is imported (you should use if __name__ == '__main__':)

bob@dylan:~$ ./3-upcoming.py 
O3b mPower 1,2 (2022-06-30T20:00:00-04:00) Falcon 9 - CCSFS SLC 40 (Cape Canaveral)
bob@dylan:~$ 
Repo:

GitHub repository: alu-machine_learning
Directory: pipeline/apis
File: 3-upcoming.py
 
4/4 pts
4. How many by rocket?
mandatory
Score: 100.0% (Checks completed: 100.0%)
By using the (unofficial) SpaceX API, write a script that displays the number of launches per rocket.

All launches should be taking in consideration
Each line should contain the rocket name and the number of launches separated by : (format below in the example)
Order the result by the number launches (descending)
If multiple rockets have the same amount of launches, order them by alphabetic order (A to Z)
Your code should not be executed when the file is imported (you should use if __name__ == '__main__':)
bob@dylan:~$ ./4-rocket_frequency.py
Falcon 9: 104
Falcon 1: 5
Falcon Heavy: 3
bob@dylan:~$ 
Repo:

GitHub repository: alu-machine_learning
Directory: pipeline/apis
File: 4-rocket_frequency.py


©2024 `African Leadership University`
