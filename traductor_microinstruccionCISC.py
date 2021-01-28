import mif
import csv
import numpy as np

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

errors = []
mif_array = [0]*4096 

def print_errors():
    global errors
    for error in errors:
        print("salida:\033[93m{}\033[0m no valida, Direccion \033[93m0x{}\033[0m".format(error["salida"],error["dir"]))

def write_data(mif_file, mifdata):
    
    with open(mif_file,"w+") as f:
        mif.dump(mifdata,f)
    return mifdata

def get_data(mif_file):
    with open(mif_file) as f:
        mem = mif.load(f)
    return mem

def asm_default():
    instruction = {
        "nCRI":1,
        "EB1":0,
        "EB0":0,
        "nWB":1,
        "EA1":0,
        "EA0":0,
        "nWA":1,
        "selbus":0,
        "UPA9":0,
        "UPA8":0,
        "UPA7":0,
        "UPA6":0,
        "UPA5":0,
        "UPA4":0,
        "UPA3":0,
        "UPA2":0,
        "UPA1":0,
        "UPA0":0,
        "nOEUPA":1,
        "nDUPA":1,
        "selmux":0,
        "nEX2":1,
        "nEX1":1,
        "nEX0":1,
        "X2":0,
        "X1":0,
        "X0":0,
        "EnaY":0,
        "nERA2":1,
        "nERA1":1,	
        "nERA0":1,
        "RA2":0,
        "RA1":0,
        "RA0":0,
        "nEAP2":1,
        "nEAP1":1,
        "nEAP0":1,
        "AP2":0,
        "AP1":0,
        "AP0":0,
        "nEPC2":1,
        "nEPC1":1,
        "nEPC0":1,
        "PC2":0,
        "PC1":0,
        "PC0":0,
        "nCBD":1,	
        "nAS":1,
        "nRW":1,
        "BD":0,
        "DINT":0,	
        "HINT":0,	
        "SET_IRQ":0,
        "SET_XIRQ":0,
        "B9":0,
        "B8":0,
        "B7":0,
        "B6":0,	
        "B5":0,	
        "B4":0,	
        "B3":0,	
        "B2":0,	
        "B1":0,	
        "B0":0,	
        "CC":0,	
        "CN":0,	
        "CV":0,	
        "CZ":0,	
        "CI":0,
        "CH":0,	
        "CX":0,	
        "CS":0,	
        "nHB":1,
        "ACCSEC":0
    }
    return instruction

def get_new_asm_struct():
    asm_struct = {
    "Q3":[],
    "Q2":[],
    "Q1":[],
    "Q0":[],
    "P4":[],
    "P3":[],
    "P2":[],
    "P1":[],
    "P0":[],
    "VF":[],
    "I1":[],
    "I0":[],
    "L11":[],
    "L10":[],
    "L9":[],
    "L8":[],
    "L7":[],
    "L6":[],
    "L5":[],
    "L4":[],
    "L3":[],
    "L2":[],
    "L1":[],
    "L0":[],
    "nCRI":[],
    "EB1":[],
    "EB0":[],
    "nWB":[],
    "EA1":[],
    "EA0":[],
    "nWA":[],
    "selbus":[],
    "UPA9":[],
    "UPA8":[],
    "UPA7":[],
    "UPA6":[],
    "UPA5":[],
    "UPA4":[],
    "UPA3":[],
    "UPA2":[],
    "UPA1":[],
    "UPA0":[],
    "nOEUPA":[],
    "nDUPA":[],
    "selmux":[],
    "nEX2":[],
    "nEX1":[],
    "nEX0":[],
    "X2":[],
    "X1":[],
    "X0":[],
    "EnaY":[],
    "nERA2":[],
    "nERA1":[],	
    "nERA0":[],
    "RA2":[],
    "RA1":[],
    "RA0":[],
    "nEAP2":[],
    "nEAP1":[],
    "nEAP0":[],
    "AP2":[],
    "AP1":[],
    "AP0":[],
    "nEPC2":[],
    "nEPC1":[],
    "nEPC0":[],
    "PC2":[],
    "PC1":[],
    "PC0":[],
    "nCBD":[],	
    "nAS":[],
    "nRW":[],
    "BD":[],
    "DINT":[],	
    "HINT":[],	
    "SET_IRQ":[],
    "SET_XIRQ":[],
    "B9":[],
    "B8":[],
    "B7":[],
    "B6":[],	
    "B5":[],	
    "B4":[],	
    "B3":[],	
    "B2":[],	
    "B1":[],	
    "B0":[],	
    "CC":[],	
    "CN":[],	
    "CV":[],	
    "CZ":[],	
    "CI":[],
    "CH":[],	
    "CX":[],	
    "CS":[],	
    "nHB":[],
    "ACCSEC":[]
    }
    return asm_struct

