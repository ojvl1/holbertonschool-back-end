#!/usr/bin/python3
"""API REST"""
import requests
import argv


def get_employee(id=None):
    """
    Function that retrive information from the REST API
    """
    # check if argv[1] is a number int
    if len(argv) > 1:
        try:
            id = int(argv[1])
        except ValueError:
            return

    if isinstance(id, int):
        base = "https://jsonplaceholder.typicode.com"
        user = requests.get(f"{base}/users/{id}").json()
        to_dos = requests.get(f"{base}/todos/?userId={id}").json()

        if user and to_dos:
            total_tasks = len(to_dos)
            # fmt: off
            titles_completed = [task["title"]
                                for task in to_dos
                                if task["completed"]]
            # fmt: on
            tasks_completed = len(titles_completed)

            print(
                "Employee {} is done with tasks({}/{}):".format(
                    user["name"], tasks_completed, total_tasks
                )
            )

            for title in titles_completed:
                print(f"\t {title}")


if __name__ == "__main__":
    get_employee()
