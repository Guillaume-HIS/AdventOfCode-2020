from copy import deepcopy

with open("input.txt", "r") as file:
    data = file.read().splitlines()
    lines = [line.split(" = ") for line in data]
    lines.append(["mask", "0"])


blocks = []
tmp = []
for elem in lines:
    if elem[0] == "mask":
        blocks.append(tmp)
        tmp = [elem]
    else:
        tmp.append(elem)
blocks.remove([])

commands = []
for block in blocks:
    dic = {}
    dic["mask"] = block[0][1]
    for k in range(1, len(block)):
        dic[int(block[k][0][3:].replace("[", "").replace("]", ""))] = []
    for k in range(1, len(block)):
        dic[int(block[k][0][3:].replace("[", "").replace("]", ""))].append(int(block[k][1]))
    commands.append(dic)


def q1(commands):
    comms = deepcopy(commands)
    memory = {}
    for blck in comms:
        msk = ""
        for key, value in blck.items():
            if key == "mask":
                msk = value
                continue
            else:
                for t in range(len(value)):
                    new_val = ""
                    for index, char in enumerate('{0:036b}'.format(value[t])):
                        if msk[index] == "X":
                            new_val += char
                        else:
                            new_val += msk[index]
                    value[t] = new_val

    for blck2 in comms:
        for key, value in blck2.items():
            if key == "mask":
                continue
            else:
                for added in value:
                    memory[key] = int(added, 2)

    return memory, sum(memory.values())


def q2(data):
    memory = {}
    msk = ""
    addr = ""
    value = ""
    for line in data:
        if line.split(" = ")[0] == "mask":
            msk = line.split(" = ")[1]
        else:
            addr = '{0:036b}'.format(int(line.split(" = ")[0].replace("mem[", "").replace("]", "")))
            val = int(line.split(" = ")[1])

            # Appli masque en laissant X
            modified_val = ""
            for i, char in enumerate(msk):
                if char == "1":
                    modified_val += "1"
                elif char == "X":
                    modified_val += "X"
                else:
                    modified_val += addr[i]

            # List avec toutes adresses
            addr_floats = [""]
            for i, bit in enumerate(modified_val):
                if bit != "X":
                    for k in range(len(addr_floats)):
                        addr_floats[k] += bit
                else:
                    tmp = []
                    for value in addr_floats:
                        tmp.append(value + "0")
                        tmp.append(value + "1")
                    addr_floats = tmp

            for address in addr_floats:
                memory[int(address, 2)] = val



    return memory, sum(memory.values())


# print(q1(commands)[0])
# print(q1(commands)[1])
print(q2(data)[1])
