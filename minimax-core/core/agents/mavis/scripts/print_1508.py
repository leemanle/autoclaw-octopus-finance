# -*- coding: utf-8 -*-
"""把 1508 号文打印到指定网络打印机（WPS COM）"""
import os, sys, time, io
import win32print
import win32com.client

PRINTER = "NPIA3A861 (HP LaserJet MFP M30w)"
DOCX = (sys.argv[1] if len(sys.argv) > 1 else
        r"C:\Users\Administrator\Desktop\国家发展改革委等部门关于加强消费基础设施建设促进消费投资良性互动的指导意见（发改就业〔2026〕1508号）.docx")
COPIES = 1

log = io.open(r"C:\Users\Administrator\.minimax\agents\mavis\scripts\_print1508.log", "w", encoding="utf-8")
def L(*a):
    s = " ".join(str(x) for x in a)
    log.write(s + "\n"); log.flush()
    print(s.encode("ascii", "replace").decode("ascii"))

_h = win32print.OpenPrinter(PRINTER)
try:
    _info = win32print.GetPrinter(_h, 2)
    L("printer found:", _info.get("pPrinterName"), "| status:", _info.get("Status"), "| jobs:", _info.get("Jobs"))
finally:
    win32print.ClosePrinter(_h)
L("current default:", win32print.GetDefaultPrinter())

old_default = win32print.GetDefaultPrinter()
if old_default != PRINTER:
    win32print.SetDefaultPrinter(PRINTER)
    L("default printer switched ->", win32print.GetDefaultPrinter())

wps = None
doc = None
try:
    wps = win32com.client.DispatchEx("KWPS.Application")
    wps.Visible = False
    try:
        wps.DisplayAlerts = 0
    except Exception:
        pass
    L("wps started")
    doc = wps.Documents.Open(DOCX)
    L("doc opened, pages:", doc.ComputeStatistics(2))  # wdStatisticPages

    ok = False
    try:
        doc.PrintOut(Background=False, Copies=COPIES, ActivePrinter=PRINTER)
        ok = True
        L("PrintOut named-args OK")
    except Exception as e:
        L("named-args failed:", e)
        # 位置参数: Background, Append, Range, OutputFileName, From, To, Item, Copies, Pages, PageSetup, ActivePrinter
        doc.PrintOut(False, False, 0, "", 0, 0, 0, COPIES, "", "", PRINTER)
        ok = True
        L("PrintOut positional OK")
    L("printout returned, ok =", ok)

    # 等待队列出清
    for i in range(60):
        h2 = win32print.OpenPrinter(PRINTER)
        try:
            jobs = win32print.EnumJobs(h2, 0, 0, 2)
        finally:
            win32print.ClosePrinter(h2)
        if not jobs:
            L("queue empty after", i, "s")
            break
        L("jobs pending:", len(jobs), [(j["JobId"], j["Status"]) for j in jobs])
        time.sleep(2)
    doc.Close(False)
    doc = None
except Exception as e:
    L("ERROR:", repr(e))
finally:
    try:
        if doc is not None:
            doc.Close(False)
    except Exception:
        pass
    try:
        if wps is not None:
            wps.Quit()
    except Exception:
        pass
    if old_default and old_default != PRINTER:
        try:
            win32print.SetDefaultPrinter(old_default)
            L("default printer restored ->", win32print.GetDefaultPrinter())
        except Exception as e:
            L("restore failed:", e)
    log.close()
