
import os

from mmgui import App, BrowserWindow

app = App(headless=False)
dict1 = {
    "FILE_DEVICE_BEEP": 0x00000001,
    "FILE_DEVICE_CD_ROM": 0x00000002,
    "FILE_DEVICE_CD_ROM_FILE_SYSTEM": 0x00000003,
    "FILE_DEVICE_CONTROLLER": 0x00000004,
    "FILE_DEVICE_DATALINK": 0x00000005,
    "FILE_DEVICE_DFS": 0x00000006,
    "FILE_DEVICE_DISK": 0x00000007,
    "FILE_DEVICE_DISK_FILE_SYSTEM": 0x00000008,
    "FILE_DEVICE_FILE_SYSTEM": 0x00000009,
    "FILE_DEVICE_INPORT_PORT": 0x0000000a,
    "FILE_DEVICE_KEYBOARD": 0x0000000b,
    "FILE_DEVICE_MAILSLOT": 0x0000000c,
    "FILE_DEVICE_MIDI_IN": 0x0000000d,
    "FILE_DEVICE_MIDI_OUT": 0x0000000e,
    "FILE_DEVICE_MOUSE": 0x0000000f,
    "FILE_DEVICE_MULTI_UNC_PROVIDER": 0x00000010,
    "FILE_DEVICE_NAMED_PIPE": 0x00000011,
    "FILE_DEVICE_NETWORK": 0x00000012,
    "FILE_DEVICE_NETWORK_BROWSER": 0x00000013,
    "FILE_DEVICE_NETWORK_FILE_SYSTEM": 0x00000014,
    "FILE_DEVICE_NULL": 0x00000015,
    "FILE_DEVICE_PARALLEL_PORT": 0x00000016,
    "FILE_DEVICE_PHYSICAL_NETCARD": 0x00000017,
    "FILE_DEVICE_PRINTER": 0x00000018,
    "FILE_DEVICE_SCANNER": 0x00000019,
    "FILE_DEVICE_SERIAL_MOUSE_PORT": 0x0000001a,
    "FILE_DEVICE_SERIAL_PORT": 0x0000001b,
    "FILE_DEVICE_SCREEN": 0x0000001c,
    "FILE_DEVICE_SOUND": 0x0000001d,
    "FILE_DEVICE_STREAMS": 0x0000001e,
    "FILE_DEVICE_TAPE": 0x0000001f,
    "FILE_DEVICE_TAPE_FILE_SYSTEM": 0x00000020,
    "FILE_DEVICE_TRANSPORT": 0x00000021,
    "FILE_DEVICE_UNKNOWN": 0x00000022,
    "FILE_DEVICE_VIDEO": 0x00000023,
    "FILE_DEVICE_VIRTUAL_DISK": 0x00000024,
    "FILE_DEVICE_WAVE_IN": 0x00000025,
    "FILE_DEVICE_WAVE_OUT": 0x00000026,
    "FILE_DEVICE_8042_PORT": 0x00000027,
    "FILE_DEVICE_NETWORK_REDIRECTOR": 0x00000028,
    "FILE_DEVICE_BATTERY": 0x00000029,
    "FILE_DEVICE_BUS_EXTENDER": 0x0000002a,
    "FILE_DEVICE_MODEM": 0x0000002b,
    "FILE_DEVICE_VDM": 0x0000002c,
    "FILE_DEVICE_MASS_STORAGE": 0x0000002d,
    "FILE_DEVICE_SMB": 0x0000002e,
    "FILE_DEVICE_KS": 0x0000002f,
    "FILE_DEVICE_CHANGER": 0x00000030,
    "FILE_DEVICE_SMARTCARD": 0x00000031,
    "FILE_DEVICE_ACPI": 0x00000032,
    "FILE_DEVICE_DVD": 0x00000033,
    "FILE_DEVICE_FULLSCREEN_VIDEO": 0x00000034,
    "FILE_DEVICE_DFS_FILE_SYSTEM": 0x00000035,
    "FILE_DEVICE_DFS_VOLUME": 0x00000036,
    "FILE_DEVICE_SERENUM": 0x00000037,
    "FILE_DEVICE_TERMSRV": 0x00000038,
    "FILE_DEVICE_KSEC": 0x00000039,
    "FILE_DEVICE_FIPS": 0x0000003A,
    "FILE_DEVICE_INFINIBAND": 0x0000003B,
    "FILE_DEVICE_VMBUS": 0x0000003E,
    "FILE_DEVICE_CRYPT_PROVIDER": 0x0000003F,
    "FILE_DEVICE_WPD": 0x00000040,
    "FILE_DEVICE_BLUETOOTH": 0x00000041,
    "FILE_DEVICE_MT_COMPOSITE": 0x00000042,
    "FILE_DEVICE_MT_TRANSPORT": 0x00000043,
    "FILE_DEVICE_BIOMETRIC": 0x00000044,
    "FILE_DEVICE_PMI": 0x00000045,
    "FILE_DEVICE_EHSTOR": 0x00000046,
    "FILE_DEVICE_DEVAPI": 0x00000047,
    "FILE_DEVICE_GPIO": 0x00000048,
    "FILE_DEVICE_USBEX": 0x00000049,
    "FILE_DEVICE_CONSOLE": 0x00000050,
    "FILE_DEVICE_NFP": 0x00000051,
    "FILE_DEVICE_SYSENV": 0x00000052,
    "FILE_DEVICE_VIRTUAL_BLOCK": 0x00000053,
    "FILE_DEVICE_POINT_OF_SERVICE": 0x00000054,
    "FILE_DEVICE_STORAGE_REPLICATION": 0x00000055,
    "FILE_DEVICE_TRUST_ENV": 0x00000056,
    "FILE_DEVICE_UCM": 0x00000057,
    "FILE_DEVICE_UCMTCPCI": 0x00000058,
    "FILE_DEVICE_PERSISTENT_MEMORY": 0x00000059,
    "FILE_DEVICE_NVDIMM": 0x0000005a,
    "FILE_DEVICE_HOLOGRAPHIC": 0x0000005b,
    "FILE_DEVICE_SDFXHCI": 0x0000005c,
    "FILE_DEVICE_UCMUCSI": 0x0000005d
}

