import Preprocess, ContentBased, NearestNeighbor
import time
from consolemenu import *
from consolemenu.items import *


def runPreprocess():
    time.sleep(1)
    Preprocess.main()
    time.sleep(1)


def runContent():
    time.sleep(1)
    ContentBased.main()
    time.sleep(1)


def runNN():
    time.sleep(1)
    NearestNeighbor.main()
    time.sleep(1)


if __name__ == "__main__":
    TITLE = "-------------Welcome to Anime Recommendation System-------------"
    SUBTITLE = "Please choose an option to continue demonstration"
    menu = ConsoleMenu(TITLE, SUBTITLE)
    function_preprocess = FunctionItem("Preprocess", runPreprocess)
    function_content = FunctionItem("Content Based", runContent)
    function_nn = FunctionItem("Nearest Neighbor", runNN)

    menu.append_item(function_preprocess)
    menu.append_item(function_content)
    menu.append_item(function_nn)
    menu.show()
    print("See you later!")
