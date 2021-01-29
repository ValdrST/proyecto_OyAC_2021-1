import csv

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

def copy_paste_drive_to_vhdl(memoria):

    memoria = memoria.replace(" ","").split("\n")[1:-1]
    print(memoria)
    memoria_loc = ""
    memoria_tr = ""
    for m in memoria:
        if 'x' in m and len(m) >= 5:
            memoria_loc += "\";\n"
            memoria_tr += memoria_loc
            memoria_loc = ""
            memoria_loc = "memoria({}) <=  x\"".format(int(m[2:],16))
        else:
            if 'x' in m:
                m = m.replace('0x','')
            memoria_loc += "{}".format(m)
    memoria_loc += "\";\n"
    memoria_tr += memoria_loc
    print(memoria_tr)

def copy_paste_drive_datos_to_vhdl(memoria):
    memoria = memoria.replace(" ","").split("\n")[1:-1]
    memoria_loc = ""
    memoria_tr = ""
    for m in memoria:
        if 'x' in m and len(m) >= 5:
            memoria_loc += "\";\n"
            memoria_tr += memoria_loc
            memoria_loc = ""
            memoria_loc = "{} =>  x\"".format(int(m[2:],16))
        else:
            if 'x' in m:
                m = m.replace('0x','')
            memoria_loc += "{}".format(m)
    memoria_loc += "\";\n"
    memoria_tr += memoria_loc
    print(memoria_tr)

def print_errors():
    global errors
    for error in errors:
        print("salida:\033[93m{}\033[0m no valida, Direccion \033[93m0x{}\033[0m".format(error["salida"],error["dir"]))

def asm_list_to_csv(csv_file, lista_asm, asm_columns):
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=asm_columns)
            writer.writeheader()
            for data in lista_asm:
                writer.writerow(data)
    except IOError:
        print("I/O error")

def asm_default():
    instruccion={
        "inst": "0",
        "selregr": "0",
        "sels1": "0",
        "sr": "0",
        "cin": "0",
        "sels2": "0",
        "seldato": "0",
        "selsrc": "0",
        "seldir": "0",
        "selop": "0",
        "selresult": "0",
        "selc": "0",
        "cadj": "0",
        "selfalgs": "0",
        "selbranch": "0",
        "vf": "0",
        "selregw": "0",
        "memw": "0",
        "seldirw": "0"
    }
    return instruccion

asm_rules = {
    "inst": 16,
    "selregr": 4,
    "sels1": 1,
    "sr": 1,
    "cin": 1,
    "sels2": 1,
    "seldato": 1,
    "selsrc": 3,
    "seldir": 2,
    "selop": 4,
    "selresult": 2,
    "selc": 1,
    "cadj": 1,
    "selfalgs": 4,
    "selbranch": 3,
    "vf": 1,
    "selregw": 3,
    "memw": 1,
    "seldirw": 2
}

def dec_to_dir_bin(dec, tam):
    strbin = "{0:b}".format(dec)
    listbin = []
    while len(strbin) < tam:
        strbin = "0{0}".format(strbin)
    for strr in strbin:
        listbin.append(strr)
    return strbin

def rules_traductor(hex_num, rule):
    if(rule >= 16):
        string = "{}".format(hex_num)
        while len(string) < 4:
            string ="0{}".format(string)
        return "X\"{}\"".format(string)
    elif(rule == 4):
        return  "X\"{}\"".format(hex_num)
    elif(rule == 1):
        return "\'{}\'".format(dec_to_dir_bin(int(hex_num), rule))
    else:
        return "\"{}\"".format(dec_to_dir_bin(int(hex_num), rule))

def traducir_dict(asm_dict, name = ""):
    instruccion = "WHEN {} => --{}\n".format(rules_traductor(asm_dict["inst"], asm_rules["inst"]),name)
    for key in asm_dict.keys():
        if key != "inst":
            instruccion += "{} <= {};\n".format(key,rules_traductor(asm_dict[key], asm_rules[key]))
    instruccion += "\n"
    return instruccion


