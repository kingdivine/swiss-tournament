# Tournament Results
Swiss style tournament created using PostgreSQL and Python.

### Requirements
- [PostgreSQL](https://www.postgresql.org/download/)
- [Python 2.7](https://www.python.org/downloads/)
- [Virtual Box](https://www.virtualbox.org/wiki/Downloads)
- [Vagrant](https://www.vagrantup.com/downloads.html)


### Files
- `tournament.sql` creates the database plus its tables and views.
- `tournament.py` contains the functions within which SQL queries are defined.
- `tournament_test.py` runs the code in `tournament.py` to test functionality. 

### Usage
- Clone [this repository](https://github.com/kingdivine/swiss-tournament.git)
- On your terminal, navigate to the tournament folder containing the project files and type `vagrant up` to turn on the virtual machine followed by `vagrant ssh` to log in.  
- Create the database by running the command `psql \i tournament.sql`.
- After this you can exit psql by typing `\q`.
- Run the `tournament_test.py` file by typing `python tournament_test.py`.  You should now see the outcome of all the code written. 
- Make changes to any of the files to add more functionality/ extra features to the software. 


### License
MIT License

