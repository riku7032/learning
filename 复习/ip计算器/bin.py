from ipaddress import ip_address
import copy

ip_address = input("请输入IP地址:")
netmask = input("请输入子网掩码:")




def mask2bin(a):
    """
    将网络号转成子网掩码
    例如24-> 255.255.255.0
    """
    string = []
    temp_str = ""
    temp = []
    for i in range(0, int(a)):
        # 根据输入的网络后，往数据组添加1
        string.append("1")
    if len(string) < 32:
        # 如果不满32位，则用0补足
        for x in range(0, 32-len(string)):
            string.append("0")
    for y in range(0, len(string)):
        # 根据string的长度，按8位切割成4份，用'.'来切割
        if y != 0 and y % 8 == 0:
            temp_str += "."
        temp_str += string[y]
    # 将4份字符串按.装进数组
    temp = temp_str.split(".")
    test = ".".join([str(i) for i in [int(i,2) for i in temp]])
    # 第一个推导是将“11111111”转成二进制，第二个推导式将int的255转成字符串
    return test


def number2bin(a, b):
    """
    将给定的ip地址和子网掩码按位与运算，求出网络段。
    例如
    ip_address = "192.168.1.182"
    netmask = "255.255.255.192"
    求得：
    192.168.1.128/26
    """
    # 将给的ip字符串切成4份字符串并转成数字型数组
    ip = [int(i) for i in a.split(".")]
    # 将给的子网掩码切成4份字符串并转成数字型数组
    netmask = [int(i) for i in b.split(".")]
    network = []
    for n in range(0, len(ip)):
        #将2个数组的每个值互相按位与运算，并将结果推进network数组
        network.append(ip[n] & netmask[n])
    # 将每个数字型结果转成字符串型，并合并成一个字符串。并返回该结构
    return ".".join([str(i) for i in network])


def hostNumber(a):
    """
    根据子网掩码计算主机数
    """
    string = []
    temp_str = ""
    temp = []
    number = 0
    for i in range(0, int(a)):
        # 根据输入的网络后，往数据组添加1
        string.append("1")
    if len(string) < 32:
        # 如果不满32位，则用0补足
        for x in range(0, 32-len(string)):
            string.append("0")
    for y in range(0, len(string)):
        # 根据string的长度，按8位切割成4份，用'.'来切割，并将其组成一个字符串
        if y != 0 and y % 8 == 0:
            temp_str += "."
        temp_str += string[y]
        # 对字符串进行反转，并数出有几个连续的0。
    for i in temp_str[::-1].replace(".",""):
        if i == "0":
            number += 1
        else:
            break
    # 计算主机数
    host = 2 ** number -2
    return host

def compareRange(netWork,hosts):
    """
    传入2个参数：
    1. 计算得出的网络号
    2. hosts数
    
    输出一个数组：
    ["ip段的第一个ip地址"，"ip段的最后一个ip地址"]
    
    比较逻辑:
    ip段的第一个地址应根据网络号选，例如：
    network: 192.168.2.0/23
    Start range: 192.168.2.1
    End range: 192.168.3.254
    Hosts： 510
    """
    outList = []
    # 将输入的网络号转成int数组
    calNetwork = [int(i) for i in netWork.split(".")]
    startRange = copy.copy(calNetwork) 
    endRange = copy.copy(calNetwork) 
    if hosts > 254:
        startRange[3] = calNetwork[3]+1
        endRange[2]= calNetwork[2]+hosts // 255 -1
        endRange[3]= calNetwork[3] + 254
    else:
        startRange[3] = calNetwork[3]+1
        endRange[3]= calNetwork[3] + hosts
    outList = [".".join([str(i) for i in startRange]),".".join([str(i) for i in endRange])]
    return outList

network = number2bin(ip_address, mask2bin(netmask)) 
string = network + "/" + netmask
hosts = hostNumber(netmask)

outlist = compareRange(network,hosts)

print(
    f"\nAddress: {ip_address} \
    \nNetmask: {mask2bin(netmask)} \
    \nNetwork: {string} \
    \nhosts: {hostNumber(netmask)}\
    \nStart range: {outlist[0]} \
    \nEnd range: {outlist[1]} \n \
    ")