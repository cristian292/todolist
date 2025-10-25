#!/usr/bin/env python3
import datetime
import json
import argparse

def openJson():
    try:
        with open("task.json", "r",encoding="utf-8") as file:
            tasks = json.load(file)
    except(json.JSONDecodeError):
        tasks = []
    return tasks

def saveJson(x):
    with open("task.json","w",encoding="utf-8") as file:
        json.dump(x,file,indent=4)


def citire(description):
    properties = {
        "id" : 1,
        "description" : description,
        "status" : "todo",
        "createdAt" : datetime.datetime.now().isoformat(),
        "updatedAt" : datetime.datetime.now().isoformat()
    }
    return properties

        
def saveTask(task):
    tasks = openJson()
    new_id = len(tasks)+1
    now = datetime.datetime.now().isoformat()
    task = {
        "id": new_id,
        "description": task,
        "status": "todo",
        "createdAt": datetime.datetime.now().isoformat(),
        "updatedAt": datetime.datetime.now().isoformat()
    }
    tasks.append(task)
    saveJson(tasks) 


def updateTask(ID, update):
    tasks=openJson()

    tasks[ID-1]['description'] = update
    tasks[ID-1]['updatedAt'] = datetime.datetime.now().isoformat()

    saveJson(tasks)


def deleteTask(ID):
    tasks=openJson()

    tasks.pop(ID-1)
    
    saveJson(tasks)

        
def markInProgress(ID,update):
    tasks=openJson()

    tasks[ID-1]['status'] = update
    tasks[ID-1]['updatedAt'] = datetime.datetime.now().isoformat()

    saveJson(tasks)

def show(status):
    tasks=openJson()
    cnt=1
    for i in tasks:
        if i["status"]==status:
            print(f"{i["id"]}. {i["description"]}")
            cnt+=1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Task manager CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Add Task
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", type=str, help="Task description")

    # Update Task
    upd_parser = subparsers.add_parser("update", help="Update a task")
    upd_parser.add_argument("task_id", type=int, help="Task ID to update")
    upd_parser.add_argument("description", type=str, help="New description")

    # Delete Task
    del_parser = subparsers.add_parser("delete", help="Delete a task")
    del_parser.add_argument("task_id", type=int, help="Task ID to delete")

    # Mark task
    mark_parser = subparsers.add_parser("mark", help="Mark task as in-progress or done")
    mark_parser.add_argument("task_id", type=int, help="Task ID to mark")
    mark_parser.add_argument("update",type=str)

    #all tasks that are [...]
    show_parser = subparsers.add_parser("show", help="Outputs all the tasks that are done")
    show_parser.add_argument("status",type=str)


args = parser.parse_args()

if args.command == "add":
    saveTask(args.description)
elif args.command == "update":
    updateTask(args.task_id, args.description)
elif args.command == "delete":
    deleteTask(args.task_id)
elif args.command == "mark":
    markInProgress(args.task_id,args.update)
elif args.command == "show":
    show(args.status)
else:
    parser.print_help()