def instruction_to_string(direccion = "000", prueba="00000", vf="0",inst="00",liga="000000000000", mutations = []):
    instruction = asm_default()
    salidas_x = list(instruction.keys())
    salidas = []
    global errors
    for salida in salidas_x:
        salidas.append(salida.lower())

    
    mutations_X = []
    for mut in mutations:
        if mut.lower() not in salidas:
            error = {
                "salida":mut.lower(), 
                "dir":direccion
            }
            errors.append(error)
            print("{} wooo".format(mut.lower()))
        else:
            mutations_X.append(mut.lower())
    mutations = mutations_X
    string_completa = ""
    for key in instruction:
        i = instruction[key]
        if key.lower() in mutations:
            i = int(not i)
        string_completa += str(i)
        #print(key, i)
    instruction = string_completa
    #direccion = "{0:X}".format(int(direccion,2))
    while len(direccion) < 3:
        direccion = "0{0}".format(direccion)
    payload = "{}{}{}{}{}".format(prueba,vf,inst,liga,instruction)
    print("======{}======".format(direccion))
    get_info_instruccion(payload)
    print("======{}======".format(direccion))
    codigo = "elsif(dir = X\"{}\") then data <= \"{}\";\n".format(direccion,payload)
    return codigo

def get_info_instruccion(inst):
    print("prueba: {0:X}".format(int(inst[:5],2)))
    print("vf: {}".format(inst[5]))
    print("ins:{}".format(inst[6:8]))
    print("liga: {0:X}".format(int(inst[8:20],2)))
    inst = inst[20:]
    default = asm_default()
    pos = 0
    for key in default:
        i = default[key]
        if int(inst[pos]) != int(i):
            print(key)
        pos += 1

def asm_list_to_csv(csv_file, lista_asm, asm_columns):
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=asm_columns)
            writer.writeheader()
            for data in lista_asm:
                writer.writerow(data)
    except IOError:
        print("I/O error")

def dec_to_dir_bin(dec, tam):
    strbin = "{0:b}".format(dec)
    listbin = []
    while len(strbin) < tam:
        strbin = "0{0}".format(strbin)
    for strr in strbin:
        listbin.append(strr)
    return strbin