dict2 = {
    0x00000001: "FILE_DEVICE_BEEP",
    0x00000002: "FILE_DEVICE_CD_ROM",
    0x00000003: "FILE_DEVICE_CD_ROM_FILE_SYSTEM",
    0x00000004: "FILE_DEVICE_CONTROLLER",
    0x00000005: "FILE_DEVICE_DATALINK",
    0x00000006: "FILE_DEVICE_DFS",
    0x00000007: "FILE_DEVICE_DISK",
    0x00000008: "FILE_DEVICE_DISK_FILE_SYSTEM",
    0x00000009: "FILE_DEVICE_FILE_SYSTEM",
    0x0000000a: "FILE_DEVICE_INPORT_PORT",
    0x0000000b: "FILE_DEVICE_KEYBOARD",
    0x0000000c: "FILE_DEVICE_MAILSLOT",
    0x0000000d: "FILE_DEVICE_MIDI_IN",
    0x0000000e: "FILE_DEVICE_MIDI_OUT",
    0x0000000f: "FILE_DEVICE_MOUSE",
    0x00000010: "FILE_DEVICE_MULTI_UNC_PROVIDER",
    0x00000011: "FILE_DEVICE_NAMED_PIPE",
    0x00000012: "FILE_DEVICE_NETWORK",
    0x00000013: "FILE_DEVICE_NETWORK_BROWSER",
    0x00000014: "FILE_DEVICE_NETWORK_FILE_SYSTE",
    0x00000015: "FILE_DEVICE_NULL",
    0x00000016: "FILE_DEVICE_PARALLEL_PORT",
    0x00000017: "FILE_DEVICE_PHYSICAL_NETCARD",
    0x00000018: "FILE_DEVICE_PRINTER",
    0x00000019: "FILE_DEVICE_SCANNER",
    0x0000001a: "FILE_DEVICE_SERIAL_MOUSE_PORT",
    0x0000001b: "FILE_DEVICE_SERIAL_PORT",
    0x0000001c: "FILE_DEVICE_SCREEN",
    0x0000001d: "FILE_DEVICE_SOUND",
    0x0000001e: "FILE_DEVICE_STREAMS",
    0x0000001f: "FILE_DEVICE_TAPE",
    0x00000020: "FILE_DEVICE_TAPE_FILE_SYSTEM",
    0x00000021: "FILE_DEVICE_TRANSPORT",
    0x00000022: "FILE_DEVICE_UNKNOWN",
    0x00000023: "FILE_DEVICE_VIDEO",
    0x00000024: "FILE_DEVICE_VIRTUAL_DISK",
    0x00000025: "FILE_DEVICE_WAVE_IN",
    0x00000026: "FILE_DEVICE_WAVE_OUT",
    0x00000027: "FILE_DEVICE_8042_PORT",
    0x00000028: "FILE_DEVICE_NETWORK_REDIRECTOR",
    0x00000029: "FILE_DEVICE_BATTERY",
    0x0000002a: "FILE_DEVICE_BUS_EXTENDER",
    0x0000002b: "FILE_DEVICE_MODEM",
    0x0000002c: "FILE_DEVICE_VDM",
    0x0000002d: "FILE_DEVICE_MASS_STORAGE",
    0x0000002e: "FILE_DEVICE_SMB",
    0x0000002f: "FILE_DEVICE_KS",
    0x00000030: "FILE_DEVICE_CHANGER",
    0x00000031: "FILE_DEVICE_SMARTCARD",
    0x00000032: "FILE_DEVICE_ACPI",
    0x00000033: "FILE_DEVICE_DVD",
    0x00000034: "FILE_DEVICE_FULLSCREEN_VIDEO",
    0x00000035: "FILE_DEVICE_DFS_FILE_SYSTEM",
    0x00000036: "FILE_DEVICE_DFS_VOLUME",
    0x00000037: "FILE_DEVICE_SERENUM",
    0x00000038: "FILE_DEVICE_TERMSRV",
    0x00000039: "FILE_DEVICE_KSEC",
    0x0000003A: "FILE_DEVICE_FIPS",
    0x0000003B: "FILE_DEVICE_INFINIBAND",
    0x0000003E: "FILE_DEVICE_VMBUS",
    0x0000003F: "FILE_DEVICE_CRYPT_PROVIDER",
    0x00000040: "FILE_DEVICE_WPD",
    0x00000041: "FILE_DEVICE_BLUETOOTH",
    0x00000042: "FILE_DEVICE_MT_COMPOSITE",
    0x00000043: "FILE_DEVICE_MT_TRANSPORT",
    0x00000044: "FILE_DEVICE_BIOMETRIC",
    0x00000045: "FILE_DEVICE_PMI",
    0x00000046: "FILE_DEVICE_EHSTOR",
    0x00000047: "FILE_DEVICE_DEVAPI",
    0x00000048: "FILE_DEVICE_GPIO",
    0x00000049: "FILE_DEVICE_USBEX",
    0x00000050: "FILE_DEVICE_CONSOLE",
    0x00000051: "FILE_DEVICE_NFP",
    0x00000052: "FILE_DEVICE_SYSENV",
    0x00000053: "FILE_DEVICE_VIRTUAL_BLOCK",
    0x00000054: "FILE_DEVICE_POINT_OF_SERVICE",
    0x00000055: "FILE_DEVICE_STORAGE_REPLICATIO",
    0x00000056: "FILE_DEVICE_TRUST_ENV",
    0x00000057: "FILE_DEVICE_UCM",
    0x00000058: "FILE_DEVICE_UCMTCPCI",
    0x00000059: "FILE_DEVICE_PERSISTENT_MEMORY",
    0x0000005a: "FILE_DEVICE_NVDIMM",
    0x0000005b: "FILE_DEVICE_HOLOGRAPHIC",
    0x0000005c: "FILE_DEVICE_SDFXHCI",
    0x0000005d: "FILE_DEVICE_UCMUCSI",
}
def Macro_Code(code: str, function, method, access):
    list_m = ["METHOD_BUFFERED","METHOD_IN_DIRECT","METHOD_OUT_DIRECT","METHOD_NEITHER"]
    list_a = ["FILE_READ_ACCESS","FILE_WRITE_ACCESS","FILE_ANY_ACCESS"]
    if method not in list_m or access not in list_a:
        return "参数错误请重新输入"
    if method == "METHOD_BUFFERED":
        if len(hex(int(function, 16) * 4)[2:]) == 3:
            code += "0" + str(hex(int(function, 16) * 4)[2:])
        elif len(hex(int(function, 16) * 4)[2:]) == 2:
            code += "00" + str(hex(int(function, 16) * 4)[2:])
        elif len(hex(int(function, 16) * 4)[2:]) == 1:
            code += "000" + str(hex(int(function, 16) * 4)[2:])
        else:
            code +=str(hex(int(function, 16) * 4)[2:])
    elif method == "METHOD_IN_DIRECT":
        if len(hex(int(function, 16) * 4 + 1)[2:]) == 3:
            code += "0" + str(hex(int(function, 16) * 4 + 1)[2:])
        elif len(hex(int(function, 16) * 4 + 1)[2:]) == 2:
            code += "00" + str(hex(int(function, 16) * 4 + 1)[2:])
        elif len(hex(int(function, 16) * 4 + 1)[2:]) == 1:
            code += "000" + str(hex(int(function, 16) * 4 + 1)[2:])
        else:
            code +=str(hex(int(function, 16) * 4 + 1)[2:])
    elif method == "METHOD_OUT_DIRECT":
        if len(hex(int(function, 16) * 4 + 2)[2:]) == 3:
            code += "0" + str(hex(int(function, 16) * 4 + 2)[2:])
        elif len(hex(int(function, 16) * 4 + 2)[2:]) == 2:
            code += "00" + str(hex(int(function, 16) * 4 + 2)[2:])
        elif len(hex(int(function, 16) * 4 + 2)[2:]) == 1:
            code += "000" + str(hex(int(function, 16) * 4 + 2)[2:])
        else:
            code += str(hex(int(function, 16) * 4 + 2)[2:])
    elif method == "METHOD_NEITHER":
        if len(hex(int(function, 16) * 4 + 3)[2:]) == 3:
            code += "0" + str(hex(int(function, 16) * 4 + 3)[2:])
        elif len(hex(int(function, 16) * 4 + 3)[2:]) == 2:
            code += "00" + str(hex(int(function, 16) * 4 + 3)[2:])
        elif len(hex(int(function, 16) * 4 + 3)[2:]) == 1:
            code += "000" + str(hex(int(function, 16) * 4 + 3)[2:])
        else:
            code += str(hex(int(function, 16) * 4 + 3)[2:])

    list1 = list(code)
    if access == "FILE_READ_ACCESS":
        list_ = int(list1.pop(-4)) + 4
        list1.insert(-3,list_)
    elif access == "FILE_WRITE_ACCESS":
        list_ = int(list1.pop(-4)) + 8
        list1.insert(-3, list_)
    code = ""
    if len(list1) != 0:
        for i in range(len(list1)):
            code += str(list1[i])
    return "0x%x" % int(code,16)


