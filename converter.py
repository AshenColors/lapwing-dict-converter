import ijson, json
from pathlib import Path

BASE_DICT = Path.cwd() / "steno-dictionaries" / "lapwing-base.json"
NUMBER_DEFS = {
    "1": "S",
    "2": "T",
    "3": "P",
    "4": "H",
    "5": "A",
    "0": "O",
    "6": "F",
    "7": "P",
    "8": "L",
    "9": "T",
}


with open("converted-lapwing-base.json", "w", encoding="UTF-8") as converted_json:
    converted_dict = {}
    with open(BASE_DICT, "r", encoding="UTF-8") as base:
        entries = ijson.kvitems(base, "")
        for k, v in entries:
            # print(f"k: {k}, v: {v}")
            if "&" in k and any(str(n) in k for n in range(10)):
                # we don't want this entry, skip it
                continue
            if any(str(n) in k for n in range(10)):
                new_k = "+" + k
                for number, stenokey in NUMBER_DEFS.items():
                    new_k = new_k.replace(number, stenokey)
            else:
                new_k = k
            converted_dict.update({new_k: v})
    converted_json.write(
        json.dumps(converted_dict, sort_keys=True, indent=0, ensure_ascii=False)
    )
