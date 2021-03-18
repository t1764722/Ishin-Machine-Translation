#automatic libretranslate script for yakuza games etc etc by garnetsunset
import json
import argparse
import polib
import time
import datetime
import re
import os, sys
import requests
import glob
from pathlib import Path
from os import path as realPath


poList = []
processes = []

for root, dirs, files in os.walk("..\\firstdir"):
    for file in files:
        if file.endswith(".po"):
             poList.append(os.path.join(root, file))
             Path(root.replace("..\\firstdir\\", "..\\lastdir\\")).mkdir(parents=True, exist_ok=True)

try:
    os.mkdir('..\\lastdir')    
except:
    pass

regex = u'[\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf]'
headers = {
    'accept': 'application/json',
    'Content-Type': 'application/x-www-form-urlencoded',
}

for fileName in poList:
    c=0
    input_file = polib.pofile(fileName)
    output_file = polib.POFile()
    output_file.metadata = {
    'Project-Id-Version': 'Ryū ga Gotoku Ishin!',
    'Report-Msgid-Bugs-To': 'dummy@dummy.com',
    'POT-Creation-Date': '3/14/2021',
    'PO-Revision-Date': '',
    'Last-Translator': '',
    'Language-Team': '',
    'Language': 'es-ES',
    'MIME-Version': '1.0',
    'Content-Type': 'text/plain; charset=UTF-8',
    'Content-Transfer-Encoding': '8bit',
    }
    for entry in input_file:
        if re.match(regex, str(entry.msgid)):
            if realPath.isfile(fileName.replace("..\\firstdir\\", "..\\lastdir\\")) == False:   
                if "TAG_" in entry.msgctxt:
                    translated_entry = polib.POEntry(
                        msgctxt=entry.msgctxt,
                        msgid=entry.msgid,
                        msgstr=entry.msgid
                        )
                elif "KIND_" in entry.msgctxt:
                    translated_entry = polib.POEntry(
                        msgctxt=entry.msgctxt,
                        msgid=entry.msgid,
                        msgstr=entry.msgid
                        )
                elif "SHOP_ID" in entry.msgctxt:
                    translated_entry = polib.POEntry(
                        msgctxt=entry.msgctxt,
                        msgid=entry.msgid,
                        msgstr=entry.msgid
                        )
                elif "CATEGORY_" in entry.msgctxt:
                    translated_entry = polib.POEntry(
                        msgctxt=entry.msgctxt,
                        msgid=entry.msgid,
                        msgstr=entry.msgid
                        )
                elif "FINISH_FLAG" in entry.msgctxt:
                    translated_entry = polib.POEntry(
                        msgctxt=entry.msgctxt,
                        msgid=entry.msgid,
                        msgstr=entry.msgid
                        )
                elif "PLAYER_" in entry.msgctxt:
                    translated_entry = polib.POEntry(
                        msgctxt=entry.msgctxt,
                        msgid=entry.msgid,
                        msgstr=entry.msgid
                        )
                elif "TYPE_" in entry.msgctxt:
                    translated_entry = polib.POEntry(
                        msgctxt=entry.msgctxt,
                        msgid=entry.msgid,
                        msgstr=entry.msgid
                        )
                elif "UNIT_" in entry.msgctxt:
                    translated_entry = polib.POEntry(
                        msgctxt=entry.msgctxt,
                        msgid=entry.msgid,
                        msgstr=entry.msgid
                        )
                elif "DETAIL_EXPLAIN" in entry.msgctxt:
                    translated_entry = polib.POEntry(
                        msgctxt=entry.msgctxt,
                        msgid=entry.msgid,
                        msgstr=entry.msgid
                        )
                elif str(entry.msgid) or re.search("^\s*$", (entry.msgid)):
                    response = requests.post('http://localhost:5000/translate', headers=headers, data=data)
                    json_data = json.loads(response.text)   
                    msgstr=str(json_data["translatedText"])    
                    if "<Sign" in str(entry.msgid):
                        msgctxt=str(entry.msgctxt)
                        substringButtons = str(entry.msgid).split("<Sign:",1)[1][0]
                        msgstr.replace("<Sign >", "<Sign:"+substringButtons+">")
                    if str(msgstr) or re.search("^\s*$", (msgstr)):
                        translated_entry = polib.POEntry(
                            msgctxt=entry.msgctxt,
                            msgid=entry.msgid,
                            msgstr=msgstr
                            )
                    else:
                        translated_entry = polib.POEntry(
                            msgctxt=entry.msgctxt,
                            msgid=entry.msgid,
                            msgstr=entry.msgid
                            )
                else:
                    translated_entry = polib.POEntry(
                        msgctxt=entry.msgctxt,
                        msgid=entry.msgid,
                        msgstr=entry.msgid
                        )
            else:    
                translated_entry = polib.POEntry(
                    msgctxt=entry.msgctxt,
                    msgid=entry.msgid,
                    msgstr=entry.msgstr
                )
            output_file.append(translated_entry)
            c += 1
    if realPath.isfile(fileName.replace("..\\firstdir\\", "..\\lastdir\\")) == False:
        output_file.save(fileName.replace("..\\firstdir\\", "..\\lastdir\\"))
        with open(fileName.replace("..\\firstdir\\", "..\\lastdir\\"), 'r', encoding="utf8") as fin:
            data = fin.read().splitlines(True)
        with open(fileName.replace("..\\firstdir\\", "..\\lastdir\\"), 'w', encoding="utf8") as fout:
            fout.writelines(data[1:])