def csv_to_mif(csv_file, mif_file):
    asm_lista_dicts = []
    with open(csv_file, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        line_count = 0
        for row in reader:
            if line_count == 0:
                asm_keys = row
            else:
                asm_struct_template = get_new_asm_struct()
                asm_data = row
                k = 0
                asm_data_string = ""
                for key in asm_keys:
                    asm_struct_template[key] = asm_data[k]
                    asm_data_string += asm_data[k]
                    k += 1
                asm_lista_dicts.append(asm_struct_template)
            line_count += 1

def instruction_to_string_eha(direccion="000", prueba="00",vf="0", inst="00", liga="000", mutations=[]):
    return instruction_to_string(direccion=direccion, 
        prueba=dec_to_dir_bin(int(prueba,16),5),
        vf=vf, 
        inst=inst,
        liga=dec_to_dir_bin(int(liga,16),12), 
        mutations=mutations)

def ram_to_string(pos='0', contenido='FF'):
    memoria_str = "mem({}) <= X\"{}\";\n".format(pos,contenido)
    return memoria_str


'''
if __name__ == "__main__":
    lista_asm = []
    mem = get_data("rom_content.mif")
    #print(mif.dumps(mem))
    print(mem[0x00][0])
    print(mem[0x00][1])
    print(mem[0x00][2])
    estructura_asm = get_new_asm_struct()
    asm_lista = list(estructura_asm.keys())
    asm_lista.reverse()
    direccion = 0
    for mdir in mem:
        c = 0
        estructura_asm = get_new_asm_struct()
        dirList = dec_to_dir_bin(direccion)
        dirList.reverse()
        for mdata in mdir:
            estructura_asm[asm_lista[c]] = mdata
            c += 1
        for dirData in dirList:
            try:
                estructura_asm[asm_lista[c]] = dirData
                c += 1
            except:
                pass
        new_dict={}
        for k,v in estructura_asm.items():
            dict_element={k:v}
            dict_element.update(new_dict)
            new_dict=dict_element
        lista_asm.append(new_dict)
        direccion += 1
    asm_lista.reverse()
    asm_list_to_csv("asm_.csv", lista_asm, asm_lista)
    csv_to_mif("asm_.csv", "rom.mif")
'''
'''
if __name__ == "__main__":

    i = asm_default()
    #instruction_to_string("000",dec_to_dir_bin(int("00",16),5),"0","00",dec_to_dir_bin(int("F08",16),12),[])
    mem = get_data("rom_content.mif")
    inicio = 0x260
    fin = 0x26B
    point = inicio
    for mdir in mem[inicio:fin+1]:
        ins = ""
        for dat in mdir.tolist():
            ins += str(dat)
        print("=========={0:X}============".format(point))
        get_info_instruccion(ins[::-1])
        print("========================")
        point += 1
'''

if __name__ == "__main__":

    get_info_instruccion("0000000000000000100010010010000000000011011100001110001110001110001110000000000000000000000010")

        #get_info_instruccion(i[:-1].replace(" ",""))

    mifInst = ""
    instrucciones = ""
    # LDAA(IMM)
    instrucciones += instruction_to_string_eha(direccion="860",prueba="00",vf="0",mutations=["nepc2","ncbd"])
    instrucciones += instruction_to_string_eha(direccion="861",prueba="00",vf="0",mutations=["nas","pc0","nwa","ea0"])
    instrucciones += instruction_to_string_eha(direccion="862",prueba="0f",vf="1",inst="11",mutations=["cz","cn","cv","b3","b6","b2"])
    instrucciones += instruction_to_string_eha(direccion="863",liga="09",prueba="18",vf="0",inst="01",mutations=["nepc2","ncbd"])
    # LDAB(IMM)
    instrucciones += instruction_to_string_eha(direccion="C60",prueba="00",vf="0",mutations=["nepc2","ncbd"])
    instrucciones += instruction_to_string_eha(direccion="C61",prueba="00",vf="0",mutations=["nas","pc0","nwa","ea0"])
    instrucciones += instruction_to_string_eha(direccion="C62",prueba="0f",vf="1",inst="11",mutations=["cz","cn","cv","b4","b7","b2"])
    instrucciones += instruction_to_string_eha(direccion="C63",liga="09",prueba="18",vf="0",inst="01",mutations=["nepc2","ncbd"])
    #LDX(IMM)
    instrucciones += instruction_to_string_eha(direccion="CE0",prueba="00",vf="0",mutations=['nEPC2','nCBD'])
    instrucciones += instruction_to_string_eha(direccion="CE1",prueba="00",vf="0",mutations=['nAS','X0','X1','nEX0','PC0'])
    instrucciones += instruction_to_string_eha(direccion="CE2",prueba="0f",vf="1",inst="11",mutations=['CZ','CN','CV','B4','B3','B6','B7','B2'])
    instrucciones += instruction_to_string_eha(direccion="CE3",liga="09",prueba="18",vf="0",inst="01" ,mutations=["nepc2","ncbd"])
    #XPAR(INH)
    instrucciones += instruction_to_string_eha(direccion="A50",prueba="00",vf="0",mutations=['nCBD','nEX2'])
    instrucciones += instruction_to_string_eha(direccion="A51",prueba="00",vf="0",mutations=['nAS','nERA0','RA0','RA1'])
    instrucciones += instruction_to_string_eha(direccion="A52",prueba="0f",vf="1",inst="11",mutations=['CC','B0','nERA0'])
    instrucciones += instruction_to_string_eha(direccion="A53",liga="09",prueba="18",vf="0",inst="01" ,mutations=["nepc2","ncbd"])
    # BRA
    instrucciones += instruction_to_string_eha(direccion="200",prueba="00",vf="0",mutations=["nhb","nera0","ra1","ra0","nepc2","ncbd"])
    instrucciones += instruction_to_string_eha(direccion="201",prueba="00",vf="0",mutations=["pc0","nas","upa2","upa1","upa0","upa5","upa4"])
    instrucciones += instruction_to_string_eha(direccion="202",prueba="00",vf="0",mutations=["nepc0","upa2","upa1","selmux","upa7"])
    instrucciones += instruction_to_string_eha(direccion="203",prueba="00",vf="1",inst="01", liga="208",mutations=["noeupa","ndupa","nepc0","pc1","pc0","cc"])
    instrucciones += instruction_to_string_eha(direccion="204",prueba="00",vf="0",mutations=["nepc1","selbus","upa7","upa2","upa1","upa0"])
    instrucciones += instruction_to_string_eha(direccion="205",prueba="00",vf="0",mutations=["pc2","noeupa","ndupa","nepc1"])
    instrucciones += instruction_to_string_eha(direccion="206",prueba="00",vf="0",mutations=["nera0","cc","b0","nhb"])
    instrucciones += instruction_to_string_eha(direccion="207",prueba="0f",vf="1",inst="11" ,mutations=["nepc2","ncbd"])
    instrucciones += instruction_to_string_eha(direccion="208",liga="09",prueba="08",vf="0",inst="01" ,mutations=["nepc1","upa7","upa5","upa2","upa1","upa0","selbus"])
    #BNE
    instrucciones += instruction_to_string_eha(direccion="260",prueba="12",vf="0",inst="01", liga="201",mutations=['nHB','nERA0','RA1','RA0','nEPC2','nCBD'])
    instrucciones += instruction_to_string_eha(direccion="261",prueba="0f",vf="1",inst="11" ,mutations=["pc0"])
    instrucciones += instruction_to_string_eha(direccion="262",liga="09",prueba="18",vf="0",inst="01" ,mutations=["nepc2","ncbd"])
    #BEQ
    instrucciones += instruction_to_string_eha(direccion="270",prueba="12",vf="1",inst="01", liga="201",mutations=['nHB','nERA0','RA1','RA0','nEPC2','nCBD'])
    instrucciones += instruction_to_string_eha(direccion="271",prueba="0f",vf="1",inst="11" ,mutations=["pc0"])
    instrucciones += instruction_to_string_eha(direccion="272",liga="09",prueba="18",vf="0",inst="01" ,mutations=["nepc2","ncbd"])
    #BHS
    instrucciones += instruction_to_string_eha(direccion="240",prueba="10",vf="0",inst="01", liga="201",mutations=['nHB','nERA0','RA1','RA0','nEPC2','nCBD'])
    instrucciones += instruction_to_string_eha(direccion="241",prueba="0f",vf="1",inst="11" ,mutations=["pc0"])
    instrucciones += instruction_to_string_eha(direccion="242",liga="09",prueba="18",vf="0",inst="01" ,mutations=["nepc2","ncbd"])
    #BCS - BLO
    instrucciones += instruction_to_string_eha(direccion="250",prueba="10",vf="1",inst="01", liga="201",mutations=['nHB','nERA0','RA1','RA0','nEPC2','nCBD'])
    instrucciones += instruction_to_string_eha(direccion="251",prueba="0f",vf="1",inst="11" ,mutations=["pc0"])
    instrucciones += instruction_to_string_eha(direccion="252",liga="09",prueba="18",vf="0",inst="01" ,mutations=["nepc2","ncbd"])
    #BMI
    instrucciones += instruction_to_string_eha(direccion="2B0",prueba="13",vf="1",inst="01", liga="201",mutations=['nHB','nERA0','RA1','RA0','nEPC2','nCBD'])
    instrucciones += instruction_to_string_eha(direccion="2B1",prueba="0f",vf="1",inst="11" ,mutations=["pc0"])
    instrucciones += instruction_to_string_eha(direccion="2B2",liga="09",prueba="18",vf="0",inst="01" ,mutations=["nepc2","ncbd"])
    #BPL
    instrucciones += instruction_to_string_eha(direccion="2A0",prueba="13",vf="0",inst="01", liga="201",mutations=['nHB','nERA0','RA1','RA0','nEPC2','nCBD'])
    instrucciones += instruction_to_string_eha(direccion="2A1",prueba="0f",vf="1",inst="11" ,mutations=["pc0"])
    instrucciones += instruction_to_string_eha(direccion="2A2",liga="09",prueba="18",vf="0",inst="01" ,mutations=["nepc2","ncbd"])
    #ADDA
    instrucciones += instruction_to_string_eha(direccion="db0",prueba="00",vf="0",mutations=['nEPC2','nCBD'])
    instrucciones += instruction_to_string_eha(direccion="db1",prueba="00",vf="0",mutations=['RA1','RA0','PC0','nAS','nERA0'])
    instrucciones += instruction_to_string_eha(direccion="db2",prueba="00",vf="0",mutations=['nERA2','nCBD'])
    instrucciones += instruction_to_string_eha(direccion="db3",prueba="00",vf="0",mutations=['nAS','EA1','EA0','UPA7','UPA2','UPA0','SELMUX','ACCSEC'])
    instrucciones += instruction_to_string_eha(direccion="db4",prueba="0f",vf="1",inst="11",mutations=['NOEUPA','NDUPA','NWA','EA0','CN','CZ','CV','CC'])
    instrucciones += instruction_to_string_eha(direccion="db5",liga="09",prueba="18",vf="0",inst="01" ,mutations=["nepc2","ncbd"])
    #CPX(imm)
    instrucciones += instruction_to_string_eha(direccion="8C0",prueba="00",vf="0",mutations=['nEPC2','nCBD'])
    instrucciones += instruction_to_string_eha(direccion="8C1",prueba="00",vf="0",mutations=['nAS','PC0','RA1','RA0','nERA0'])
    instrucciones += instruction_to_string_eha(direccion="8C2",prueba="00",vf="0",mutations=['UPA2','UPA1','UPA0','UPA5','UPA4','nERA0'])
    instrucciones += instruction_to_string_eha(direccion="8C3",prueba="00",vf="0",mutations=['nEX0','UPA2','UPA1','UPA4','SELMUX','CN','CZ','CV','CC'])
    instrucciones += instruction_to_string_eha(direccion="8C3",prueba="0f",vf="1",inst="11",mutations=['nEX0','UPA2','UPA1','UPA4','SELMUX','CN','CZ','CV','CC'])
    instrucciones += instruction_to_string_eha(direccion="8C4",liga="09",prueba="18",vf="0",inst="01" ,mutations=["nepc2","ncbd"])
    #INX
    instrucciones += instruction_to_string_eha(direccion="080",prueba="00",vf="0",mutations=['X0'])
    instrucciones += instruction_to_string_eha(direccion="081",prueba="0f",vf="1",inst="11",mutations=['CZ','B4','B3'])
    instrucciones += instruction_to_string_eha(direccion="082",liga="09",prueba="18",vf="0",inst="01" ,mutations=["nepc2","ncbd"])
    #XABA
    instrucciones += instruction_to_string_eha(direccion="AD0",prueba="00",vf="0",inst="00", liga="201",mutations=['EA1','EA0','EB1','EB0','UPA0','Selmux','UPA7'])
    instrucciones += instruction_to_string_eha(direccion="AD1",prueba="0f",vf="1",inst="11" ,mutations=['nOEUPA','nDUPA','nEX0','X1','X0','CN','CZ','CV','CC'])
    instrucciones += instruction_to_string_eha(direccion="AD2",liga="09",prueba="18",vf="0",inst="01" ,mutations=["nepc2","ncbd"])
    #JMP
    instrucciones += instruction_to_string_eha(direccion="7E0",prueba="00",vf="0",mutations=['nEPC2','nCBD'])
    instrucciones += instruction_to_string_eha(direccion="7E1",prueba="00",vf="0",mutations=['nAS','nERA1','RA2','BD','PC0'])
    instrucciones += instruction_to_string_eha(direccion="7E2",prueba="00",vf="0",mutations=['nEPC2','nCBD'])
    instrucciones += instruction_to_string_eha(direccion="7E3",prueba="00",vf="0",mutations=['nAS','RA1','RA0','nERA0'])
    instrucciones += instruction_to_string_eha(direccion="7E4",prueba="00",vf="0",mutations=['nERA0','nERA1','nEPC0','nEPC1','PC2','PC0'])
    instrucciones += instruction_to_string_eha(direccion="7E5",prueba="0f",vf="1",inst="11" ,mutations=[])
    instrucciones += instruction_to_string_eha(direccion="7E6",liga="09",prueba="18",vf="0",inst="01" ,mutations=["nEPC2","nCBD"])
    #SUBB(ind,x)
    instrucciones += instruction_to_string_eha(direccion="e00",prueba="00",vf="0",mutations=['nEPC2','nCBD'])
    instrucciones += instruction_to_string_eha(direccion="e01",prueba="00",vf="0",mutations=['nAS','PC0','UPA2','UPA1','UPA0','UPA5','UPA4'])
    instrucciones += instruction_to_string_eha(direccion="e02",prueba="00",vf="0",mutations=['UPA2','UPA1','SELMUX','UPA7'])
    instrucciones += instruction_to_string_eha(direccion="e03",prueba="00",vf="0",mutations=['nERA0','nOEUPA','nDUPA','RA0','RA1','CC'])
    instrucciones += instruction_to_string_eha(direccion="e04",prueba="00",vf="0",mutations=['SELBUS','UPA2','UPA1','UPA0','nERA1'])
    instrucciones += instruction_to_string_eha(direccion="e05",prueba="00",vf="0",mutations=['nOEUPA','nDUPA','nERA1','RA2'])
    instrucciones += instruction_to_string_eha(direccion="e06",prueba="00",vf="0",mutations=['nERA2','nCBD'])
    instrucciones += instruction_to_string_eha(direccion="e07",prueba="00",vf="0",mutations=['nAS','EB1','EB0','UPA3','UPA4','SELMUX'])
    instrucciones += instruction_to_string_eha(direccion="e08",prueba="0f",vf="1",inst="11",mutations=['nOEUPA','nDUPA','EB0','nWB','CH','CN','CZ','CV','CC'])
    instrucciones += instruction_to_string_eha(direccion="e09",liga="09",prueba="18",vf="0",inst="01" ,mutations=["nepc2","ncbd"])
    #ADDA(ind,x)
    instrucciones += instruction_to_string_eha(direccion="ab0",prueba="00",vf="0",mutations=['nEPC2','nCBD'])
    instrucciones += instruction_to_string_eha(direccion="ab1",prueba="00",vf="0",mutations=['nAS','UPA2','UPA1','UPA0','UPA5','UPA4','PC0'])
    instrucciones += instruction_to_string_eha(direccion="ab2",prueba="00",vf="0",mutations=['UPA2','UPA1','nEX0','SELMUX'])
    instrucciones += instruction_to_string_eha(direccion="ab3",prueba="00",vf="0",mutations=['nDUPA','nOEUPA','RA1','RA0','nERA0','CC'])
    instrucciones += instruction_to_string_eha(direccion="ab4",prueba="00",vf="0",mutations=['SELBUS','nERA1','UPA1'])
    instrucciones += instruction_to_string_eha(direccion="ab5",prueba="00",vf="0",mutations=['nDUPA','nOEUPA','RA2','nERA1','nDUPA','nOEUPA'])
    instrucciones += instruction_to_string_eha(direccion="ab6",prueba="00",vf="0",mutations=['nERA2','nCBD'])
    instrucciones += instruction_to_string_eha(direccion="ab7",prueba="00",vf="0",mutations=['nAS','EA1','EA0','UPA2','UPA0','SELMUX'])
    instrucciones += instruction_to_string_eha(direccion="ab8",prueba="0f",vf="1",inst="11",mutations=['nOEUPA','nDUPA','EA0','nWA','CH','CN','CZ','CV','CC'])
    instrucciones += instruction_to_string_eha(direccion="ab9",liga="09",prueba="18",vf="0",inst="01" ,mutations=["nepc2","ncbd"])

    print(instrucciones)
    print_errors()
    get_info_instruccion("0000000000000000000010010010000000000011011100001110001110000110000110000000000000000000000010")
    memoria_str = ""
    memoria_str += ram_to_string(pos="0",contenido="20")
    memoria_str += ram_to_string(pos="1",contenido="0B")
    memoria_str += ram_to_string(pos="2",contenido="00")
    memoria_str += ram_to_string(pos="3",contenido="02")
    memoria_str += ram_to_string(pos="4",contenido="04")
    memoria_str += ram_to_string(pos="5",contenido="05")
    memoria_str += ram_to_string(pos="6",contenido="01")
    memoria_str += ram_to_string(pos="7",contenido="02")
    memoria_str += ram_to_string(pos="8",contenido="06")
    memoria_str += ram_to_string(pos="9",contenido="07")
    memoria_str += ram_to_string(pos="10",contenido="09")
    memoria_str += ram_to_string(pos="11",contenido="01")
    memoria_str += ram_to_string(pos="12",contenido="86")
    memoria_str += ram_to_string(pos="13",contenido="00")
    memoria_str += ram_to_string(pos="14",contenido="C6")
    memoria_str += ram_to_string(pos="15",contenido="00")
    memoria_str += ram_to_string(pos="16",contenido="DE")
    memoria_str += ram_to_string(pos="17",contenido="03")
    memoria_str += ram_to_string(pos="18",contenido="FF")
    memoria_str += ram_to_string(pos="19",contenido="16")
    memoria_str += ram_to_string(pos="20",contenido="AB")
    memoria_str += ram_to_string(pos="21",contenido="00")
    memoria_str += ram_to_string(pos="22",contenido="E0")
    memoria_str += ram_to_string(pos="23",contenido="00")
    memoria_str += ram_to_string(pos="24",contenido="8C")
    memoria_str += ram_to_string(pos="25",contenido="0A")
    memoria_str += ram_to_string(pos="26",contenido="2F")
    memoria_str += ram_to_string(pos="27",contenido="0A")
    memoria_str += ram_to_string(pos="28",contenido="1B")
    memoria_str += ram_to_string(pos="29",contenido="97")
    memoria_str += ram_to_string(pos="30",contenido="02")
    memoria_str += ram_to_string(pos="31",contenido="20")
    memoria_str += ram_to_string(pos="32",contenido="1F")
    print(memoria_str)

    ins = '''
    0000000000000000000010010010000000000011011100001110001110000110000110000000000000000000000010
	0000000000000000000010010010000000000011011100001011001110001110011011000000000000000000000010
	0000000000000000000010010010000000000011011100001110001110000110000110000000000000000000000010
	0000000000000000000010010010000000000011011100001100111110001110011010000000000000000000000010
	0111111100000000000010010010000000000011011100001000001110001001011110000000000000000000000010
	1100000100000000000010010010000000000011011100001110001110000110000110000000000000000000000010
    '''
    get_info_instruccion("0000000000000000000010010010000000000011011100001110001110000110000110000000000000000000000010")
    get_info_instruccion("0000000000000000000010010010000000000011011100001011001110001110011011000000000000000000000010")
    get_info_instruccion("0000000000000000000010010010000000000011011100001110001110000110000110000000000000000000000010")
    get_info_instruccion("0000000000000000000010010010000000000011011100001100111110001110011010000000000000000000000010")
    get_info_instruccion("0111111100000000000010010010000000000011011100001000001110001001011110000000000000000000000010")
    get_info_instruccion("1100000100000000000010010010000000000011011100001110001110000110000110000000000000000000000010")