def capitalize(fn):
    def inner(name):
        result = fn(name)
        result = result.replace(name, f"Mr. {name}")

        return result

    return inner
@capitalize
def hello(name):
    return f"Hello {name}"

@capitalize
def goodbye(name):
    return f"Bye {name}"

print(hello("mateusz"))
print(goodbye("mateusz"))