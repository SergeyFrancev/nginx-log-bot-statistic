# Nginx Log Bot Statistic

**Nginx Log Bot Statistic** is a Python command-line utility for analyzing Nginx server `access.log` files. This application allows you to obtain statistics on requests from web crawlers within these log files.

This solution is based on [robot_detector](https://github.com/amandasaurus/robot-detection) using the browser User-Agent Header .

## Features

- Analyze Nginx `access.log` files to identify requests from web crawlers.
- Get list web crawlers.
- Get count request from web crawlers.
- Сan analyze both a single file, `access.log`, and files in the directory that resemble `access.log.[N]`.
- Simple and intuitive command-line interface.

## Installation

1. Clone the repository from GitHub:
    ```shell
    git clone https://github.com/SergeyFrancev/nginx-log-bot-statistic
    ```
2. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```

## Usage
### Base Example
```
python bot_stat.py [command:stat|bot_list] [path_to_files|path_to_files_dir]
```
### Count request from bots
```
python3 bot_stat.py stat /path/to/access.log
```
Output:
> ```
Stat:
>* Read lines: 201691
>- Count requests from users: 105609
>- Count requests from bots: 96082

### Get list uniques bot UserAgents
```
python bot_stat.py bot_list /path/to/dir_with_log_files/
```
Output:
>```
>python-requests/2.31.0
>Mozilla/5.0 (compatible; BLEXBot/1.0; +[link])
>...
>```
