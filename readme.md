### CLI based task manager tool

This is the simple CLI tool can be helpful in increasing your productivity. More like your todolist.
It uses `Postgresql` as database.


### How to use

```bash
usage: task [-h] [--mark] [--add-task] [--fetch-all] [--fetch-com] [--fetch-incom]

Command line task tracker

options:
  -h, --help         show this help message and exit
  --mark , -M        Mark you task complete , pass task id
  --add-task, -T     Add some other task
  --fetch-all, -A    Get all of your tasks
  --fetch-com, -C    Get list of completed tasks
  --fetch-incom, -I  Get list of completed tasks

```

- Added your database name and user name in `.env` file
- Example

```shell
database=db_name
username=usr_name
```
- just run `./setup.sh`

That's it now add your new task using 

```shell
$ task -T
```

### Features
- Support of database
- Easy to use
- Easy to setup 
- No support for Billy G ( except WSL ) Lol


### Prerequisites

- Make sure you have install Postgresql in your system
- 

