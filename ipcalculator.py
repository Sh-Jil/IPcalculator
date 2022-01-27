
def binary(ipnew):
    binary = ""
    for i in ipnew:
        bi = str(bin(i))[2:].zfill(8)
        binary += bi+"."
    return all_bin(binary[:-1])
    
def all_bin(binary):
    return "".join(binary.split("."))
    
def bin_dec(binary):
    es = [str(binary[i:i + 8]) for i in range(0, len(binary), 8)]
    return ".".join([str(int(i,2)) for i in es])

def netadd(binary,mask):
    a = 32-mask
    return bin_dec(binary) if mask==32 else bin_dec(str(binary[:-a])+str(binary[-a:]).replace('1','0'))

def subnet(binary,mask):
    a = 32-mask
    return bin_dec(str(binary[:-a]).replace('0','1')+str(binary[-a:]).replace('1','0'))

def wildcard(binary,mask):
    a = 32-mask
    return bin_dec(str(binary[:-a]).replace('1','0')+str(binary[-a:]).replace('0','1'))

def broadd(binary,mask):
    a = 32-mask
    return bin_dec(binary) if mask==32 else bin_dec(str(binary[:-a])+str(binary[-a:]).replace('0','1'))

def hostmax(binary,mask):
    a = 32-mask
    return bin_dec(binary) if mask==32 else bin_dec(str(binary[:-a])+str((binary[-a:]).replace('1','0')).replace('0','1',a-1))

def hostmin(binary,mask):
    a = 32-mask
    return bin_dec(binary) if mask==32 else bin_dec(str(binary[:-a])+str(binary[-a:]).replace('1','0')[:-1]+str(1))

def nohost(mask):
    a = 32-mask
    return 1 if mask==32 else pow(2,a)-2


ip,mask = input("ip:").split("/")
mask = int(mask)
ipnew = [int(i) for i in ip.split(".")]
print("ip address:",ip)
binary = binary(ipnew)
print("network:",netadd(binary,mask))
print("Subnet:",subnet(binary,mask))
print("wildcard:",wildcard(binary,mask))
print("\n")
print("Broadcast:",broadd(binary,mask))
print("Hostmin",hostmin(binary,mask))
print("Hostmax",hostmax(binary,mask))
print("No of hosts Available:",nohost(mask))