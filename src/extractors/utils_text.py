PREFIXES = ["best", "top", "cheap", "new"]
SUFFIXES = ["2024", "ideas", "review", "tutorial"]

def generate_prefix_suffix_variants(query: str, use_prefix: bool, use_suffix: bool):
    variants = []

    if use_prefix:
        for p in PREFIXES:
            variants.append(f"{p} {query}")

    if use_suffix:
        for s in SUFFIXES:
            variants.append(f"{query} {s}")

    return variants