def Code_Macro(index: str):
    list1 = [0, 1, 2, 3]
    list2 = [4, 5, 6, 7]
    get_f = 0
    get_d = ""
    get_m = ""
    get_a = ""
    at = int(index[-1],16)

    if at < 4:
        f = at
    else:
        f = at % 4

    if f == 0:
        get_m = "METHOD_BUFFERED"
    elif f == 1:
        get_m = "METHOD_IN_DIRECT"
    elif f == 2:
        get_m = "METHOD_OUT_DIRECT"
    elif f == 3:
        get_m = "METHOD_NEITHER"

    at1 = int(index[-4:-3])
    if at1 in list1:
        get_a = "FILE_ANY_ACCESS"
    elif at1 in list2:
        get_a = "FILE_READ_ACCESS"
    elif at1 == 8 or at1 == 9:
        get_a = "FILE_WRITE_ACCESS"

    at3 = int(index[2:-4],16)
    if at3 in dict2.keys():
        get_d = dict2[at3]
    else:
        return "未找到对应的function"

    at2 = index[-4:]
    i_ = int(at2[-4:], 16) // 4
    get_f = "{:X}".format(i_)[-3:]
    if get_f == "0":
        return "#define IO_CTL_DIY CTL_CODE(" + get_d + ", 0x" + get_f + "," + get_m + "," + get_a + ")"
    lstrip1 = get_f.lstrip("0")
    return "#define IO_CTL_DIY CTL_CODE(" + get_d + ", 0x" + lstrip1 + "," + get_m + "," + get_a + ")"