if __name__  == "__main__":
    instrucciones = ""
    instrucciones += traducir_dict({
        "inst": "86",
        "selregr": "0",
        "sels1": "0",
        "sr": "1",
        "cin": "0",
        "sels2": "0",
        "seldato": "1",
        "selsrc": "3",
        "seldir": "0",
        "selop": "4",
        "selresult": "1",
        "selc": "1",
        "cadj": "0",
        "selfalgs": "1",
        "selbranch": "0",
        "vf": "1",
        "selregw": "1",
        "memw": "0",
        "seldirw": "0"
    }, "LDAA(IMM)")

    instrucciones += traducir_dict({
        "inst": "C6",
        "selregr": "0",
        "sels1": "0",
        "sr": "1",
        "cin": "0",
        "sels2": "0",
        "seldato": "1",
        "selsrc": "3",
        "seldir": "0",
        "selop": "4",
        "selresult": "1",
        "selc": "1",
        "cadj": "0",
        "selfalgs": "1",
        "selbranch": "0",
        "vf": "1",
        "selregw": "4",
        "memw": "0",
        "seldirw": "0"
    }, "LDAB(IMM)")

    instrucciones += traducir_dict({
        "inst": "CE",
        "selregr": "E",
        "sels1": "0",
        "sr": "1",
        "cin": "0",
        "sels2": "0",
        "seldato": "1",
        "selsrc": "2",
        "seldir": "1",
        "selop": "4",
        "selresult": "1",
        "selc": "1",
        "cadj": "0",
        "selfalgs": "1",
        "selbranch": "0",
        "vf": "1",
        "selregw": "2",
        "memw": "0",
        "seldirw": "0"
    }, "LDX(DIR)")

    instrucciones += traducir_dict({
        "inst": "AB",
        "selregr": "6",
        "sels1": "1",
        "sr": "1",
        "cin": "0",
        "sels2": "0",
        "seldato": "1",
        "selsrc": "2",
        "seldir": "0",
        "selop": "1",
        "selresult": "1",
        "selc": "1",
        "cadj": "0",
        "selfalgs": "2",
        "selbranch": "0",
        "vf": "1",
        "selregw": "1",
        "memw": "0",
        "seldirw": "0"
    }, "ADDA(ind,x)")

    instrucciones += traducir_dict({
        "inst": "E0",
        "selregr": "2",
        "sels1": "1",
        "sr": "1",
        "cin": "0",
        "sels2": "0",
        "seldato": "1",
        "selsrc": "2",
        "seldir": "0",
        "selop": "1",
        "selresult": "1",
        "selc": "1",
        "cadj": "0",
        "selfalgs": "2",
        "selbranch": "0",
        "vf": "1",
        "selregw": "4",
        "memw": "0",
        "seldirw": "0"
    }, "SUBB(ind,x)")

    instrucciones += traducir_dict({
        "inst": "8C",
        "selregr": "E",
        "sels1": "1",
        "sr": "0",
        "cin": "0",
        "sels2": "0",
        "seldato": "1",
        "selsrc": "3",
        "seldir": "1",
        "selop": "2",
        "selresult": "0",
        "selc": "1",
        "cadj": "1",
        "selfalgs": "3",
        "selbranch": "0",
        "vf": "1",
        "selregw": "0",
        "memw": "0",
        "seldirw": "0"
    }, "CPX(IMM)")

    instrucciones += traducir_dict({
        "inst": "2F",
        "selregr": "0",
        "sels1": "0",
        "sr": "1",
        "cin": "0",
        "sels2": "1",
        "seldato": "0",
        "selsrc": "5",
        "seldir": "0",
        "selop": "1",
        "selresult": "1",
        "selc": "1",
        "cadj": "0",
        "selfalgs": "0",
        "selbranch": "4",
        "vf": "1",
        "selregw": "0",
        "memw": "0",
        "seldirw": "0"
    }, "BLE")

    instrucciones += traducir_dict({
        "inst": "20",
        "selregr": "0",
        "sels1": "0",
        "sr": "1",
        "cin": "0",
        "sels2": "1",
        "seldato": "0",
        "selsrc": "5",
        "seldir": "0",
        "selop": "1",
        "selresult": "1",
        "selc": "1",
        "cadj": "0",
        "selfalgs": "0",
        "selbranch": "0",
        "vf": "1",
        "selregw": "0",
        "memw": "0",
        "seldirw": "0"
    }, "BRA")

    instrucciones += traducir_dict({
        "inst": "80",
        "selregr": "E",
        "sels1": "0",
        "sr": "1",
        "cin": "0",
        "sels2": "0",
        "seldato": "1",
        "selsrc": "3",
        "seldir": "0",
        "selop": "1",
        "selresult": "1",
        "selc": "1",
        "cadj": "1",
        "selfalgs": "C",
        "selbranch": "0",
        "vf": "1",
        "selregw": "2",
        "memw": "0",
        "seldirw": "0"
    }, "INCX")

    instrucciones += traducir_dict({
        "inst": "01",
        "selregr": "0",
        "sels1": "0",
        "sr": "0",
        "cin": "0",
        "sels2": "0",
        "seldato": "0",
        "selsrc": "0",
        "seldir": "0",
        "selop": "0",
        "selresult": "0",
        "selc": "0",
        "cadj": "0",
        "selfalgs": "0",
        "selbranch": "0",
        "vf": "1",
        "selregw": "0",
        "memw": "0",
        "seldirw": "0"
    }, "NOP")

    instrucciones += traducir_dict({
        "inst": "7E",
        "selregr": "0",
        "sels1": "0",
        "sr": "0",
        "cin": "0",
        "sels2": "0",
        "seldato": "0",
        "selsrc": "3",
        "seldir": "0",
        "selop": "4",
        "selresult": "1",
        "selc": "0",
        "cadj": "0",
        "selfalgs": "0",
        "selbranch": "0",
        "vf": "1",
        "selregw": "0",
        "memw": "0",
        "seldirw": "0"
    }, "JMP(EXT)")

    instrucciones += traducir_dict({
        "inst": "A5",
        "selregr": "9",
        "sels1": "0",
        "sr": "1",
        "cin": "0",
        "sels2": "0",
        "seldato": "1",
        "selsrc": "2",
        "seldir": "0",
        "selop": "B",
        "selresult": "0",
        "selc": "1",
        "cadj": "1",
        "selfalgs": "1",
        "selbranch": "0",
        "vf": "1",
        "selregw": "0",
        "memw": "0",
        "seldirw": "0"
    }, "XPAR")

    instrucciones += traducir_dict({
        "inst": "27",
        "selregr": "0",
        "sels1": "0",
        "sr": "1",
        "cin": "0",
        "sels2": "1",
        "seldato": "0",
        "selsrc": "5",
        "seldir": "0",
        "selop": "1",
        "selresult": "1",
        "selc": "1",
        "cadj": "0",
        "selfalgs": "0",
        "selbranch": "2",
        "vf": "1",
        "selregw": "0",
        "memw": "0",
        "seldirw": "0"
    }, "BEQ")

    instrucciones += traducir_dict({
        "inst": "25",
        "selregr": "0",
        "sels1": "0",
        "sr": "1",
        "cin": "0",
        "sels2": "1",
        "seldato": "0",
        "selsrc": "5",
        "seldir": "0",
        "selop": "1",
        "selresult": "1",
        "selc": "1",
        "cadj": "0",
        "selfalgs": "0",
        "selbranch": "1",
        "vf": "1",
        "selregw": "0",
        "memw": "0",
        "seldirw": "0"
    }, "BLO")

    instrucciones += traducir_dict({
        "inst": "AD",
        "selregr": "1",
        "sels1": "0",
        "sr": "1",
        "cin": "0",
        "sels2": "0",
        "seldato": "1",
        "selsrc": "1",
        "seldir": "0",
        "selop": "1",
        "selresult": "1",
        "selc": "1",
        "cadj": "0",
        "selfalgs": "2",
        "selbranch": "0",
        "vf": "1",
        "selregw": "2",
        "memw": "0",
        "seldirw": "0"
    }, "XABA")

    print(instrucciones)


    memoria_datos = """
0x0000
0x00
0x02
0x0001
0x00
0x04
0x0002
0x00
0x05
0x0003
0x00
0x01
0x0004
0x00
0x02
0x0005
0x00
0x06
0x0006
0x00
0x07
0x0007
0x00
0x09
0x0008
0x00
0x01
        """
    memoria_inst = """        
        0x0000
        00
        86
        00
        00
        0x0001
        00
        C6
        00
        00
        0x0002
        00
        DE
        00
        01
        0x0003
        00
        00
        00
        01
        0x0004
        00
        00
        00
        01
        0x0005
        00
        AD
        00
        0A
        0x0006
        00
        AB
        00
        00
        0x0007
        00
        8C
        00
        09
        0x0008
        00
        2F
        00
        05
        0x0009
        00
        20
        00
        0D
        0x000A
        00
        E0
        00
        00
        0x000B
        00
        8C
        00
        09
        0x000C
        00
        2F
        00
        05
        0x000D
        00
        1B
        00
        00
        0x000E
        00
        97
        00
        00
        0x000F
        00
        20
        00
        0F
        """
    memoria_inst = """
0x0000
00
86
00
00
0x0001
00
01
00
00
0x0002
00
01
00
00
    """
    copy_paste_drive_to_vhdl(memoria_inst)
    copy_paste_drive_datos_to_vhdl(memoria_datos)