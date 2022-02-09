class Ipcalc():
    
    def __init__(self,ip,mask):
        self.mask = int(mask)
        ipnew = [int(i) for i in ip.split(".")]
        print("ip address:",ip)
        self.bin = Ipcalc.binary(ipnew)
        print("network:",Ipcalc.netadd(self))
        print("Subnet:",Ipcalc.subnet(self))
        print("wildcard:",Ipcalc.wildcard(self))
        print("\n")
        print("Broadcast:",Ipcalc.broadd(self))
        print("Hostmin",Ipcalc.hostmin(self))
        print("Hostmax",Ipcalc.hostmax(self))
        print("No of hosts Available:",Ipcalc.nohost(self))

    def binary(self):
        binary = ""
        for i in self:
            bi = str(bin(i))[2:].zfill(8)
            binary += bi+"."
        return Ipcalc.all_bin(binary[:-1])
        
    def all_bin(self):
        return "".join(self.split("."))
        
    def bin_dec(self):
        es = [str(self[i:i + 8]) for i in range(0, len(self), 8)]
        return ".".join([str(int(i,2)) for i in es])

    def netadd(self):
        a = 32-self.mask
        return Ipcalc.bin_dec(self.bin) if self.mask==32 else Ipcalc.bin_dec(str(self.bin[:-a])+str(self.bin[-a:]).replace('1','0'))

    def subnet(self):
        a = 32-self.mask
        return Ipcalc.bin_dec(str(self.bin[:-a]).replace('0','1')+str(self.bin[-a:]).replace('1','0'))

    def wildcard(self):
        a = 32-self.mask
        return Ipcalc.bin_dec(str(self.bin[:-a]).replace('1','0')+str(self.bin[-a:]).replace('0','1'))

    def broadd(self):
        a = 32-self.mask
        return Ipcalc.bin_dec(self.bin) if self.mask==32 else self.bin_dec(str(self.bin[:-a])+str(self.bin[-a:]).replace('0','1'))

    def hostmax(self):
        a = 32-self.mask
        return Ipcalc.bin_dec(self.bin) if self.mask==32 else self.bin_dec(str(self.bin[:-a])+str((self.bin[-a:]).replace('1','0')).replace('0','1',a-1))

    def hostmin(self):
        a = 32-self.mask
        return Ipcalc.bin_dec(self.bin) if self.mask==32 else self.bin_dec(str(self.bin[:-a])+str(self.bin[-a:]).replace('1','0')[:-1]+str(1))

    def nohost(self):
        a = 32-self.mask
        return 1 if self.mask==32 else pow(2,a)-2


ip,mask = input("ip:").split("/")
Ipcalc(ip,mask)
