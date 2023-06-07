from typing import List

## Author(s): Josue N Rivera

def prune_str(text: str) -> str:
    return  text.replace("_", "").replace(" ", "").upper()

def prune_str_list(texts: List[str]) -> List[str]:
    return [prune_str(text) for text in texts]
