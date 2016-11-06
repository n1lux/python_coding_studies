
def even_integers_generetor(n):
    for i in range(n):
        if i % 2 == 0:
            yield i


# generetor expression
def generetor_expression_upper_items(items_list):
    return (item.upper() for item in items_list)

if __name__ == "__main__":
    inter = even_integers_generetor(50)
    print(next(inter))
    print(next(inter))
    print(next(inter))
    print(next(inter))
    print(next(inter))
    print(next(inter))
    print(next(inter))



    for i in even_integers_generetor(10):
        print(i)
