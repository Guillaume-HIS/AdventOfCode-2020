with open("input.txt", "r") as file:
    rules0, messages = file.read().split("\n\n")
    rules0 = rules0.splitlines()
    messages = messages.splitlines()


def make_rules(raw):
    rules_final = {}

    for rule in raw:
        k, v = rule.split(": ")

        # Si v est une lettre
        if v[0] == '"':
            rules_final[int(k)] = v[1:-1]

        else:
            vals = v.split(" | ")
            tmp = []
            for val in vals:
                tmp.append([int(k) for k in val.split()])
            rules_final[int(k)] = tmp

    return rules_final


def is_ok(msg, rule):

    if len(rule) > len(msg):
        return False

    elif len(rule) == 0 or len(msg) == 0:
        return len(rule) == 0 and len(msg) == 0

    rule_last = rule.pop()

    if isinstance(rule_last, str):
        if msg[0] == rule_last:
            return is_ok(msg[1:], rule.copy())

    else:
        for r in rules[rule_last]:
            if is_ok(msg, rule + list(reversed(r))):
                return True

    return False


def cnt_correct(msgs, rules):
    cnt = 0
    for msg in msgs:
        if is_ok(msg, list(reversed(rules[0][0]))):
            cnt += 1
    return cnt


rules = make_rules(rules0)


print("Q1 : ", cnt_correct(messages, rules))
rules[8] = [[42], [42, 8]]
rules[11] = [[42, 31], [42, 11, 31]]
print("Q2 : ", cnt_correct(messages, rules))