def operation(msg):
    list_ck = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
               "a", "b", "c", "d", "e", "f", "F", "E", "D", "C", "B","A"]
    if "code" in msg:
        code = msg["code"]
        if code[:2] != "0x" and code[:2] != "0X":
            win.webview.send_message_to_js({"msg": "^参数错误请重新输入"})
            return
        for i in code[2:]:
            if i not in list_ck:
                win.webview.send_message_to_js({"msg": "^参数错误请重新输入"})
                return

        macro = Code_Macro(code)
        win.webview.send_message_to_js({"msg":"^"+macro})
    elif "device_type" in msg:
        device_type = msg["device_type"]
        function = msg["function"]
        method = msg["method"]
        access = msg["access"]
        net = 0
        if device_type[:2] != "0x" and device_type not in dict1.keys():
            win.webview.send_message_to_js({"msg": "f参数错误请重新输入"})
            return
        if device_type in dict1.keys():
            code1 = "0x%x" % dict1[device_type]
            code2 = Macro_Code(code1, function, method, access)
            win.webview.send_message_to_js({"msg": "f" + code2})
            win.webview.send_message_to_js({"msg": "?" + "#define IO_CTL_DIY CTL_CODE(" + device_type + ", " + function + "," + method + "," + access + ")"})
            return
        for i in device_type[2:]:
            if i not in list_ck:
                win.webview.send_message_to_js({"msg": "f参数错误请重新输入"})
                return
        net = int(device_type,16)
        if net not in dict1.values():
            win.webview.send_message_to_js({"msg": "f未找到该函数,请输入正确的函数"})

        else:
            code1 = "0x%x" % net
        code2 = Macro_Code(code1, function, method, access)
        win.webview.send_message_to_js({"msg": "f"+code2})

        win.webview.send_message_to_js({"msg": "?"+"#define IO_CTL_DIY CTL_CODE(" + dict2[net] + ", " + function + "," + method + "," + access + ")"})

    elif "ccode" in msg:
        micro = msg["ccode"]
        list1 = micro.split(")")[0].split("(")[1].split(",")

        if list1[0].strip() not in dict1.keys():
            win.webview.send_message_to_js({"msg": "!" + "未找到该函数,请输入正确的函数"})
        else:
            code = "0x%x" % dict1[list1[0].strip()]
        macro_code = Macro_Code(code, list1[1].strip(), list1[2].strip(), list1[3].strip())
        win.webview.send_message_to_js({"msg":"!"+ macro_code})
def on_create(ctx):
    global win

    win = BrowserWindow({
        "title": "CtlCode",
        "width": 1200,
        "height": 800,
        "dev_mode": False,
    })

    win.webview.load_file(os.path.join(os.path.dirname(os.path.abspath(__file__)), "ui", "index.html"))
    win.webview.bind_function("operation", operation)
    win.webview.bind_function("Macro_Code", Macro_Code)
    win.webview.bind_function("Code_Macro", Code_Macro)
    win.show()

def main():

    app.on("create", on_create)
    app.run()


if __name__ == "__main__":
    main()