if __name__ == "__main__":
    import UtilClasses
    matrix = UtilClasses.Matrix([range(i,i+6,2) for i in range(1,6)])
    print(matrix)
    for r in matrix:
        print r

    