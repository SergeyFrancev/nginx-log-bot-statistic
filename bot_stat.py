import os
import re
import sys
import typing as t
import robot_detection.robot_detection as rd


AGENT_REGEXP = re.compile(r".*\".*\".*\".*\".*\"(.*)\".*\".*\"")


def get_files(path_to_file: str) -> t.List[str]:
    if os.path.isdir(path_to_file):
        files = os.listdir(path_to_file)
        out = [os.path.join(path_to_file, f) for f in files if f.startswith('access.log')]
        assert len(out) > 0, 'Directory not contains any "access.log" files'
    else:
        out = [path_to_file]

    return out


def is_bot(agent: str) -> bool:
    return rd.is_robot(agent)
    

def lines_from_path(path_to_dir):
    for path_to_file in get_files(path_to_dir):
        with open(path_to_file, 'r', encoding='UTF-8') as file:
            while line := file.readline():
                yield line


def parse_agent(log_line: str) -> t.Optional[str]:
    # res = re.search(r".*\".*\".*\".*\".*\"(.*)\".*\".*\"", log_line)
    res = AGENT_REGEXP.search(log_line)
    if not res or len(res.groups()) < 1:
        return None
    return res.group(1)


def analyze_line_on_bot_agent(log_line: str) -> t.Optional[t.Tuple[str, bool]]:
    try:
        agent = parse_agent(log_line)
        if agent == "":
            return agent, True
        return agent, is_bot(agent)
    except ValueError:
        print('Incorrect agent name line:', log_line)
        print('Incorrect agent name:', agent)
        return agent, True
    return None


def print_stat(path_to_fails: str):
    count_lines = 0
    count_bots = 0
    count_users = 0
    for log_line in lines_from_path(path_to_fails):
        count_lines += 1
        agent, is_bot = analyze_line_on_bot_agent(log_line)
        if not agent:
            continue
        if is_bot:
            count_bots += 1
        else:
            count_users += 1

    print('Stat:')
    print('* Read lines:', count_lines)
    print('- Count requests from users:', count_users)
    print('- Count requests from bots:', count_bots)


def print_bot_list(path_to_file: str):
    bots = set()
    for log_line in lines_from_path(path_to_file):
        agent, is_bot = analyze_line_on_bot_agent(log_line)
        if not is_bot:
            continue
        bots.add(agent)

    for b in bots:
        print(b)


def print_agents_by_rule(path_to_file: str, rule: str):
    print(f'Start check_rule [{rule}] in: ', path_to_file)
    bots = set()
    reg = re.compile(rule)
    count_lines = 0
    for log_line in lines_from_path(path_to_file):
        count_lines += 1
        agent = parse_agent(log_line)
        if agent and reg.search(agent.lower()):
            bots.add(agent)
    
    print('* Read lines: ', count_lines)

    if len(bots) == 0:
        print('No bots by this rule')
    for b in bots:
        print(b)


if __name__ == '__main__' and len(sys.argv) > 2:
    command = sys.argv[1]
    path_to_dir = sys.argv[2]
    print('len', len(sys.argv))

    if command == 'stat' and len(sys.argv) == 3:
        print_stat(path_to_dir)
    elif command == 'bot_list' and len(sys.argv) == 3:
        print_bot_list(path_to_dir)
    elif command == 'grep_by_rule' and len(sys.argv) == 4:
        rule = sys.argv[3]
        print_agents_by_rule(path_to_dir, rule)
    else:
        print(f'Incorrect command "{command}"')
