# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

x="""
123
456
789
"""
# Press the green button in the gutter to run the script.
import json
if __name__ == '__main__':
    k = ["hi\nzifuchuan\n999", "99\nuihgdh\n782"]
    with open("./kk.jsonl","w",encoding="utf-8")as f:
        for i in k:
            f.write(json.dumps(i,ensure_ascii=False)+"\n")
        f.write(json.dumps(x,ensure_ascii=False)+"\n")
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/