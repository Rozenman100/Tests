
def create_pascal_pyramid(bottom: int) -> list[list]:
    print(" " * bottom, [1])

    if bottom == 1:
        return 
    else:
        def create_row(last_row, break_point):
            row = [1]
            for i in range(len(last_row)):
                if i == len(last_row) - 1:
                    row.append(1)
                else:
                    row.append(last_row[i] + last_row[i+1])
            print(" " * break_point, row)
            if break_point == 1:
                return
            else:
                create_row(row, break_point - 1)
        
        create_row([1], bottom - 1)

        
create_pascal_pyramid(8)

# create first row

# create second row while appending it
