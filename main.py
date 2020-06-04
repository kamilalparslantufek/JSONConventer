from src.getjson import get_json
from src.convertjson import Converter

def run():
    url = input("Enter JSON link to convert :")
    result = get_json(url)
    csv = Converter().convert2csv(result)
    print(csv)
    mydb = Converter().convert2sql(result)

if __name__ == "__main__":
    run()