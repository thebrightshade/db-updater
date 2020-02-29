import pandas
import os

data = {"ADB ID":[""],
        'DEVICE ID':[""],
        "CARRIER":[""],
        "PH. NUMBER":[""],
        "CALL TO NO.":[""],
        "BUILD ID":[""],
        "SCENARIO":[""],
        "MARKET":[""],
        "TESTER NAME":[""]}

def create_csv():
    cols=["ADB ID","DEVICE ID","CARRIER","PH. NUMBER","CALL TO NO.","BUILD ID","SCENARIO","MARKET","TESTER NAME"]
    f = open("database.csv", "w+")
    for i,item in enumerate(cols):
        if i+1<len(cols):
            f.write("{},".format(item))
        else:
            f.write(item)
    f.close()

def connect():
    if not os.path.exists("database.csv"):
        create_csv()
    db = pandas.read_csv("database.csv")
    db.set_index(["ADB ID"],inplace=True,drop=True)
    return db

def set_data(device_id, adb_id, operator_name, phone_no, call_to_no, build_id, scenario, market, tester_name):
    data["ADB ID"] = [adb_id]
    data["DEVICE ID"] = [device_id]
    data["CARRIER"] = [operator_name]
    data["PH. NUMBER"] = [phone_no]
    data["CALL TO NO."] = [call_to_no]
    data["BUILD ID"] = [build_id]
    data["SCENARIO"] = [scenario]
    data["MARKET"] = [market]
    data["TESTER NAME"] = [tester_name]
    return data

def update(device_id, adb_id, operator_name, phone_no, call_to_no, build_id, scenario, market, tester_name):
    data = set_data(device_id, adb_id, operator_name, phone_no, call_to_no, build_id, scenario, market, tester_name)
    db = connect()
    df1 = pandas.DataFrame(data)
    df1.set_index(['ADB ID'], inplace=True, drop=True)
    if adb_id in db.index:
        db.loc[adb_id] = df1.loc[adb_id]
    elif adb_id != "":
        db = pandas.concat([db, df1], sort=False)
    else:
        pass
    db.to_csv('database.csv')
    return db


def view():
    db = connect()
    return db


def delete(adb_id=''):
    db = connect()
    if adb_id in db.index:
        db = db.drop([adb_id])
    db.to_csv('database.csv')
    return db

# import pdb; pdb.set_trace()
# update("N10PRDTVB","9710474a","TMO","4253899346","4256145362","SM8250-SDX55LA-945-HI-c9-169","SMARTEST","LV-mmW","SHADMAAN")

# print(view())
